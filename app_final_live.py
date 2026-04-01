import streamlit as st
import base64
from openai import OpenAI
import io
import wave
from PIL import Image

# --- 기본 설정 ---
SAMPLE_RATE = 24000 

def encode_image(image_file):
    image_file.seek(0)
    return base64.b64encode(image_file.read()).decode("utf-8")

def pcm_to_wav(pcm_data):
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(pcm_data)
    return buf.getvalue()

# --- UI 구성: 사이드바 (API 키 입력) ---
st.set_page_config(page_title="Kanana 통합 분석기", layout="wide")

with st.sidebar:
    st.title("🔑 서비스 설정")
    st.info("서비스를 이용하려면 API 키가 필요합니다.")
    
    # API 키 입력창 (비밀번호 형식)
    user_api_key = st.text_input("Kanana API Key 입력", type="password", placeholder="KC_IS_...")
    
    if not user_api_key:
        st.warning("⚠️ API 키를 입력해 주세요.")
        st.stop()  # API 키가 없으면 여기서 실행을 멈춤
    else:
        st.success("✅ 인증되었습니다.")
        st.divider()
        st.caption("설정 완료. 이제 이미지를 분석할 수 있습니다.")

# --- API 클라이언트 초기화 (사용자가 입력한 키 사용) ---
client = OpenAI(
    base_url="https://kanana-o.a2s-endpoint.kr-central-2.kakaocloud.com/v1",
    api_key=user_api_key
)

# --- 메인 화면 (API 키가 있어야만 아래 내용이 나타남) ---
st.title("🖼️ Kanana 그림 분석기")
st.write("이미지와 질문을 입력하고, 원하는 결과 형태를 선택하세요.")

uploaded_file = st.file_uploader("이미지 업로드", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 4:5 비율 레이아웃
    col1, col2 = st.columns([4, 5], gap="large")

    with col1:
        st.subheader("🖼️ 업로드 이미지")
        st.image(uploaded_file, use_container_width=True)
    
    with col2:
        st.subheader("🔍 분석 제어판")
        
        # 질문 입력
        user_prompt = st.text_area("질문을 입력하세요 (비워두면 기본 분석을 수행합니다)", 
                                   placeholder="예: 이 사진 분위기를 설명해줘.")
        
        # 출력 형태 선택
        output_format = st.radio("결과를 어떤 형태로 받으시겠습니까?", 
                                 options=["선택 안 함", "텍스트로 읽기", "음성으로 듣기"],
                                 index=0)
        
        st.divider()
        
        result_area = st.container()
        
        # 버튼 활성화 조건
        analyze_ready = output_format != "선택 안 함"
        analyze_btn = st.button("분석 시작", type="primary", use_container_width=True, disabled=not analyze_ready)

        if not analyze_ready:
            st.caption("⚠️ 결과를 받을 형태를 선택해야 버튼이 활성화됩니다.")

        if analyze_btn:
            with st.spinner("AI가 분석 중입니다..."):
                try:
                    image_b64 = encode_image(uploaded_file)
                    final_prompt = user_prompt if user_prompt.strip() else "이미지를 보고 한국어로 자세하게 설명해줘."
                    
                    # 1. 텍스트 모드 (중복 증식 방지)
                    if output_format == "텍스트로 읽기":
                        response = client.chat.completions.create(
                            model="kanana-o",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
                                        {"type": "text", "text": final_prompt}
                                    ]
                                }
                            ],
                            modalities=["text"],
                            stream=False
                        )
                        result_text = response.choices[0].message.content
                        with result_area:
                            st.success("✅ 분석 완료!")
                            st.markdown(f"### 📝 분석 결과\n\n{result_text}")

                    # 2. 음성 모드
                    elif output_format == "음성으로 듣기":
                        response = client.chat.completions.create(
                            model="kanana-o",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
                                        {"type": "text", "text": final_prompt}
                                    ]
                                }
                            ],
                            modalities=["text", "audio"],
                            stream=True
                        )

                        all_audio_bytes = b""
                        for chunk in response:
                            if not chunk.choices: continue
                            delta = chunk.choices[0].delta
                            if hasattr(delta, 'audio') and delta.audio:
                                audio_payload = delta.audio
                                b64_pcm = audio_payload.get("data") if isinstance(audio_payload, dict) else getattr(audio_payload, "data", None)
                                if b64_pcm:
                                    all_audio_bytes += base64.b64decode(b64_pcm)

                        with result_area:
                            if all_audio_bytes:
                                wav_data = pcm_to_wav(all_audio_bytes)
                                st.success("✅ 음성 생성 완료")
                                st.audio(wav_data, format="audio/wav")
                            else:
                                st.error("음성 데이터를 생성하지 못했습니다.")

                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")
else:
    st.info("👈 왼쪽에서 이미지를 먼저 업로드해 주세요.")

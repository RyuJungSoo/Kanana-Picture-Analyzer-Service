# 🦁 Kanana Picture Analyzer (그림 분석기)
이미지를 보고, 읽어주고, 들려주는 똑똑한 AI 가이드    
> Kakao의 Kanana-o 모델을 활용하여 이미지와 텍스트를 동시에 분석하고, 결과값을 텍스트 또는    
**고음질 음성(TTS)** 으로 제공하는 멀티모달 서비스입니다.

[그림 분석기 바로가기](https://kanana-picture-analyzer-service-agq7tqq7w9xpy2ymtmu6fz.streamlit.app/)

---
## ✨ 주요 기능 (Key Features)
* 🖼️ 멀티모달 분석: 이미지를 업로드하고 질문을 입력하면 AI가 상황을 정밀하게 분석합니다.

* 🎧 결과 선택 모드 : 분석 결과를 눈으로 읽는 텍스트 모드와 귀로 듣는 음성 모드 중 선택할 수 있습니다.

* 🔐 보안 강화 (Sidebar API Key): 사용자의 API 키가 코드에 노출되지 않도록 사이드바를 통해 안전하게 입력받는 구조를 채택했습니다.
       
---
## 🛠 기술 스택 (Tech Stack)
| 구분 | 기술 / 라이브러리 | 상세 역할 |
| :---: | :---: | :---: |
| Language | Python 3.x | 서비스 로직 및 데이터 처리 메인 언어 |
| Framework | Streamlit | 대화형 웹 인터페이스 및 프론트엔드 구성 |
| AI Model | Kanana-o | 멀티모달 분석 및 음성 생성 모델 |
| API Bridge | OpenAI SDK |	Kanana-o 모델과의 안정적인 통신 및 스트리밍 처리 |
| Image | Pillow (PIL) | 이미지 파일 로드 및 전처리를 위한 라이브러리 |
| Audio |	Wave / IO |	PCM 음성 데이터를 WAV 형식으로 변환 및 바이너리 처리 |
| Deployment | Streamlit Cloud | GitHub 연동을 통한 24시간 클라우드 호스팅 서비스 |
       
---
## 🚀 시작하기 (Getting Started)
<img width="212" height="251" alt="Image" src="https://github.com/user-attachments/assets/785699d2-a6a3-4180-8e5a-27d2562d26db" />        
          
1. 앱이 실행되면 왼쪽 사이드바에 Kanana API Key를 입력합니다.            
                  
<img width="989" height="337" alt="Image" src="https://github.com/user-attachments/assets/f62ab6fd-23eb-49f6-8310-9215fc90b8c9" />                     
                                       
2. 분석하고 싶은 이미지를 업로드합니다.
                     
<img width="989" height="559" alt="Image" src="https://github.com/user-attachments/assets/2e970ee5-f6ac-4101-ba02-d02dddc90797" />                  
                         
3. 추가 질문이 있다면 텍스트 창에 입력합니다. (비워둘 시 기본 분석 수행)                            
                              
<img width="549" height="364" alt="Image" src="https://github.com/user-attachments/assets/6687a8f7-0688-4981-a7c4-381feff7cb97" />          
                                   
4. **[결과 형태(텍스트/음성)]** 를 선택하고 '분석 시작' 버튼을 누릅니다.

---
## 🌟 기대 효과 및 확장 가능성 (Expected Effects)
본 프로젝트는 단순한 분석 도구를 넘어, 다음과 같은 **배리어 프리(Barrier-Free)** 서비스로의 확장 잠재력을 가지고 있습니다.

* **미술관 디지털 도슨트**: 시각 장애인 관람객에게 작품의 구도, 색감, 분위기를 상세한 음성으로 묘사하여 독립적인 예술 감상을 지원합니다.
* **지능형 전시 안내**: 관람객의 실시간 질문에 맞춰 작품의 세부 정보를 설명해 주는 맞춤형 안내 단말기로 활용 가능합니다.
* **정보 격차 해소**: Kanana-o의 정밀한 멀티모달 분석력을 통해 시각 정보 접근이 어려운 환경에서 혁신적인 가이드를 제공합니다.

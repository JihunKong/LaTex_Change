# LaTex_Change
# LaTeX-to-Readable Math Converter

이 앱은 복잡한 LaTeX 수식을 일반적인 수학 표기법으로 바꿔주는 스트림릿 기반 웹 애플리케이션입니다. 학생, 교사 및 일반 사용자들이 수학 문제의 풀이 과정을 보다 쉽게 이해할 수 있도록 지원합니다.

## 🛠️ 주요 기능

- **LaTeX 수식 변환**: LaTeX 형식으로 작성된 수학 문제 및 해설을 일반적인 기호와 문장으로 변환합니다.
- **실시간 미리보기**: 입력 즉시 변환된 결과를 확인할 수 있습니다.
- **쉬운 복사 기능**: 변환된 결과를 클릭 한 번으로 복사하여 편리하게 사용할 수 있습니다.

## 🚀 빠른 시작

### 설치 방법

1. 저장소를 클론합니다:
   ```bash
   git clone https://github.com/yourusername/latex-to-readable-math.git
   cd latex-to-readable-math
   ```

2. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

3. 앱을 실행합니다:
   ```bash
   streamlit run app.py
   ```

## 📖 사용 예시

다음과 같은 LaTeX 코드:

```latex
\alpha + \beta = 2\sqrt{3} + \sqrt{3} = 3\sqrt{3}
```

변환 결과:

```
α + β = 2√3 + √3 = 3√3
```

## 📁 프로젝트 구조

```
latex-to-readable-math/
├── app.py
├── requirements.txt
└── README.md
```

## 🤝 기여하기

이 프로젝트에 기여하고 싶다면 언제든지 풀 리퀘스트를 제출하거나 이슈를 생성해주세요. 개선 제안과 버그 리포트는 언제나 환영입니다!

## 📜 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다.

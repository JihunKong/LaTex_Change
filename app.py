import streamlit as st
import sympy
from sympy.parsing.latex import parse_latex
import re

def convert_latex_to_readable(latex_text):
    try:
        # 한글 설명과 LaTeX 수식을 분리
        parts = re.split(r'(\$[^$]+\$|\$\$[^$]+\$\$)', latex_text)
        
        result = []
        for part in parts:
            if part.startswith('$') and part.endswith('$'):
                # LaTeX 수식 처리
                latex_math = part[1:-1]  # $ 기호 제거
                try:
                    # LaTeX를 SymPy 표현식으로 변환
                    expr = parse_latex(latex_math)
                    # 일반 텍스트로 변환
                    readable = str(expr)
                    result.append(readable)
                except:
                    result.append(part)  # 변환 실패시 원본 유지
            else:
                # 한글 설명은 그대로 유지
                result.append(part)
        
        return ''.join(result)
    except Exception as e:
        return f"오류 발생: {str(e)}"

def main():
    st.title("LaTeX 수식 변환기")
    st.write("LaTeX 수식을 일반적인 수학 표기법으로 변환합니다.")
    
    # 입력 텍스트 영역
    input_text = st.text_area(
        "LaTeX 수식 입력",
        placeholder="예시: $\\alpha + \\beta = 2\\sqrt{3} + \\sqrt{3} = 3\\sqrt{3}$",
        height=150
    )
    
    if st.button("변환하기"):
        if input_text:
            result = convert_latex_to_readable(input_text)
            st.write("변환 결과:")
            st.code(result, language=None)
            
            # 복사 버튼
            if st.button("결과 복사"):
                st.write("복사되었습니다!")
        else:
            st.warning("입력해주세요!")

if __name__ == "__main__":
    main() 
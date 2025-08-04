"""
토목공사 재료 무게 계산기
Civil Engineering Materials Weight Calculator
"""

import streamlit as st
import pandas as pd
import numpy as np
from materials_data import get_materials_df, get_material_density, get_materials_by_category, MATERIALS_DATA

def main():
    # 페이지 설정
    st.set_page_config(
        page_title="토목공사 재료 무게 계산기",
        page_icon="🏗️",
        layout="wide"
    )
    
    # 메인 제목
    st.title("🏗️ 토목공사 재료 무게 계산기")
    st.markdown("**부피(m³)를 입력하여 토목공사 재료의 무게를 계산하세요**")
    
    # 사이드바 - 재료 정보 테이블
    with st.sidebar:
        st.header("📋 재료 밀도 참조표")
        
        # 카테고리별 필터
        categories = list(set([info["category"] for info in MATERIALS_DATA.values()]))
        selected_category = st.selectbox(
            "분류별 보기",
            ["전체"] + categories,
            key="category_filter"
        )
        
        # 재료 데이터 표시
        df = get_materials_df()
        if selected_category != "전체":
            df = df[df["분류"] == selected_category]
        
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown("---")
        st.markdown("**📖 사용법:**")
        st.markdown("1. 재료를 선택하세요")
        st.markdown("2. 부피(m³)를 입력하세요")
        st.markdown("3. 계산 결과를 확인하세요")
    
    # 메인 영역을 두 개 컬럼으로 분할
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📐 계산 입력")
        
        # 재료 선택
        material_options = list(MATERIALS_DATA.keys())
        selected_material = st.selectbox(
            "재료 선택",
            material_options,
            key="material_select"
        )
        
        # 선택된 재료의 밀도 표시
        density = get_material_density(selected_material)
        st.info(f"**{selected_material}**의 밀도: **{density:,} kg/m³**")
        
        # 부피 입력
        volume = st.number_input(
            "부피 입력 (m³)",
            min_value=0.001,
            max_value=100000.0,
            value=1.0,
            step=0.1,
            format="%.3f",
            key="volume_input"
        )
        
        # 계산 버튼
        calculate_button = st.button("🧮 계산하기", type="primary", use_container_width=True)
    
    with col2:
        st.header("📊 계산 결과")
        
        if calculate_button or volume > 0:
            try:
                # 무게 계산 (kg)
                weight_kg = volume * density
                weight_ton = weight_kg / 1000
                
                # 결과 표시
                st.success("✅ 계산 완료!")
                
                # 결과 메트릭
                col_kg, col_ton = st.columns(2)
                
                with col_kg:
                    st.metric(
                        label="무게 (kg)",
                        value=f"{weight_kg:,.2f} kg"
                    )
                
                with col_ton:
                    st.metric(
                        label="무게 (ton)",
                        value=f"{weight_ton:.3f} ton"
                    )
                
                # 계산 공식 표시
                st.markdown("---")
                st.markdown("**📋 계산 공식:**")
                st.latex(r"무게(kg) = 부피(m³) \times 밀도(kg/m³)")
                st.markdown(f"**계산:** {volume} m³ × {density:,} kg/m³ = **{weight_kg:,.2f} kg**")
                
                # 추가 정보
                st.markdown("---")
                st.markdown("**📝 계산 세부사항:**")
                calculation_data = {
                    "항목": ["재료명", "부피", "밀도", "무게 (kg)", "무게 (ton)"],
                    "값": [
                        selected_material,
                        f"{volume} m³",
                        f"{density:,} kg/m³",
                        f"{weight_kg:,.2f} kg",
                        f"{weight_ton:.3f} ton"
                    ]
                }
                
                result_df = pd.DataFrame(calculation_data)
                st.dataframe(result_df, hide_index=True, use_container_width=True)
                
                # 결과 내보내기
                csv_data = result_df.to_csv(index=False, encoding='utf-8-sig')
                st.download_button(
                    label="📥 결과 다운로드 (CSV)",
                    data=csv_data,
                    file_name=f"재료무게계산_{selected_material}_{volume}m3.csv",
                    mime="text/csv"
                )
                
            except Exception as e:
                st.error(f"❌ 계산 중 오류가 발생했습니다: {str(e)}")
        else:
            st.info("👆 왼쪽에서 재료를 선택하고 부피를 입력한 후 '계산하기' 버튼을 클릭하세요.")
    
    # 하단 정보
    st.markdown("---")
    
    # 주의사항
    with st.expander("⚠️ 주의사항 및 면책조항"):
        st.markdown("""
        **주의사항:**
        - 이 계산기는 일반적인 재료 밀도 값을 사용합니다.
        - 실제 밀도는 재료의 품질, 함수율, 온도 등에 따라 달라질 수 있습니다.
        - 정확한 계산을 위해서는 실제 재료의 밀도 측정값을 사용하시기 바랍니다.
        - 본 계산 결과는 참고용이며, 실제 공사에 사용 시 전문가의 검토를 받으시기 바랍니다.
        
        **데이터 출처:**
        - 한국건설기술연구원 표준
        - KS 규격 기준값
        - 일반적인 공학 참고서 값
        """)
    
    # 앱 정보
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666666; font-size: 0.8em;'>
        토목공사 재료 무게 계산기 | 개발: Streamlit Python | 
        버전: 1.0 | 업데이트: 2025.08.03
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

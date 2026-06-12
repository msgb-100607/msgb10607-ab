import streamlit as st

# 세션 상태(Session State)를 이용해 입력 기록을 저장할 리스트 초기화
if "weight_list" not in st.session_state:
    st.session_state.weight_list = []
if "food_list" not in st.session_state:
    st.session_state.food_list = []

# 웹 페이지 제목 설정
st.title("🐾 반려동물 권장사료량 안내 프로그램")
st.write("반려동물의 몸무게를 입력하시면 알맞은 권장 사료량을 안내해 드립니다.")

st.divider() # 구분선

# 1. 입력부 (Sidebar 또는 메인 화면에 배치 가능)
st.subheader("🔢 몸무게 입력")
weight = st.number_input(
    "반려동물의 몸무게(kg)를 입력하세요:", 
    min_value=0, 
    max_value=100, 
    value=0, 
    step=1
)

# 2. 로직 처리 (기존 코드의 조건문 유지, 오타 수정 foood -> food)
if weight == 0:
    st.info("💡 몸무게를 입력하시면 계산이 시작됩니다. (0kg은 종료 상태를 의미합니다.)")
else:
    if weight <= 5:
        food = 100
    elif weight <= 10:
        food = 180
    elif weight <= 20:
        food = 300
    else:
        food = 450

    # 3. 출력부 (결과 표시)
    st.success(f"🎉 몸무게 **{weight}kg**의 권장 사료량은 **{food}g**입니다.")
    
    # '기록하기' 버튼을 누르면 리스트에 추가 (선택 사항)
    if st.button("현재 결과 기록하기"):
        st.session_state.weight_list.append(weight)
        st.session_state.food_list.append(food)
        st.toast("기록이 완료되었습니다!", icon="💾")

# 4. 저장된 데이터 확인 (기존 weight_list, food_list 활용)
if st.session_state.weight_list:
    st.divider()
    st.subheader("📊 계산 기록 확인")
    
    # 데이터를 표(Dataframe) 형태로 보여주기 위해 딕셔너리 생성
    history_data = {
        "몸무게 (kg)": st.session_state.weight_list,
        "권장 사료량 (g)": st.session_state.food_list
    }
    st.dataframe(history_data, use_container_width=True)
    
    # 기록 초기화 버튼
    if st.button("기록 전체 삭제"):
        st.session_state.weight_list = []
        st.session_state.food_list = []
        st.rerun()
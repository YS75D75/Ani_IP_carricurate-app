import streamlit as st

st.title("実験用 計算ツール")

# 入力欄（スマホでも数字の増減がしやすいスライダー＋入力枠になります）
x = st.number_input("マウスの体重（g）は？", min_value=1.0, value=20.0, step=0.1)

# 計算処理
injection_min = 20 * (x * 0.001)
injection_max = 80 * (x * 0.001)
ani_g = 50 * (x * 0.001)

if injection_min > 0:
    ani_injection = ani_g / injection_min
else:
    ani_injection = 0

# 計算結果を綺麗にスマホ向けに表示
st.subheader("計算結果")
st.success(f"腹腔内投与許容量: {injection_min:.2f} μl - {injection_max:.2f} μl")
st.info(f"必要Ani量: {ani_g:.2f} mg")
st.warning(f"作成するAniの濃度: {ani_injection:.4f} mg/μl")

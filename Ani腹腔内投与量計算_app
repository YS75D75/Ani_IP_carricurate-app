import streamlit as st

st.title("実験用 計算ツール")

# 入力フォーム（数値入力をスマホでもしやすくする）
x = st.number_input("マウスの体重（g）は？", min_value=1.0, value=20.0, step=0.1)

# 計算処理
injection_min = 20 * (x * 0.001)
injection_max = 80 * (x * 0.001)
ani_g = 50 * (x * 0.001)

# ゼロ除算（エラー）を防ぐ対策
if injection_min > 0:
    ani_injection = ani_g / injection_min
else:
    ani_injection = 0

# 結果の表示（綺麗に見やすく装飾）
st.subheader("計算結果")
st.success(f"腹腔内投与許容量: {injection_min:.2f} μl - {injection_max:.2f} μl")
st.info(f"必要Ani量: {ani_g:.2f} mg")
st.warning(f"作成するAniの濃度: {ani_injection:.4f} mg/μl")


import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# 初期化
if "answered" not in st.session_state:
    st.session_state.answered = False

quiz = {
    "question": "ここはどこでしょう？",
    "image_path": "Room.png",
    "options": ["大学院/学生研究室", "PCルーム", "コンピュータ室", "自習室"],
    "answer": "大学院/学生研究室"
}

st.set_page_config(layout="centered")
st.title("🖼️データサイエンス学部クイズ")

# 画像読み込み＆縮小
image = Image.open(quiz["image_path"])
image = image.resize((350, int(image.height * 350 / image.width)))  # 幅350pxに縮小

# PIL画像をbase64に変換してHTMLで中央表示
buffered = BytesIO()
image.save(buffered, format="PNG")
img_base64 = base64.b64encode(buffered.getvalue()).decode()

# HTMLで中央表示
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_base64}" alt="quiz image" style="max-width: 100%; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader(quiz["question"])
user_answer = st.radio("選択肢を選んでください", quiz["options"])

if st.button("答える"):
    st.session_state.answered = True
    st.session_state.user_answer = user_answer

if st.session_state.answered:
    if st.session_state.user_answer == quiz["answer"]:
        st.success("正解！🎉")
    else:
        st.error(f"不正解！正解は「{quiz['answer']}」です。")
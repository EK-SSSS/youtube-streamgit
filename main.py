import streamlit as st
import time
st.title("Streamlit 超入門")

st.write("プレぐれすばーの表示")
"Start!"

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!"

left_column,right_column=st.columns(2)
button=left_column.button("右からむに文字を表示")
if button:
    right_column.write("ここは右カラム")
expader=st.expander("問い合わせ")
expader.write("問い合わせを書く")
expader.write("問い合わせを書く")
expader.write("問い合わせを書く")
# text=st.sidebar.text_input("あなたの趣味を教えて。")
# "あなたの趣味:",text
# if st.checkbox("Show Image"):
#     img=Image.open('pen.png ')
#     st.image(img, caption='pengin', use_container_width=True)

# condition=st.sidebar.slider("今のあなたの調子は？",0,100,50)
# "コンディション:",condition
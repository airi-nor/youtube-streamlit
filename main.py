import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')

'Start!'

#barの上に表示されるlatest iteration。空で用意
latest_iteration = st.empty()
#バーを用意
bar = st.progress(0)

for i in range(100):
    #for文回す度にiterationの中身が徐々に追加される
    latest_iteration.text(f'Iteration {i + 1}')
    #barを進化させている
    bar.progress(i + 1)
    #0.1秒ごとにfor文を回す
    time.sleep(0.1)
    #1にすると一秒ごとに

'Done!'
#for文が終わると表示される

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')

expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)


# 'あなたの趣味:', text, 'です'
# 'コンディション:', condition


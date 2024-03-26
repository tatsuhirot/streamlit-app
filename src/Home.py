# streamlit を使用するために import します
import streamlit as st

# ページタイトルを表示します
st.title('Streamlit app')

# `h2` タグとして表示するために `markdown` 記法を使用しています
st.markdown('## Streamlit の紹介')
st.markdown('Python のフレームワーク, Streamlit の紹介です. このページは Streamlit を使って実装してます.')

# こちらも markdown 記法を利用して `h3` タグと `a` タグを実現してます
st.markdown('### API Reference')
link = '[Streamlit API](https://docs.streamlit.io/library/api-reference)'
comment = f'{link}: Streamlit の API については左こちらのリンクを参照してください.'

# unsafe_allow_html=True とすることで html タグを html として解釈させます( 公式では非推奨としています )
# 下記リファレンスをご参照ください
# https://docs.streamlit.io/1.12.0/library/api-reference/text/st.markdown#stmarkdown
st.markdown(comment, unsafe_allow_html=True)
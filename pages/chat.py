import streamlit as st

from sqls.chat_sql import chat_sql

st.set_page_config(layout="wide")
conn = st.connection("mysql", type="sql")

if "page" not in st.session_state:
    st.session_state.page = 1
if "pagesize" not in st.session_state:
    st.session_state.pagesize = 15

st.markdown("""
<style>
[data-testid="block-container"] {
    padding: 3rem; 
}
</style>
""", unsafe_allow_html=True)


def get_chat():
    sql = chat_sql.format(
        pagesize=st.session_state.pagesize,
        offset=st.session_state.page * st.session_state.pagesize
    )
    df = conn.query(sql=sql)
    df = df.set_index("id")
    return df


def get_total_chat_count():
    df = conn.query(sql="SELECT COUNT(*) AS cnt FROM kakaotalk_chat")
    return df.iloc[0]["cnt"]


def change_page():
    selected_page = int(st.session_state["select_page"].split(" / ")[0])
    st.session_state.page = selected_page


st.title("채팅 대쉬보드")
df = get_chat()
total_count = get_total_chat_count()
total_pages = total_count // st.session_state.pagesize + 1

cols = st.columns(3)
with cols[0]:
    st.selectbox(
        label="페이지",
        label_visibility="collapsed",
        options=[f"{x+1} / {total_pages} 페이지" for x in range(total_pages)],
        index=st.session_state.page - 1,
        on_change=change_page,
        key="select_page"
    )
st.dataframe(df, height=38 * len(df))

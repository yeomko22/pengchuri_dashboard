import plotly.express as px
import streamlit as st

from sqls.chat_per_date import chat_per_date_sql
from sqls.dau_sql import dau_sql
from sqls.ru_sql import ru_sql

st.set_page_config(layout="wide")
conn = st.connection("mysql", type="sql")


@st.cache_resource
def get_ru_data():
    return conn.query(sql=ru_sql)


@st.cache_resource
def get_dau_data():
    return conn.query(sql=dau_sql)


@st.cache_resource
def get_chat_per_date():
    return conn.query(sql=chat_per_date_sql)


st.title("펭추리 대쉬보드")
st.markdown("""
<style>
[data-testid="block-container"] {
    padding: 3rem; 
}
</style>
""", unsafe_allow_html=True)

ru_df = get_ru_data()
chat_df = get_chat_per_date()
dau_df = get_dau_data()

cols = st.columns(6)
with cols[0]:
    st.metric(label="total users", value=ru_df["cnt"].sum())
with cols[1]:
    st.metric(label="total chat", value=chat_df["cnt"].sum())
with cols[2]:
    st.metric(label=f"today new user", value=ru_df.iloc[-1]["cnt"])
with cols[3]:
    st.metric(label=f"today chat user", value=dau_df.iloc[-1]["cnt"])
with cols[4]:
    st.metric(label=f"today chat", value=chat_df.iloc[-1]["cnt"])

col1, col2, col3 = st.columns(3)
with col1:
    with st.expander("Daily RU"):
        st.write(ru_df)
    ru_fig = px.line(ru_df, x='date', y="cnt", height=300)
    st.plotly_chart(ru_fig, use_container_width=True)
with col2:
    with st.expander("DAU"):
        st.write(dau_df)
    dau_fig = px.line(dau_df, x='date', y="cnt", height=300)
    st.plotly_chart(dau_fig, use_container_width=True)
with col3:
    with st.expander("일별 채팅 수"):
        st.write(chat_df)
    chat_fig = px.line(chat_df, x='date', y="cnt", height=300, range_y=(0, max(chat_df["cnt"])))
    st.plotly_chart(chat_fig, use_container_width=True)


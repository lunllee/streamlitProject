import streamlit as st
import pandas as pd
import os

st.title('Streamlit!!!')
col1, col2 = st.columns(2)


# 파일을 읽어서 DataFrame 으로 변환
@st.cache
def read_file(path) -> pd.core.frame.DataFrame:
    path_split = os.path.splitext(path)
    extension = {".csv": "csv"}.get(path_split[1], "unknown")
    df = pd.DataFrame()

    if extension == "csv":
        df = pd.read_csv(path)

    return df


@st.cache
def convert_csv(df):
    return df.to_csv().encode('utf-8')


def main():
    data_load_state = st.text('데이터 로드 중...')
    data = read_file('data/covid.csv')
    data_load_state.text('데이터 로드 완료!')

    data_columns = data.columns
    st.text(type(data_columns))
    st.text(type(data_columns.array))
    df_columns = pd.DataFrame(data_columns, columns=['컬럼'])
    st.text(data_columns)
    st.write(df_columns)

    with col1:
        multi_select = st.multiselect('기존 컬럼 선택',
                                      data_columns.array)

        all_options = st.checkbox("Select all options")
        if all_options:
            multi_select = data_columns.array

    with col2:
        st.text('작업할 컬럼')
        st.write(pd.DataFrame(multi_select))

    if st.checkbox('원본 데이터 보기'):
        st.subheader('covid.csv')
        st.write(data)
        to_csv = convert_csv(data)
        st.download_button(label='원본 파일 다운로드', data=to_csv, file_name='covid.csv', mime='text/csv')


if __name__ == '__main__':
    main()

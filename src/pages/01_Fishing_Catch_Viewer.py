import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_icon=":fish:", layout="wide")

np.random.seed(0)  
# JP: 魚種ごとにAmountの分布を調整するための関数を定義
# EN: Define a function to adjust the distribution of Amount for each species
def adjust_amount(species):
    if species == "Tuna":
        return np.random.choice([0, 0, 0, 1, 2, 3], size=1, p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05])[0]
    elif species == "Salmon":
        return np.random.randint(5, 16)
    elif species == "Trout":
        return np.random.randint(2, 20)
    elif species == "Mackerel":
        return np.random.randint(10, 31)
    elif species == "Sardine":
        return np.random.randint(15, 31)
    elif species == "Cod":
        return np.random.randint(0, 11)
    elif species == "Herring":
        return np.random.randint(0, 21)
    elif species == "Flounder":
        return np.random.randint(3, 18)
    elif species == "Sea Bass":
        return np.random.randint(1, 12)
    elif species == "Snapper":
        return np.random.randint(4, 22)
    else:
        return np.random.randint(0, 31)
    
date_range = pd.date_range(start="2000-01-01", end="2000-03-31")
species = [
    "Tuna", "Salmon", "Trout", "Mackerel", "Sardine",
    "Cod", "Herring", "Flounder", "Sea Bass", "Snapper"
]
# データフレームの生成
data = {
    "Date": np.repeat(date_range, len(species)),
    "Species": np.tile(species, len(date_range)),
    "Amount": np.random.randint(0, 30)
}

df = pd.DataFrame(data)
# データフレームのAmount列を更新
df['Amount'] = df['Species'].apply(adjust_amount)

# タイトル
st.title('Fishing Catch Viewer')

# ユーザー入力
start_date = st.sidebar.date_input('Start date', date_range[0])
end_date = st.sidebar.date_input('End date', date_range[-1])
selected_species = st.sidebar.multiselect('Select species', species, default=species)

# データフィルタリング
filtered_data = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date)) & (df['Species'].isin(selected_species))]

# データ集計と折れ線グラフの作成
line_fig = px.line(filtered_data.groupby(['Date', 'Species'])['Amount'].sum().reset_index(), x='Date', y='Amount', color='Species', title='Total Amount by Species Over Time')

# ヴァイオリンプロットの作成
violin_fig = px.violin(filtered_data, y='Amount', color='Species', box=True, hover_data=filtered_data.columns,
                       title='Distribution of Amount by Species')

# Create Bar Chart
# Order is Descending
bar_fig = px.bar(filtered_data.groupby('Species')['Amount'].sum().reset_index().sort_values('Amount', ascending=False), x='Species', y='Amount', title='Total Amount by Species', labels={'Amount': 'Total Amount'})

# Streamlitでグラフを表示
st.plotly_chart(line_fig, use_container_width=True)
st.plotly_chart(violin_fig, use_container_width=True)
st.plotly_chart(bar_fig, use_container_width=True)

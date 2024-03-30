import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_icon=":ship:", layout="wide")

# データと計算式の再定義
np.random.seed(0)
length = 90
dates = pd.date_range(start="2024-01-01", periods=length, freq="D") + pd.to_timedelta(np.random.choice([0, 1], size=length), unit='h')
port_names = ["Tokyo", "Osaka"]
arrival_ports = [port_names[i % 2] for i in range(length)]
departure_ports = [port_names[(i + 1) % 2] for i in range(length)]
departure_times = dates + pd.to_timedelta(np.random.choice([1, 2], size=length), unit='h')
arrival_times = dates + pd.DateOffset(days=1)
emission_factor = 3.206
oxidation_factor = 0.995
a = 1984
c = 0.489


def calculate_cii_rate(year):
    cii_rate = {'2019': 0, '2023': 5, '2024': 7, '2025': 9, '2026': 11}
    return (100 - cii_rate[str(year)]) / 100, cii_rate[str(year)]

st.title('CO2 Emission Evaluation by CII')
# Streamlitで年を選択
year = st.selectbox("CII Reduction Rate in Year", options=[2019, 2023, 2024, 2025, 2026], index=4)  # 2026年をデフォルト値とする
# CIIレートを表示
cii_rate_value, reduction_rate = calculate_cii_rate(year)
st.write(f"Reduction Rate for {year}: {reduction_rate}%")

# データフレームの生成
data = {
    "Departure Time": departure_times,
    "Departure Port": departure_ports,
    "Arrival Time": arrival_times,
    "Arrival Port": arrival_ports,
    "Duration (hours)": arrival_times - departure_times,
    "Distance (nautical miles)": np.random.uniform(320, 350, size=length).round(2),
    "Dead Weight (ton)": np.random.uniform(5000, 7000, size=length).round(2),
    "Oil Consumption (L)": np.random.uniform(15000, 18000, size=length).round(2),
}
df = pd.DataFrame(data)
df['Duration (hours)'] = df['Duration (hours)'].dt.total_seconds() / 3600
df['Speed (knots)'] = df['Distance (nautical miles)'] / df['Duration (hours)']
df['Emission (g)'] = df['Oil Consumption (L)'] * emission_factor * oxidation_factor * 1000
df['AER'] = df['Emission (g)'] / (df['Distance (nautical miles)'] * df['Dead Weight (ton)'])

# CII基準値の計算
x = np.arange(5000, 7000, 0.1)
y = a * np.power(x, -c) * calculate_cii_rate(year)[0]

# Plotlyで基準値のプロットと散布図を描画
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='CII Rate'))
fig.add_trace(go.Scatter(x=df['Dead Weight (ton)'], y=df['AER'], mode='markers', name='Ship Data'))
fig.update_layout(title='AER vs Dead Weight with CII Rate for ' + str(year),
                  xaxis_title='Dead Weight (ton)',
                  yaxis_title='Annual Efficiency Ratio (AER)',
                  legend_title="Legend")

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)

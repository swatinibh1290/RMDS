import streamlit as st
import pandas as pd
import plotly.express as px
from yahooquery import Ticker

ticker_data = pd.read_csv('./funds.csv')
#print(ticker_data['Ticker'])


metric_list = list(ticker_data['Name'].unique())

metric = st.selectbox(label = "Choose a Ticker to view holdings and sector %", options = metric_list)
#print(ticker_data[ticker_data['Name']==metric]['Ticker'])
metric_ticker = ticker_data[ticker_data['Name']==metric]['Ticker'].values[0]
#metric_ticker = ticker_data[ticker_data['Name']==metric]['Ticker']

def checkholdingandsectors(ticker):
    tickers = Ticker(ticker)
    trial1 = pd.DataFrame(tickers.fund_top_holdings)
    trial2 = pd.DataFrame(tickers.fund_sector_weightings)

    fig1 = px.bar(trial1,x='holdingName',y='holdingPercent',title='Top 10 Holdings',
    labels={
        'holdingName':'Holdings',
        'holdingPercent': 'Percentage Holdings'
    })

    fig2 = px.pie(trial2,names=trial2.index ,values=trial2[ticker])

    return fig1, fig2

checkholdingandsectors('AWPCX')

title = "Holdings and Sector"
fig1, fig2 = checkholdingandsectors(metric_ticker)
#px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric_labels[metric]}"})
st.plotly_chart(fig1, use_container_width=True)

st.plotly_chart(fig2, use_container_width=True)
import yfinance as yf
import pandas as pd


def determine_anomaly(data, threshold):
    anomaly_dict = {}
    for ticker in data.columns:
        week_result = float((data[ticker].to_frame().iloc[0])/(data[ticker].iloc[:7].mean()))
        month_result = float((data[ticker].to_frame().iloc[0])/(data[ticker].mean()))
        if week_result>threshold or month_result>threshold:
            anomaly = True
        else:
            anomaly = False
        anomaly_dict[(ticker, week_result, month_result)] = anomaly
    return anomaly_dict


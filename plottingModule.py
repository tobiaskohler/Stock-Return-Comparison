import yfinance as yf
import pandas as pd
import plotly.express as px
import numpy as np

import datetime
import os
import traceback

def plot_returns(symbols, frequency, start=None, end=None, price_type='Close'):
    
    """
    This function plots the log returns of the given symbols over the specified time frame.
    
    Parameters:
        symbols (list of str): A list of symbols to retrieve the financial data from yahoo finance.
        
        frequency (str): The frequency of data to return: 'monthly', 'quarterly', or 'yearly'.
        
        start (str, optional): The start date in the format 'YYYY-MM-DD'. Defaults to None, which is calculated as 2 years ago from the current date.
        
        end (str, optional): The end date in the format 'YYYY-MM-DD'. Defaults to None, which is calculated as the current date.
        
        price_type (str, optional): The type of price to use: 'Close', 'Open', 'High', 'Low'. Defaults to 'Close'.
    
    Returns:
        df (pd.DataFrame): A Pandas dataframe of the log returns.
        
        str: Returns an error message string in case of an exception.

    Raises:
        ValueError: If an invalid frequency is provided.
    """
    
    try:
        if start is None or end is None:
            end = datetime.datetime.today().strftime("%Y-%m-%d")
            start = (datetime.datetime.today() - pd.DateOffset(years=2)).strftime("%Y-%m-%d")
            stocks_data = {symbol: yf.Ticker(symbol).history(period='2y') for symbol in symbols}
        
        stocks_data = {symbol: yf.Ticker(symbol).history(start=start, end=end) for symbol in symbols}
        
        data = {symbol: stocks_data[symbol][price_type] for symbol in symbols}    
        
        df = pd.DataFrame(data)
        df.dropna(inplace=True)
        
        for col in df.columns:
            print(col)
            df[col] = df[col] / df[col].iloc[0] * 100
            log_returns = np.log(df) - np.log(df.shift(1))
        
        print(log_returns)
        
        if frequency == 'monthly':
            log_returns = log_returns.resample('M').sum()
        elif frequency == 'quarterly':
            log_returns = log_returns.resample('Q').sum()
        elif frequency == 'yearly':
            log_returns = log_returns.resample('Y').sum()
        else:
            raise ValueError("Invalid frequency")
        
        
        fig = px.bar(log_returns.reset_index(), x='Date', y=symbols, height=600, width=600,  labels={'x': 'Period', 'y': 'log return'}, template="plotly_white", barmode = 'group')
        fig.update_layout(yaxis_title=f'log return ({price_type} prices)', xaxis_title=f'Period ({frequency})')
        fig.update_layout(title_x=0.5, legend_title="Assets", hovermode="x unified")
        fig.show()
        
        save = input("Save graph to the current folder? (y/n)")

        if save.lower() == 'y':
            
            folder_name = "output"
            save_dir = os.path.isdir(folder_name)
            current_dir = os.getcwd()
            symbols_string = "".join([symbol.replace(",", "") for symbol in symbols])

            if not save_dir:
                os.makedirs(folder_name)
                
            fig.write_image(f"{current_dir}/{folder_name}/{symbols_string}_log-return_{frequency}_{price_type}_{start}-{end}.png")
            fig.write_html(f"{current_dir}/{folder_name}/{symbols_string}_log-return_{frequency}_{price_type}_{start}-{end}.html")
            print(f"Exports saved to {current_dir}/{folder_name}.")
            
            return df
        
    except Exception as e:
        error_msg = f"Unexpected Error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        
        return error_msg

if __name__ == '__main__':
    plot_returns(['AAPL', 'MSFT'], 'monthly', '2019-01-01', '2020-01-01', 'Close')
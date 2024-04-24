import pandas as pd

# Pandas is a data manipulation and analysis tool that is built on Numpy.
# Pandas uses a data structure known as DataFrame (think of it as Microsoft excel in Python). 
# DataFrames empower programmers to store and manipulate data in a tabular fashion (rows and columns).
# Series Vs. DataFrame? Series is considered a single column of a DataFrame.



# Let's define a two-dimensional Pandas DataFrame
# Note that you can create a pandas dataframe from a python dictionary

bank_client_df = pd.DataFrame({'Bank Client ID': [111, 222, 333, 444], 
                               'Bank Client Name': ['John', 'Eva', 'Steve', 'Sara'],
                               'Net Worth [$]':[3500, 29000, 10000, 2000],
                               'Years with bank':[3, 9, 4, 5]})

print(bank_client_df)

# Let's obtain the data type 

print(type(bank_client_df))

# you can only view the first couple of rows using .head()

print(bank_client_df.head(2))

# you can only view the last couple of rows using .tail()

print(bank_client_df.tail(2))

#MINI CHALLENGE #6: A porfolio contains a collection of securities such as stocks, bonds and ETFs. Define a dataframe named 'portfolio_df' that holds 3 different stock ticker symbols, number of shares, and price per share (feel free to choose any stocks)
#Calculate the total value of the porfolio including all stocks


portgolio_df = pd.DataFrame({'Stock ticker symbol': ['AAPL', 'AMZN', 'T'], 
                               'number of stock': [3, 4, 9],
                               'Price x share [$]':[3500, 29000, 100]})

print(portgolio_df)

stock_dollar_value = portgolio_df['Price x share [$]'] * portgolio_df['number of stock']

print(stock_dollar_value)
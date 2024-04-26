import pandas as pd

bank_client_df = pd.DataFrame({'Bank Client ID': [111, 222, 333, 444], 
                               'Bank Client Name': ['John', 'Eva', 'Steve', 'Sara'],
                               'Net Worth [$]':[3500, 29000, 10000, 2000],
                               'Years with bank':[3, 9, 4, 5]})

print(bank_client_df)

#sorting the df without changing the values in memory

bank_client_df.sort_values(by= "Years with bank")
print(bank_client_df)

#sort and change

bank_client_df.sort_values(by= "Years with bank", inplace=True)
print(bank_client_df)
import pandas as pd

#Let's define a dataframe as follow


bank_client_df = pd.DataFrame({'Bank Client ID': [111, 222, 333, 444], 
                               'Bank Client Name': ['John', 'Eva', 'Steve', 'Sara'],
                               'Net Worth [$]':[3500, 29000, 10000, 2000],
                               'Years with bank':[3, 9, 4, 5]})


print(bank_client_df)
print("\n")
# Pick certain rows that satisfy a certain criteria

df_loyal = bank_client_df[ bank_client_df['Years with bank'] >= 5]
print(df_loyal)
print("\n")

# Delete a column from a Dataframe
del bank_client_df["Bank Client ID"]
print(bank_client_df)
print("\n")

#Mini Challenge #8: using "bank_client_df" dataframe, select high networth individuals (>= 5000), what is the combined networth for all customers with 5000+?

df_high_networth_clients = bank_client_df[bank_client_df['Net Worth [$]'] >= 5000]
print(df_high_networth_clients)
print("\n")

print(df_high_networth_clients["Net Worth [$]"].sum())
import pandas as pd

bank_client_df = pd.DataFrame({'Bank Client ID': [111, 222, 333, 444], 
                               'Bank Client Name': ['John', 'Eva', 'Steve', 'Sara'],
                               'Net Worth [$]':[3500, 29000, 10000, 2000],
                               'Years with bank':[3, 9, 4, 5]})

print(bank_client_df)

#Define a function that takes a column and increase the value of 20%

def networth_update(balance):
    return balance * 1.2

bank_client_updated_df = bank_client_df['Net Worth [$]'].apply(networth_update)

print(bank_client_updated_df)

bank_client_len_df = bank_client_df["Bank Client Name"].apply(len)

print(bank_client_len_df)

#Mini Challenge 9: Define a function that triples the networth and add 200$, apply the function to the data frame and calculate the updated total networth

def triple_and_200(balance):
    return (balance * 3.0) + 200

bank_client_updated_df = bank_client_df['Net Worth [$]'].apply(triple_and_200)

print(bank_client_updated_df.sum())
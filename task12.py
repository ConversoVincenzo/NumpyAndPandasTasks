import pandas as pd

#Define a dataframe named 'Bank_df_1' that contains the names of 5 bank clients

bank_clients_names_df = pd.DataFrame({'Bank Client Name': ['John', 'Eva', 'Steve', 'Sara', 'Mark']},
                                     index=[1, 2, 3, 4, 5])

print(bank_clients_names_df)

bank_new_clients_df = pd.DataFrame({'Bank Client Name': ['John', 'Eva', 'Steve', 'Sara', 'Mark']},
                                     index=[6, 7, 8, 9, 10])

bank_clients_names_df = pd.concat([bank_clients_names_df, bank_new_clients_df])

print(bank_clients_names_df)

client_salary_df = pd.DataFrame({'Salary': [1000, 100000, 20000, 3300, 40000, 990000, 30000, 30000, 4000, 77777]},
                                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

bank_client_df = pd.concat([bank_clients_names_df, client_salary_df], axis=1)

print(bank_client_df)


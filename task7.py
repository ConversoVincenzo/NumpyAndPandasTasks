import pandas as pd

# Read tabular data

house_price_df = pd.read_html("https://www.livingin-canada.com/house-prices-canada.html")
print(house_price_df[0])
print("\n")
print(house_price_df[1])

#Mini Challenge #7: Write a code that uses Panda to read Tabular US Retirement data

retirment_data_df = pd.read_html("https://www.ssa.gov/oact/progdata/nra.html")
print(retirment_data_df[0])
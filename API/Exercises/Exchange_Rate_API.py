import requests
import pandas as pd


# TODO 1: initialize and set up our API info
API_KEY = 'enteryourapikeyhere'
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR"
header = {'apikey': API_KEY}
trial = requests.get(url, headers=header)


# TODO 2: add all data to a json to begin extraction
json_rates = trial.json()['rates']


# TODO 3: initialize a null dataframe
base_eur_rates_df = pd.DataFrame(columns=['Symbol', 'Rate'])


# TODO 4: loop through rates_json and add values to my dataframe
for country_abbr, ex_rate in json_rates.items():
    base_eur_rates_df.loc[len(base_eur_rates_df)] = [country_abbr, ex_rate]

# set the index as the Symbol
base_eur_rates_df = base_eur_rates_df.set_index('Symbol')


# TODO 5: output this as an accessible CSV
base_eur_rates_df.to_csv('data_output/euro_base_exchange_rates.csv')

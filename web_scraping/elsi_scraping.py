import csv
from matplotlib.pyplot import axis
import pandas as pd
import district_users as du
import twitter_scraping as ts


elsi_data = pd.read_csv('../data/ELSI_locale_data.csv')
N = 25
# clean data

def clean_data(input_df):
    data = input_df.copy()
    # extract only locale
    data['Locale'] = data['Locale'].str.extract("(?:\d*-)(\w*)(?:: \w*)")
    # # make district name lowercase
    # data['Agency Name'] = data['Agency Name'].str.lower()
    data = data.dropna()
    locale_data = data.groupby(by='Locale').count().rename({'Agency Name':'Num Districts'}, axis=1)[['Num Districts']]
    print(f"found {len(data)} districts with the following locale breakdown: \n \n {locale_data}")
    return data

def gen_random_sample(input_df):
    locale_list = input_df['Locale'].unique()
    out = pd.DataFrame()
    for locale in locale_list:
        sample_df = input_df[input_df['Locale']==locale].sample(N)
        out = pd.concat([out, sample_df])
    print(out)
    return out
        
    

def main():
    cleaned_elsi = clean_data(elsi_data)
    rand_sample = gen_random_sample(cleaned_elsi)
    # save sample to csv
    # rand_sample.to_csv('../data/elsi_locale_sample.csv')
    
if __name__ == '__main__':
    main()
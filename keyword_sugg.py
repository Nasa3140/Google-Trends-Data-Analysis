# python code for to analysis google trends data for daily search using country
# for keyword with keyword suggestion

import pandas as pd
from pytrends.request import TrendReq

# Set up the Pytrends client
pytrends = TrendReq(hl='en-US', tz=360)

# Define the keyword and country
keyword = 'Python'
country = 'IN'

# Build the payload for the daily search trend data
pytrends.build_payload(kw_list=[keyword], geo=country, timeframe='today 1-m', gprop='')

# Extract the daily search trend data as a Pandas DataFrame
df = pytrends.interest_over_time()

# Extract the related queries/suggestions as a dictionary of Pandas DataFrames
related_queries_dict = pytrends.related_queries()

# Print the first 5 rows of the DataFrame
print(df.head())

# Print the top 5 rising related queries/suggestions
print('\nTop 5 Rising Related Queries:')
print(related_queries_dict[keyword]['rising'].head())

# Print the top 5 top related queries/suggestions
print('\nTop 5 Top Related Queries:')
print(related_queries_dict[keyword]['top'].head())
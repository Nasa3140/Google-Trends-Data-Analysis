# Get the google trends scraper connection
from pytrends.request import TrendReq
import pandas as pd

# Add my parameters
trend = TrendReq(hl='en-US', tz=360)

# Function to get trending searches accross countries
countries=['india', 'united_states']
def trending_searches(country):
    data= trend.trending_searches(country)
    print(data.head(5))

for country in countries:
    print(country)
    trending_searches(country)
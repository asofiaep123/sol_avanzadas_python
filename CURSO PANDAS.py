# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 19:42:38 2023

@author: Sofía
"""

import pandas as pd


pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])


# =============================================================================
# PARTE 1:
# =============================================================================


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

fruit_sales = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},index=["2017 Sales","2018 Sales"])


ingredients = pd.Series(["4 cups","1 cup","2 large","1 can"],index=["Flour","Milk","Eggs","Spam"],name="Dinner")


reviews = pd.read_csv("WINE/winemag-data_first150k.csv",index_col=0)


animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])


# =============================================================================
# PARTE 2
# =============================================================================


desc = reviews.description

first_description = desc[0]
first_row =reviews.iloc[0]
first_descriptions = desc[:10]
sample_reviews = reviews.iloc[[1,2,3,5,8],:]
df = reviews.loc[[0,1,10,100],["country","province","region_1","region_2"]]
df = reviews.loc[:99,["country","variety"]]
italian_wines = reviews[reviews.country=="Italy"]


paises=reviews[(reviews.country=="Australia")+(reviews.country=="New Zealand")]
top_oceania_wines = paises[paises.points>=95]


# =============================================================================
# PARTE 3
# =============================================================================

reviews.taster_name.describe()
reviews.taster_name.describe()

median_points = reviews.points.median()

countries = reviews.country.unique()

reviews_per_country = reviews.country.value_counts()

prom=reviews.price.mean()
centered_price = reviews.price - prom

m = (reviews.points/reviews.price).idxmax()
bargain_wine = reviews.title[m]

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

(reviews.description=="tropical").count()
reviews.description.map(lambda desc: "tropical" in desc).sum()

vinos=reviews[reviews.country=="Canada"]
star_3 = (reviews.points>=95)*3
star_2 = (reviews.points>=80)*2
star_1 = (reviews.points<80)*1
star_ratings = star_3+star_2+star_1


# =============================================================================
# PARTE 4
# =============================================================================

reviews_written = reviews.groupby("taster_twitter_handle").size()

best_rating_per_price = reviews.groupby("price")["points"].max().sort_index()

price_extremes = reviews.groupby('variety').price.agg([min,max])

sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)


# =============================================================================
# PARTE 5
# =============================================================================

dtype = reviews.points.dtype

point_strings = reviews.points.astype(str)

n_missing_prices = pd.isnull(reviews.price).sum()

reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)


# =============================================================================
#   PARTE 6 
# =============================================================================

renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

reindexed = reviews.rename_axis("wines", axis='rows')

combined_products = pd.concat([gaming_products, movie_products])

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))


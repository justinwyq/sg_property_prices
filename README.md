# Singapore Property Prices

This project aims to build a regression model to predict property prices in Singapore.

## Current Status
Regression model has been built and is being refined for HDB resale prices using the HDB resale price data available at data.gov.sg here: https://data.gov.sg/dataset/resale-flat-prices. The current model achieves an R-squared of 0.89 in predicting resale flat prices.

Some features that have been engineered, with the help of Geocoding and Google's distance matrix APIs, include:
1. Distance to nearest MRT/LRT station
2. Distance to shopping malls
3. Travel time from nearest station to CBD

A web-scraping bot implemented in scrapy has also been built to scrape listing data from 99co. 

Initial model accuracy for the HDB data from 99co is low, at an R-squared of 0.47. However, this may be because 99co reflects the listed price and not the actual resale price.

## Work in progress
1. Refine model for 99co listings
2. Built an automated tool to detect under-priced 99co listings and send alert via email

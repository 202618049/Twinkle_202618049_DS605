# Twinkle_202618049_DS605
DS605 Fundamentals of Machine Learning

Name: Twinkle Chauhan

Student ID: 202618049

Assignment:01 
Date: 06,August'2026

# Project Overview
This repository contains the complete end-to-end data pipeline for extracting, cleaning, visualizing, and analyzing book data from `books.toscrape.com`.

Repository Contents

books_raw.csv: Raw dataset extracted via web scraping.
books_cleaned.csv: Processed dataset with converted numeric columns (price_numeric, rating_num) and engineered features (value_score).
price_distribution.png: Histogram showing price distribution across books.
rating_distribution.png: Bar chart showing book counts per star rating (1 to 5).
average_price_by_category.png: Horizontal bar chart comparing average prices by book category.
price_vs_rating.png: Scatter plot analyzing the relationship between price and rating.
wordcloud.png: Word cloud generated from combined book descriptions.

Data Pipeline Summary

Extraction (Scrapy / Web Scraping): Scraped title, price, rating, category, stock availability, and descriptions across multiple pages.
Preprocessing (Pandas): Cleaned currency symbols from price data, converted textual ratings to numeric values (1 to 5), handled missing values, and created a value_score feature (Rating / Price).
Visualization (Matplotlib / WordCloud): Generated four key exploratory charts and a description-based word cloud.

Key Findings and Insights

Price vs. Rating Relationship
Price is not related to star ratings. High-rated 5-star books are present at both cheap (15 pounds) and expensive (50+ pounds) price points.

Category Analysis

Most Represented Categories: Travel and Sequential Art (highest total volume of listed books).
Most Expensive Categories: Travel and Science Fiction (highest average price per book).

Best Value Books
Books with 5-star ratings priced under 20 pounds provide the highest value for money based on the value_score metric.

Dataset Limitations

Sample Size: Limited to 100 books scraped across 5 pages.
No Customer Reviews: Summary descriptions were used for textual analysis as the website lacks written customer reviews.
Static Snapshot: Data represents a single point in time and does not capture dynamic price or inventory changes.

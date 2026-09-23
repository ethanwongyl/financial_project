## Introduction

This project is a self-motivated project on stock market prices to demonstrate data analysis skills of the applicant while expanding knowledge of the financial market. The goal of the project is not only to build a pipeline for the stocks, but also to investigate how real market events affect the market, and individual stock prices. SQL and Python are heavily applied to the data analysis aspect of the project for data analysis and pipeline development.

The historical data of three stocks - HSBC (0005.HK), Tencent (0700.HK), and HKEX (0388.HK) over the past ~6.5 years (2020-2026) are studied alongside the data of Hang Seng Index (HSI). The OHLCV data of these four instruments are then put through a full analytical pipeline, which includes ingestion, cleaning, relational storage, and SQL-driven data analysis. In addition to understanding what each quantifiable figure represents during data analysis, the results are also compared to the real market events, where the fluctuations can be interpreted as a result of these events.

---

## Tech Stack

| Layer | Tools |
| --- | --- |
| Data Ingestion | `yfinance` |
| Data Wrangling | `pandas` |
| Relational Storage | `PostgreSQL` via `SQLAlchemy` |
| Database Engine | `DuckDB` connected to `PostgreSQL` |
| Visualisation | `matplotlib` |

---

## Pipeline

1. **Data Extraction** - using `yfinance` library, daily OHLCV data between 01-01-2020 to 28-08-2026 of all four tickers are pulled from Yahoo Finance.
2. **Data Cleaning** - the raw data retrieved contains artifacts that are cleaned and corrected. These include incorrect column names, two blank rows, and uppercased column names that cannot be easily read in `PostgreSQL`.
3. **Data Storage** - cleaned data is loaded into `PostgreSQL` vis `SQLAlchemy`.
4. **Data Analysis** - by attaching `DuckDB` to `PostgreSQL`, the analytical commands in SQL are executed in the database engine, which will be further explained in the following section.

---

## Analytical Methodology

When is pipeline in SQL is built, one of the key principle is that the pipeline can be safely re-run when new data is looked at. Therefore, each query creates a new table by `CREATE OR REPLACE VIEW` to avoid name clashes.

This section explains the analytical processes of this project with the window functions used in SQL to investigate the aforementioned datasets.

__Daily returns__

The percentage change between the closing prices of a particular day and the previous day. The `LAG()` function is used to access the closing price of the previous day. This forms the basis of everything that we use in this project. Firstly, the stock prices between different stocks are not comparable, and therefore daily returns are used to normalise the comparison between different stocks. Furthermore, statistical analysis of the time series of stocks assumes stationarity of the data. As the raw price of a stock may increase or decrease over time, it cannot be used in such an analysis. Instead, the daily return of a stock is formulated to allow the time series techniques to be mentioned to work.

__Volatility__

By calculating the sample standard deviation `STDDEV_SAMP()` over a 20-day rolling window, the volatilities of the stocks are returned. The volatility of a stock tells us how fluctuated a stock is to its mean return. The volatilities are also annualised with a multiplier of √252, the generalised number of trading days in a stock market. One point to note here is that a sample standard deviation is used instead of the population standard deviation as we formulate the rolling volatility within a small moving period (20 days), which result in a ~2.6% difference in calculation.

The most volatile periods of these stocks are identified, then compared to market events in the past to find how these events affected the stock market.

__Moving Averages__

The `AVG()` window function in SQL allows us to compute the moving average of a stock price. In this project, the 50-day and 200-day moving averages are both calculated. One caveat when formulating the moving averages is that the reliable averages start only on the 50th and 200th day respectively, since the averages before that do not have sufficient data points. Therefore, a `ROW_NUMBER()` filter is used together with `WHERE rn>=50` to purposefully remove misleading data points, which will also be explained in __Cross Detection__. The same technique is used in volatility for the first 20 days of the dataset, but has a significantly smaller effect on the results.

__Cross Detection__

__Correlation__

__Beta__

---

## Results

1. volatile period
2. Moving averages and Cross detection

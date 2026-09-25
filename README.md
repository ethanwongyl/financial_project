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

The `AVG()` window function in SQL allows us to compute the moving average of a stock price. In this project, the 50-day and 200-day moving averages are both calculated. One caveat when formulating the moving averages is that the reliable averages start only on the 50th and 200th day respectively, since the averages before that do not have sufficient data points to return a correct 50-/200-day average. Therefore, a `ROW_NUMBER()` filter is used together with `WHERE rn>=50` to purposefully remove misleading data points, which will also be explained in __Cross Detection__. The same technique is used in volatility for the first 20 days of the dataset, but has a significantly smaller effect on the results.

__Cross Detection__

The 'Golden Cross' is detected when the 50-day average surpass the 200-day average, and 'Death Cross' vice versa. The function `LAG()` has been used to compare the two averages on two consecutive days. As mentioned in the __Moving Average__ section, the unreliable averages could result in a false detection. The filter that was used when formulating the moving averages successfully masked one false 'Death Cross' signal in March 2020 out. The stock price, 50-day average, 200-day moving average, and the cross detections are also plotted on a graph.

__Correlation__

The correlation between different prices shows how these prices move with one another. All four tickers are compared in a loop of `CORR()` window function to create a correlation table. A correlation between two stocks ranges from -1 (exact opposite direction) to +1 (exact same movement), and we can compare the correlation between different stocks and the Hang Seng Index to investigate the characteristics of different stocks.

__Beta__

The beta $$\beta$$ is often compared between a stock and the corresponding stock market index, and it reflects how much a fluctuation in the stock market is amplified in a particular stock price. It is calculated using the covariance between the stock returns and the market return, divided by the variance of the market return. At $\beta > 1$, the stock price amplifies a market fluctuation; at $\beta = 1$, the stock price moves in line with the market; at $0 < \beta < 1$, the stock is more defensive and moves less than a market fluctuation; when $\beta$ is negative, a stock moves opposite to the direction of the market fluctuation. 

In this project, the beta between all three stocks are compared with the Hang Seng Index. The results can tell us the systematic risk of a stock has, which comes from the fluctuation of the market itself, after excluding all the risks independent to individual companies. 

__Rolling Correlation and Rolling Beta__

The rolling correlation and beta with a 60-day window is also calculated to compare how different stocks performed against the HSI over the 6.5-year period. They are plotted side-to-side with the market level and the average attained from the previous sub-sections. A window of 60 days is used to ensure that the correlation, covariance, and variance have sufficient data to be taken into account; and that the time period is also short enough so that it would not smoothen out the fluctuations of the market.

---

## Results

1. volatile period
2. Moving averages and Cross detection

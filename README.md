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

The percentage change between the closing prices of a particular day and the previous day. The `LAG()` function is used to access the closing price of the previous day. This forms the basis of everything that we use in this project, as (why)

__Volatility__

__Moving Averages__

__Cross Detection__

__Correlation__

__Beta__

This project is a self-motivated project on stock market prices to demonstrate data analysis skills of the applicant while expanding knowledge of the financial market. The goal of the project is not only to build a pipeline for the stocks, but also to investigate how real market events affect the market, and individual stock prices. SQL and Python are heavily applied to the data analysis aspect of the project for data analysis and pipeline development.

The historical data of three stocks - HSBC (0005.HK), Tencent (0700.HK), and HKEX (0388.HK) over the past ~6.5 years (2020-2026) are studied alongside the data of Hang Seng Index (HSI). The OHLCV data of these four instruments are then put through a full analytical pipeline, which includes ingestion, cleaning, relational storage, and SQL-driven data analysis. In addition to understanding what each quantifiable figure represents during data analysis, the results are also compared to the real market events, where the fluctuations can be interpreted as a result of these events.

## Tech Stack

| Layer | Tools |
| --- | --- |
| Data Ingestion | `yfinance` |
| Data Wrangling | `pandas` |
| Relational Storage | `PostgreSQL` via `SQLAlchemy` |
| Database Engine | `DuckDB` connected to `PostgreSQL` |
| Visualisation | `matplotlib` |


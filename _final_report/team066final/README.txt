DESCRIPTION:

This software package contains source code for getting started with an Enhanced Chilean Mutual Fund Data Explorer. Our technology stack is Python 3 on top of Jupyter Notebooks, and Tableau.

This project has 4 main parts:

Step 1 Data Scraping – First we scrape publicly available mutual fund data from aafm.cl. We then store this in a raw format for further processing. This step is purely about data collection.

Step 2 Data Splitting and Compression – We take the raw data collected in a step one, split it into constituent parts, then store it in an optimized way using Parquet. This enables us to have a compressed data source that is easier to process in subsequent steps.

Step 3 Clean and Transformation – We take the previously split and compressed data, clean it as appropriate, and merge parts of it together, and perform other processes such as dimensionality reduction to enable better consumption during machine learning.

Step 4 Analysis/Machine Learning – This is the last processing step but is by far the largest. We take our recently cleaned data and run it through several machine learning algorithms such as t-SNE, K-means for clustering, anomaly detection, calculating efficiency frontiers, etc.

Step 5 Visualization – Using Tableau, we enable users to quickly view funds and glean their own observations. Our workbook contains four primary dashboards.

	1) Chilean Mutual Funds Anomaly Detection: This dashboard enables investors to quickly view a self-organized map of the available funds, observe outliers and fund misclassifications, and compare funds to their proper classifications.

	2) AAFM Category Fund Summary: This is the destination dashboard from the bar filter above. It is a table that shows the funds that are in the selected AAFM category, whether the fund is marked as an anomaly or not, average annual return, and average annual risk of each fund.

	3) Similar Chilean Mutual Funds: This dashboard enables users to view funds that have been classified as similar to a selected fund from a table. Fund similarity is designated solely as whether funds fall into the same AAFM Category.

	4) Modern Portfolio Theory (MPT): This dashboard is used to display the Modern Portfolio Theory options for AAFM categories and K-means clustering categories. Users are able to quickly visualize how different portfolio options compare to each other, and they are colored on a user-entered Sharpe ratio (a financial performance metric).


INSTALLATION:
Our technology stack is Python 3 on top of Jupyter Notebooks, and Tableau.
To get started install Python 3, Jupyter Notebooks or VS Code, and Tableau for your operating system.
Python installers can be found at https://www.python.org/downloads/.
Jupyter Notebooks or VS Code Notebooks can be found at https://jupyter.org/install and https://code.visualstudio.com/docs/python/jupyter-support respectively.
Tableau can be found at https://www.tableau.com/products/desktop/download. Tableau is a paid for product, but they do provide educational discounts, etc., as well as free 2-week trial.

EXECUTION:
From directory of the unzipped project, run "python install CODE" from a terminal. This will install required Python dependencies, create an aafm_work directory in the user's home directory, and a few other installation requirements.
Once installation has been completed, navigate to your user's home directory, on the aafm_work directory, and start the main.ipynb Python notebook.
main.ipynb is a condensed aggregate of our entire process (if you're interested in seeing more of our code open the dva package), which scrapes data from the web, extracts/transforms/stores our data as several CSV files, preparing the data from consumption from Tableau.
Once you've run main.ipynb you can open the Tableau dashboard Chilean_fundsdashboard.twbx, found in the same directory as main.ipynb.
For a quick overview of the Tableau dashboard, visit the YouTube video below.

DEMO VIDEO: 
https://www.youtube.com/watch?v=eKTFBlOoYdo
DESCRIPTION:

This software package contains source code for getting started with an Enhanced Chilean Mutual Fund Data Explorer. It makes use of Python Notebooks to scrape, transform, and analyze. The data is then handed off to a Tableau Workbook for visualization.



ASSUMPTIONS:

* You know about python notebooks and have a compatible notebook environment installed.
* You know about Tableau and have a recent version installed.



INSTALLATION:

TODO: Cover Scraping
we extracted the data from aafm api using the simple request script in python and generated the raw excel files. we used these excel files as our source of data and started our analysis.

TODO: Cover ETL
For the ETL, we started by reading the source data files and generating the parquet files for each source. In the process of generating the files we did some basic data cleaning.Then we loaded the required parquet files into SQL DB and then tried analysing the data and created detailed funds summary data  by joining the funds data with the yearly returns details.

TODO: Cover Analysis/Export
As a next step into our analysis we have used the above data and applied the machine learning algorithms.we hypothesized Autoencoders and Principle Component Analysis would yield good results for finding outliers in mutual fund classification but it didn't worked out in our case due to the size of our data.Initially we started with ~4,000,000 records and have cleaned and transformed it down to 312 records, so we decided to use t-SNE for the dimesnionality reduction and self organizing. then we have used the K-Means clustering to determine the number od clusters based on the average annual return and average annual risk.


EXECUTION:

TODO: Cover running the software in Tableu
we used tableau as a viaualization tool for our project.This helps the users to quickly view the fundsand their return and risk. They can view the similarity between the funds and classification of the funds using the kmeans algorithm we have created 4 dashboards to visualize the possible interactions.
1.	Chilean Mutual Funds Anomaly Detection 
2.	AAFM Category Fund Summary 
3.	Similar Chilean Mutual Funds 
4.	Modern Portfolio Theory (MPT) 

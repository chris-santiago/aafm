DESCRIPTION:

This software package contains source code for getting started with an Enhanced Chilean Mutual Fund Data Explorer. we have used Python, SQL and Tableau.This project has 4 main parts-

Step 1 Data Scraping -First step is the source data extraction.Data can be extracted from aafm api using the simple request script in python using a jupyter notebook ffmm_funciones. This will produce multiple excel files related to the funds, their returns, categories and risks.

Step 2 ETL- ETL covers loading of the source raw data, cleaning and analysing the required data and finally generating a cleaned data set by joining multiple files

Step 3 Applying Machine learning Algorithm -As a next step into the analysis, several machine algorithms needs like PCA,Autoencoder,t-SNE, K-means clustering to be applied on the dataset.

Step 4 Visualization -This helps the users to quickly view the fundsand their return and risk. They can view the similarity between the funds and classification of the funds using the kmeans algorithm we have created 4 dashboards to visualize the possible interactions.
a.Chilean Mutual Funds Anomaly Detection : This dashboard enables investors to quickly view a self-organized map of the available funds, observe outliers and fund misclassifications, and compare funds to their proper classifications.
b.AAFM Category Fund Summary: This is the destination dashboard from the bar filter above. It is a table that shows the funds that are in the selected AAFM category, whether the fund is marked as an anomaly or not, average annual return, and average annual risk of each fund.
c.Similar Chilean Mutual Funds: This dashboard enables users to view funds that have been classified as similar to a selected fund from a table. Fund similarity is designated solely as whether funds fall into the same AAFM Category.
d.Modern Portfolio Theory (MPT) : This dashboard is used to display the Modern Portfolio Theory options for AAFM categories and K-means clustering categories. Users are able to quickly visualize how different portfolio options compare to each other, and they are colored on a user-entered Sharpe ratio (a financial performance metric).



INSTALLATION:

You need to have python installed in your machine and tools like visual studio code, Jupyter lab to run these note books using python.
You need to have tableau installed in your system in order to view the visualizations. you can get a trial version free for 2 weeks if you don't have the tableau software installed already.
you need to have DB Browser for SQLlite to host the data. 



EXECUTION:


Run pip install in the CODE directly. This will install a code package and also create a folder, aafm_work in the user's home directory.In this folder they will find the main.ipynb file which will run our entire workflow, from pulling data from web to creating final CSV files for tableau consumption.  It will also install a copy of the tabluea dashboard in the aafm_work folder.

DEMO VIDEO: 

https://www.youtube.com/watch?v=eKTFBlOoYdo

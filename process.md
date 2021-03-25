# Notes

## Notebook Flow

Extract -> Cleaned_Explore -> Raw_Explore -> Raw_Clean -> Monthly_Returns -> PCA/ISOMAP/MDS/t-SNE_Viz -> PCA_and_Distance_Detect

## Data Extraction

- Original dataset: 1.6GB
- Used Dask to parallelize extraction operations
- Extracted files:
	- Time series of prices for all mutual funds and series, 2015-01 through 2021-01 (5.9 million rows)
	- Descriptive data for all mutula funds and series (6,400 rows)
	- Time series of fund flows (inflow and outflow) for all mutual funds and series, 2015-01 through 2021-01 (5.9 million rows)

## Data Transformation

- Joined descriptive fund data with price time series and select columns from fund flows
- Resample daily price data to monthly price data
- Remove funds that don't exist in most recent period
- Remove funds that don't have at least 36 months of data
- Remove funds that have constant price over time
- Within each fund, select series with longest price history
- Transform fund prices to monthly percent returns
- Fill missing values with respective `aafmCategory` means, by month
- Annualize monthly prices to compound annual growth and annual standard deviation metrics
	- Join with main dataset

## Mapping to Lower Dimensionality and Anomaly Detection

- Test MDS, IsoMap, and t-SNE dimensionality reduction techniques.
	- Try within-group mappings
	- Try aggregate mappings
	- Within-group mappings did not lead clearly visualize normal observations vs anomalies
	- MDS, and IsoMap did not clearly separate groups nor closely cluster similar observations
	- Choose t-SNE and aggregate mappings
- Use t-SNE to map monthly returns (73 dimensions) to X and Y coordinates (2 dimensions)
- Try PCA and Autoencoder to detect anomalies via reconstruction error; within-group sample size too small for meaningful results.
- Try defining anomalies based on t-SNE coordinates and distance from `aafmCategory` means
- Choose distance measure over PCA and Autoencoder
- Plot observations using t-SNE mapping
	- Size bubbles by assets under management (`netPatrimony`)
	- Color bubbles by `aafmCategory`
	- Flag anomalies with marker overlay
	- Include `fundName`, `aafmCategory`, `netPatrimony`, `ann_return`, `ann_stdev` and `dist_anomaly` in tooltip

## New References

van der Maaten, L. & Hinton, G. (2008). *Visiualizing data using t-SNE*. Journal of Machine Learning Research, 9(Nov):2579-2605.
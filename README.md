# Time series forecasting


## Summary Statistics of the Datasets:

- Checked summary statistics (mean, median, min, max, etc.) for each dataset.
  
##  Checking for Missing Values in The Datasets:

- Examined missing values in each dataset and addressed missing values in the oil dataset using a backward-fill strategy.

##  Completeness of the 'date' column in the Train Dataset:

- Confirmed completeness of the 'date' column in the train dataset.

## Merging The Train Dataset with Other Datasets:

- Merged the train dataset with stores, transactions, holiday events, and oil datasets based on common columns.

# Exploratory Data Analysis (EDA):

- Conducted univariate, bivariate, and multivariate analyses.
- Explored distributions, trends, correlations, and relationships between variables.
- Visualized sales trends over time, oil price trends over time, sales by store type, city, and state, relationships between sales and transactions, and total sales by product family.
  
## Correlation Matrix:

### Interpretation of Correlation Values:

- The correlation matrix contains values ranging from -1 to 1, where:
  - -1 represents a perfect negative correlation,
  - 1 represents a perfect positive correlation, and
  - 0 represents no correlation.

### Correlation Analysis:

- 'sales' and 'transactions': Weak positive correlation, indicating that as transactions increase, sales tend to increase as well.
- 'sales' and 'dcoilwtico': Weak negative correlation, suggesting that as oil prices increase, sales tend to decrease, although the correlation is not significant.
- 'transactions' and 'dcoilwtico': Even weaker negative correlation compared to 'sales' and 'dcoilwtico', indicating no clear relationship between the two variables.

# Stationarity Test:

## Augmented Dickey-Fuller (ADF) Test:

- Null hypothesis: The data has a unit root, meaning it's not stationary.
- Alternative hypothesis: The data is stationary or trend-stationary.
- Conclusion: Based on the very low p-value and test statistics significantly lower than critical values, the data is stationary.

# Promotions Affect on Sales:

## Hypothesis Testing:

- Null Hypothesis: Promotional activities have no significant impact on store sales.
- Alternative Hypothesis: Promotional activities have a significant impact on store sales.
- Conclusion: Reject the null hypothesis, indicating that promotional activities have a significant impact on store sales.

# Other Analyses:

## Day, Month, and Year Effects on Sales:

- Analyzed sales variations by day of the week, month, and year, revealing patterns such as higher sales during certain months and lower sales during others.

## Holiday Effect on Sales:

- Explored the impact of holidays on sales through box plots, indicating variations in sales during holidays compared to non-holidays.

## Lowest and Highest Sales Each Year:

- Identified the dates with the lowest and highest sales for each year.

## Sales by Store Cluster:

- Examined average sales by store cluster, highlighting clusters with the highest number of stores.

## Promotions, Oil Prices, and Holidays Affect on Sales:

- Calculated correlations between sales and promotions, oil prices, and holidays, indicating a moderate positive correlation between sales and promotions, a weak negative correlation between sales and oil prices, and a very weak negative correlation between sales and holidays.

# Feature Engineering:

- **Time Lag Features:** Incorporate lagged versions of the target variable 'sales' to capture the temporal dependencies in the data.
- **Seasonal Features:** Introduce features such as month, day of the week, and holiday indicators to capture seasonal variations and special events that may influence sales patterns.
- **External Variables:** Include external variables such as promotions, oil prices, and holidays to capture their impact on sales.

# Model Selection:

- **Baseline Models:** Start with simple baseline models such as linear regression, seasonal decomposition models (e.g., SARIMA), or exponential smoothing methods (e.g., Holt-Winters) to establish a benchmark for model performance.
- **Advanced Time Series Models:** Explore more sophisticated time series models such as ARIMA, SARIMA, or seasonal ARIMA, which can capture complex patterns and seasonality in the data.
- **Machine Learning Models:** Experiment with machine learning algorithms such as Random Forests, Gradient Boosting Machines (GBM), or Long Short-Term Memory (LSTM) networks to capture nonlinear relationships and interactions between features.
- **Ensemble Methods:** Combine the predictions of multiple models using ensemble methods such as stacking or blending to improve overall performance and robustness.

# Model Evaluation:

- **Cross-Validation:** Use time series cross-validation techniques such as rolling origin or expanding window validation to evaluate the models' performance on unseen data while preserving temporal dependencies.
- **Evaluation Metrics:** Consider metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) to assess the models' accuracy and predictive performance.
- **Visual Inspection:** Visualize the predicted sales against the actual sales to identify any discrepancies or patterns that the models may have missed.
- **Business Impact:** Evaluate the models' performance based on their business impact, such as their ability to accurately forecast sales and inform decision-making processes related to inventory management, staffing, and marketing strategies.

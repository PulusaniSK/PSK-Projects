#Which companies beat Nifty 50 in 10 years and analysis about the stock market in India

#SQL Code for Data Extraction and Preprocessing**:

#Extract historical data for Nifty 50 stocks
SELECT 
    stock_code, 
    stock_name, 
    date, 
    open_price, 
    close_price, 
    volume
FROM stock_data
WHERE stock_code IN (SELECT stock_code FROM nifty_50);

-- #Clean and preprocess the data
SELECT 
    stock_code,
    stock_name,
    date,
    open_price,
    close_price,
    (close_price - open_price) / open_price AS daily_return,
    volume
FROM stock_data_cleaned
```

**Python Code for Performance Analysis and Visualization**:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the preprocessed data
stock_data = pd.read_csv('stock_data_cleaned.csv')

# Calculate the 10-year total return for each stock
stock_data['cumulative_return'] = (1 + stock_data['daily_return']).cumprod()
stock_returns = stock_data.groupby('stock_code')['cumulative_return'].iloc[-1]

# Identify the companies that beat the Nifty 50 index
nifty_50_return = stock_returns['NIFTY_50']
beating_nifty_50 = stock_returns[stock_returns > nifty_50_return]

# Visualize the results
plt.figure(figsize=(12, 6))
beating_nifty_50.sort_values().plot(kind='barh')
plt.title('Companies that Beat the Nifty 50 Index in 10 Years')
plt.xlabel('Total Return')
plt.ylabel('Stock Code')
plt.show()
```


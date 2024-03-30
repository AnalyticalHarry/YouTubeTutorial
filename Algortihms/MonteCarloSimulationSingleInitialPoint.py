import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# download NVDA data
nvda_data = yf.download('NVDA', period='5y')

# daily returns
nvda_data['Daily Return'] = nvda_data['Adj Close'].pct_change()

# number of simulations and trading days
n_simulations = 2000
n_days = 30

# last closing price and the daily return average and standard deviation
last_price = nvda_data['Adj Close'].iloc[-1]  # Changed to .iloc[-1]
mean_daily_return = nvda_data['Daily Return'].mean()
std_dev_daily_return = nvda_data['Daily Return'].std()

# all price series
all_price_series = []

# generate simulations
for x in range(n_simulations):
    daily_volatility = np.random.normal(mean_daily_return, std_dev_daily_return, n_days)
    price_series = [last_price]  # Start with the last closing price
    for y in daily_volatility:
        price = price_series[-1] * (1 + y)
        price_series.append(price)
    all_price_series.append(price_series)

# list of price series
simulation_df = pd.DataFrame(all_price_series).transpose()

plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(simulation_df.columns)))
for column, color in zip(simulation_df.columns, colors):
    plt.plot(simulation_df[column], color=color, alpha=0.9)
plt.axhline(y=last_price, color='r', linestyle='-', linewidth=2, label='Last Closing Price')
plt.title('Monte Carlo Simulation for NVIDIA Stock', fontsize=14)
plt.xlabel('Day', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
plt.legend()
plt.show()

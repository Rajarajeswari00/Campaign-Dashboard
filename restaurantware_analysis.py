# Section 5

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('Data for the Assessment.csv')

# Clean the data
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])

# Calculate metrics
data['ACoS'] = data['Ad Spend'] / data['Sales']  # 
data['CTR'] = data['Clicks'] / data['Impressions']     
data['Net Margin Percent'] = (data['Sales'] - data['Cost'] - data['Ad Spend']) / data['Sales']

# Top 5 best-selling products by total sales
top_5_products = data.groupby('ASIN')['Sales'].sum().sort_values(ascending=False).head(5).index.tolist()

# Scatterplot: Sales vs Advertising Spend
plt.figure(figsize=(10,6))
sns.scatterplot(x='Ad Spend', y='Sales', data=data)
plt.title('Sales vs Advertising Spend')
plt.savefig('sales_vs_advertising_spend.png')
plt.show()

# Bar chart: Average Net Margin % by Campaign
campaign_margin_avg = data.groupby('Campaign')['Net Margin Percent'].mean().sort_values()
plt.figure(figsize=(10,6))
campaign_margin_avg.plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('Average Net Margin Percentage by Campaign')
plt.xlabel('Campaign')
plt.ylabel('Net Margin Percent')
plt.xticks(rotation=30, ha='right')
plt.axhline(0, color='gray', linewidth=1)  
plt.tight_layout()
plt.savefig('net_margin_percent_by_campaign_bar.png')
plt.show()

# Bonus: Find top 5 products by sales within each campaign and save as CSV
top5_campaign = data.groupby(['Campaign', 'ASIN'])['Sales'].sum().reset_index()
top5_campaign = top5_campaign.sort_values(['Campaign', 'Sales'], ascending=[True, False])
top5_campaign = top5_campaign.groupby('Campaign').head(5)
top5_campaign.to_csv('top5_campaign.csv', index=False)
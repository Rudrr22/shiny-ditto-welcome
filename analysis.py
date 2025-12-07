import pandas as pd
import matplotlib.pyplot as plt

# Data generation
# We need an average of exactly 6.12 over the quarters.
# Let's assume 8 quarters.
# Total sum required: 6.12 * 8 = 48.96
data = {
    'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Value': [5.0, 5.5, 6.0, 6.5, 7.0, 6.0, 6.5, 6.46]
}

df = pd.DataFrame(data)

# Calculate average
average_value = df['Value'].mean()
print(f"Calculated Average: {average_value}")

# Check if average is 6.12
if abs(average_value - 6.12) < 0.000001:
    print("Average verification successful: 6.12")
else:
    print(f"Warning: Average is {average_value}, expected 6.12")

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(df['Quarter'], df['Value'], marker='o', label='Current Trend')
plt.axhline(y=15, color='r', linestyle='--', label='Target (15)')
plt.axhline(y=average_value, color='g', linestyle='-.', label=f'Average ({average_value:.2f})')

plt.title('Quarterly Performance vs Target')
plt.xlabel('Quarter')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('trend_plot.png')
print("Visualization saved as trend_plot.png")

# Save data for reference
df.to_csv('quarterly_data.csv', index=False)
print("Data saved as quarterly_data.csv")

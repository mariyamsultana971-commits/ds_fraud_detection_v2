import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data - make sure the CSV name matches exactly
df = pd.read_csv('Fraud_Analysis_Dataset.csv')

# Show the first 5 rows to make sure it loaded correctly
print("Data Preview:")
display(df.head())

# Check the distribution of Fraud (1) vs Genuine (0)
print("\nTransaction Counts:")
print(df['isFraud'].value_counts())

# Visualize it
plt.figure(figsize=(6,4))
sns.countplot(x='isFraud', data=df)
plt.title('Fraud vs. Genuine Transactions')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Housing.csv')

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Plot distribution of 'price' if it exists
if 'price' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(df['price'], kde=True)
    plt.title('Distribution of House Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

# Correlation heatmap (for numerical columns only)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
# 2. Boxplots for numerical variables
plt.figure(figsize=(12, 8))
numeric_columns = ['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking']
for i, column in enumerate(numeric_columns):
    plt.subplot(2, 3, i + 1)
    sns.boxplot(y=df[column], color='skyblue')
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()

# 3. Line Plot: area vs. price
df_sorted = df.sort_values('area')
plt.figure(figsize=(10, 5))
sns.lineplot(x='area', y='price', data=df_sorted)
plt.title("Line Plot: Area vs. Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

# 4. Scatter Matrix of numeric variables
scatter_matrix(df[numeric_columns], figsize=(12, 10), diagonal='kde')
plt.suptitle("Scatter Matrix of Numeric Features", y=1.02)
plt.show()
# Set style
sns.set(style="darkgrid")

# KDE plots for numeric features
numeric_columns = ['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking']

plt.figure(figsize=(12, 8))
for i, column in enumerate(numeric_columns):
    plt.subplot(2, 3, i + 1)
    sns.kdeplot(data=df[column], fill=True, color='purple')
    plt.title(f'KDE Plot of {column}')
plt.tight_layout()
plt.show()

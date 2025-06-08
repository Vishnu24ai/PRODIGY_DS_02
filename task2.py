import pandas as pd


df = pd.read_csv(r"C:\Users\USER\Desktop\Prodigy June\Titanic-Dataset.csv")


print("📊 Dataset Info:")
print(df.info())
print("\n")


print("📈 Summary Statistics:")
print(df.describe(include='all'))
print("\n")


print("🔍 Missing Values:")
print(df.isnull().sum())
print("\n")


df_cleaned = df.drop(columns=['Cabin', 'Ticket', 'Name'])

df_cleaned = df_cleaned.dropna(subset=['Embarked'])

# 6. Fill missing Age values with median
df_cleaned['Age'].fillna(df_cleaned['Age'].median(), inplace=True)

# 7. Verify cleaning
print("✅ After Cleaning - Missing Values:")
print(df_cleaned.isnull().sum())

# 8. Final shape
print("\n🧹 Cleaned Data Shape:", df_cleaned.shape)

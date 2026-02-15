import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
df = pd.read_csv("preprocessing.csv")
print(df.isnull().sum())
num_col = ['Age','Salary','Experience_Years','Performance_Score']
cat_col = ['Department','City']
for col in num_col:
    df[col] = df[col].fillna(df[col].mean())
for col in cat_col:
    df[col] = df[col].fillna(df[col].mode()[0])
print(df.isnull().sum())
X = df.drop("Performance_Score", axis=1).copy()
y = df["Performance_Score"]
le = LabelEncoder()
X['Department'] = le.fit_transform(X['Department'])
X['City'] = le.fit_transform(X['City'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)
print(X_train_sc[:5])
print(X_test_sc[:5])


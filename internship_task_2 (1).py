# -*- coding: utf-8 -*-
"""Internship Task 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12O3JytX59z6qVHWaKLuSczJ9CRzQP4Kh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
titanic_df = pd.read_csv(url)


train_df = titanic_df.copy()

print("=== Dataset Information ===")
print(train_df.info())
print("\n=== First 5 Rows ===")
print(train_df.head())

print("\n=== Missing Values Before Cleaning ===")
print(train_df.isnull().sum())


if train_df['Age'].isnull().any():
    train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())

train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})

train_df['FamilySize'] = train_df['Siblings/Spouses Aboard'] + train_df['Parents/Children Aboard'] + 1
train_df['IsAlone'] = 0
train_df.loc[train_df['FamilySize'] == 1, 'IsAlone'] = 1

print("\n=== Basic Statistics ===")
print(train_df.describe())

print(f"\nOverall survival rate: {train_df['Survived'].mean():.2%}")

sns.set_style('whitegrid')
plt.figure(figsize=(15, 12))

plt.subplot(2, 2, 1)
sns.barplot(x='Sex', y='Survived', data=train_df)
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender (0=Male, 1=Female)')

plt.subplot(2, 2, 2)
sns.barplot(x='Pclass', y='Survived', data=train_df)
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')

plt.subplot(2, 2, 3)
sns.histplot(train_df['Age'], bins=30, kde=True)
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')

plt.subplot(2, 2, 4)
sns.histplot(data=train_df, x='Age', hue='Survived', bins=30, multiple='stack')
plt.title('Survival by Age')
plt.xlabel('Age')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x='FamilySize', y='Survived', data=train_df)
plt.title('Survival Rate by Family Size')
plt.ylabel('Survival Rate')
plt.xlabel('Family Size')
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(data=train_df, x='Age', hue='Survived', fill=True)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Survived', y='Fare', data=train_df)
plt.title('Fare Distribution by Survival')
plt.xlabel('Survived (0=No, 1=Yes)')
plt.ylabel('Fare')
plt.show()

print("\n=== Key Findings ===")
print(f"1. Overall survival rate: {train_df['Survived'].mean():.2%}")
print(f"2. Female survival rate: {train_df[train_df['Sex'] == 1]['Survived'].mean():.2%}")
print(f"3. Male survival rate: {train_df[train_df['Sex'] == 0]['Survived'].mean():.2%}")
print(f"4. First class survival rate: {train_df[train_df['Pclass'] == 1]['Survived'].mean():.2%}")
print(f"5. Third class survival rate: {train_df[train_df['Pclass'] == 3]['Survived'].mean():.2%}")
print(f"6. Alone passengers survival rate: {train_df[train_df['IsAlone'] == 1]['Survived'].mean():.2%}")
print(f"7. Passengers with family survival rate: {train_df[train_df['IsAlone'] == 0]['Survived'].mean():.2%}")
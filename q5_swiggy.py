import pandas as pd
import numpy as np
from google.colab import files

# ---------------- FILE UPLOAD ---------------- #

uploaded = files.upload()

# Get uploaded file name
file_name = list(uploaded.keys())[0]

# ---------------- LOAD DATASET ---------------- #

df = pd.read_csv(file_name)

print("\n=========== ORIGINAL DATASET ===========\n")
print(df.head())

print("\n=========== DATASET INFO ===========\n")
print(df.info())

print("\n=========== NULL VALUES BEFORE CLEANING ===========\n")
print(df.isnull().sum())

# ---------------- DATA CLEANING ---------------- #

numeric_columns = []

for column in df.columns:

    if (
        "amount" in column.lower()
        or "order" in column.lower()
        or "price" in column.lower()
        or "cost" in column.lower()
        or "total" in column.lower()
    ):

        if df[column].dtype != "object":
            numeric_columns.append(column)

# Replace NULL values in numeric columns with average

for column in numeric_columns:

    average_value = df[column].mean()

    df[column].fillna(average_value, inplace=True)

    print(f"\nAverage replaced in -> {column}")
    print(f"Average value used -> {average_value}")

# Replace remaining null values with "NULL"

remaining_columns = [col for col in df.columns if col not in numeric_columns]

for column in remaining_columns:

    df[column].fillna("NULL", inplace=True)

# ---------------- CLEANED OUTPUT ---------------- #

print("\n=========== CLEANED DATASET ===========\n")
print(df.head())

print("\n=========== NULL VALUES AFTER CLEANING ===========\n")
print(df.isnull().sum())

# ---------------- SAVE CLEANED FILE ---------------- #

cleaned_file = "cleaned_shopping_data.csv"

df.to_csv(cleaned_file, index=False)

print("\nCleaned dataset saved successfully")
print(f"Saved File -> {cleaned_file}")

# ---------------- DOWNLOAD FILE ---------------- #

files.download(cleaned_file)
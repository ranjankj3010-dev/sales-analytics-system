import pandas as pd

def clean_sales_data_pandas(file_path = "Sales-data.rtf"):
    # Load data
    df = pd.read_csv(file_path = "Sales-data.rtf", sep="|")

    total_records = len(df)

    # ---------- CLEANING (KEEP RECORDS) ----------
    # Remove commas from ProductName
    df["ProductName"] = df["ProductName"].str.replace(",", " ", regex=False)

    # Remove commas from numeric columns and convert types
    df["Quantity"] = (
        df["Quantity"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(int)
    )

    df["UnitPrice"] = (
        df["UnitPrice"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # ---------- INVALID RECORD CONDITIONS ----------
    invalid_mask = (
        ~df["TransactionID"].str.startswith("T") |      # TransactionID not starting with T
        (df["Quantity"] <= 0) |                          # Quantity <= 0
        (df["UnitPrice"] <= 0) |                         # UnitPrice <= 0
        (df["CustomerID"].isna()) |                      # Missing CustomerID
        (df["CustomerID"].str.strip() == "") |
        (df["Region"].isna()) |                          # Missing Region
        (df["Region"].str.strip() == "")
    )

    invalid_removed = invalid_mask.sum()

    # Keep only valid records
    df_cleaned = df.loc[~invalid_mask].reset_index(drop=True)

    # ---------- REQUIRED OUTPUT ----------
    print(f"Total records parsed: {total_records}")
    print(f"Invalid records removed: {invalid_removed}")
    print(f"Valid records after cleaning: {len(df_cleaned)}")

    return df_cleaned

import pandas as pd
import os

def clean_csv(df_csv, csv_path, image_dir):
    # Read the CSV file
    df = df_csv
    
    # Initialize a list to store indices of rows to keep
    rows_to_keep = []

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        image_path = os.path.join(image_dir, f"{row['id']}.jpg")
        
        # Check if the image file exists
        if os.path.exists(image_path):
            rows_to_keep.append(index)

    # Keep only the rows where images were found
    df_cleaned = df.loc[rows_to_keep]

    # Reset the index of the cleaned DataFrame
    df_cleaned = df_cleaned.reset_index(drop=True)

    # Save the cleaned CSV
    cleaned_csv_path = csv_path
    df_cleaned.to_csv(cleaned_csv_path, index=False)
    
    print(f"Cleaned CSV saved to: {cleaned_csv_path}")
    print(f"Original row count: {len(df)}")
    print(f"Cleaned row count: {len(df_cleaned)}")

# Usage
csv_output_path = 'datasets/osv5m/train_cleaned.csv'
image_dir = 'datasets/osv5m/images/train/00'
train_csv = 'datasets/osv5m/train.csv'
train_csv = pd.read_csv(train_csv)
clean_csv(train_csv, csv_output_path, image_dir)
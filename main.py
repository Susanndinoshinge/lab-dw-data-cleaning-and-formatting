import pandas as pd
from data_cleaning import clean_data

def main():
    # Load the data
    customer_data = pd.read_csv('customer_data.csv')

    # Clean and format the data
    cleaned_data = clean_data(customer_data)

    # Print the cleaned data
    print("Cleaned Data:")
    print(cleaned_data.head())

    # Save the cleaned data to a new CSV file
    cleaned_data.to_csv('cleaned_data.csv', index=False)

if __name__ == "__main__":
    main()


import pandas as pd

def clean_gender(gender):
    # Clean gender values
    gender = str(gender).lower().strip()
    if gender in ['f', 'femal']:
        return 'F'
    elif gender == 'male':
        return 'M'
    else:
        return gender

state_abbreviations = {
    'az': 'Arizona',
    'cali': 'California',
    'wa': 'Washington'
}

def clean_state(state, state_abbreviations):
    # Your state cleaning logic
    pass

def map_state(state):
    return state_abbreviations.get(state, state)  # Return full name if abbreviation exists, else return original value
customer_data['state'] = customer_data['state'].str.lower().apply(map_state)

def clean_education(education):
    # Clean education values
    return str(education).replace('Bachelors', 'Bachelor')

def clean_vehicle_class(vehicle_class):
    # Clean vehicle class values
    keywords = ['sports', 'luxury']
    if any(keyword in str(vehicle_class).lower() for keyword in keywords):
        return 'Luxury'
    elif 'suv' in str(vehicle_class).lower():
        return 'SUV'
    elif 'car' in str(vehicle_class).lower():
        return 'Car'
    else:
        return vehicle_class

def clean_customer_lifetime_value(value):
    # Clean customer lifetime value column
    return pd.to_numeric(str(value).replace('%', ''), errors='coerce')

def clean_number_of_open_complaints(complaints):
    # Clean number of open complaints column
    complaints = complaints.split('/')
    return int(complaints[1]) if len(complaints) > 1 else int(complaints[0])

def clean_data(customer_data):
    # Apply cleaning functions to the DataFrame
    customer_data['gender'] = customer_data['gender'].apply(clean_gender)
    customer_data['state'] = customer_data['state'].apply(clean_state)
    customer_data['education'] = customer_data['education'].apply(clean_education)
    customer_data['vehicle_class'] = customer_data['vehicle_class'].apply(clean_vehicle_class)
    customer_data['customer_lifetime_value'] = customer_data['customer_lifetime_value'].apply(clean_customer_lifetime_value)
    customer_data['number_of_open_complaints'] = customer_data['number_of_open_complaints'].apply(clean_number_of_open_complaints)
    
    # Fill null values in numerical columns with median, and in categorical columns with mode
    numerical_columns = customer_data.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = customer_data.select_dtypes(include=['object']).columns
    
    customer_data[numerical_columns] = customer_data[numerical_columns].fillna(customer_data[numerical_columns].median())
    customer_data[categorical_columns] = customer_data[categorical_columns].fillna(customer_data[categorical_columns].mode().iloc[0])
    
    # Convert numeric columns to integers
    customer_data[numerical_columns] = customer_data[numerical_columns].applymap(int)
    
    # Drop duplicate rows
    #customer_data = customer_data.drop_duplicates()
    customer_data.drop_duplicates(keep='first', inplace=True, ignore_index=True)
    
    # Reset index for consistency
    #customer_data.reset_index(drop=True, inplace=True)
    
    return customer_data

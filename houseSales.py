# import kagglehub
import pandas as pd

# # Download latest version
# path = kagglehub.dataset_download("abdulwadood11220/usa-house-sales-data")
# print(f"Data downloaded to: {path}")

# Load the dataset
data = pd.read_csv("C:\\Users\\vlche\\.cache\\kagglehub\\datasets\\abdulwadood11220\\usa-house-sales-data\\versions\\1\\us_house_Sales_data.csv")

# # Explore the dataset
# print(data.head(), '\n')
# print(data.info(), '\n')
# print(data.shape, '\n')

# # Check for missing values
# print(data.isnull().sum(), '\n') # None

## Clean and manipulate dataset
# for column in data.columns:
#     print(data[column].value_counts(), '\n')

# Clean Price, Bedrooms, Bathrooms, Area, Lot Size columns
data['Price'] = data['Price'].str.replace('$', '').str.replace(',', '').astype(float)
data['Address'] = data['Address'].str.split(',').str[0]  # Keep only the street address
data['Bedrooms'] = data['Bedrooms'].str.replace(' bds', '').astype(int)
data['Bathrooms'] = data['Bathrooms'].str.replace(' ba', '').astype(int)
data['Area (Sqft)'] = data['Area (Sqft)'].str.replace(' sqft', '').astype(float)
data['Lot Size'] = data['Lot Size'].str.replace(' sqft', '').astype(float)
# split listing agent from company
data['Listing Company'] = data['Listing Agent'].str.split(' - ').str[1]
data['Listing Agent'] = data['Listing Agent'].str.split(' - ').str[0]
# Drop URL column
data = data.drop(columns='Listing URL')

# Rename columns for consistency and convenience
data.columns = data.columns.str.lower().str.split('(').str[0].str.strip().str.replace(' ', '_')

# reorder columns for better readability
data = data[['address', 'city', 'state', 'zipcode', 
             'bedrooms', 'bathrooms', 'area', 'lot_size', 
             'property_type', 'mls_id', 'year_built', 'days_on_market', 
             'price', 'status',
             'listing_agent', 'listing_company']]

for column in data.columns:
    print(data[column].value_counts(), '\n')

# # Save the cleaned dataset
# data.to_excel(".\\houseSales\\cleaned_us_house_sales.xlsx", index=False)
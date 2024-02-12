import pandas as pd
# Read the CSV file into a DataFrame


# df = pd.read_csv('../../Biodata.csv')

# # Convert 'Credit1' column to numeric, coercing errors to NaN
# df['Credit1'] = pd.to_numeric(df['Credit1'], errors='coerce')

# # Perform calculations
# total_expenses = df['Credit1'].sum()
# average_expense = df['Credit1'].mean()

# # Display or save the results
# print("Total expenses:", total_expenses)
# print("Average expense:", average_expense)

# # Drop rows with NaN values in the 'Details' column
# df = df.dropna(subset=['Details'])

# # Filter transactions with 'Swiggy' in the 'Details' column
# swiggy_transactions = df[df['Details'].str.contains('Swiggy', case=False)]

# # Display the filtered transactions
# print("Transactions including 'Swiggy':")
# print(swiggy_transactions)

# # Optionally, save the results to a new CSV file
# # df.to_csv('results.csv', index=False)

# def add(file_path,column_name):
#     df=pd.read_csv(file_path)
#     df[column_name]=pd.to_numeric(df[column_name],errors='coerce')
#     sumResult=df[column_name].sum()
#     return sumResult



import pandas as pd  
 
df = pd.DataFrame({ 
 
    "Order Date": [ 
        "2024-01-10", 
        "2024-01-15", 
        "2024-02-05", 
        "2024-02-12", 
        "2024-03-01", 
        "2024-03-15", 
        "2024-04-10", 
        "2024-04-20", 
        "2024-05-05", 
        "2024-01-15" 
    ], 
 
    "Product Name": [ 
        "Laptop", 
        "Mouse", 
        "Printer", 
        "Tablet", 
        "Laptop", 
        "Monitor", 
        "Mouse", 
        "Printer", 
        "Smartwatch", 
        "Mouse" 
    ], 
 
    "Category": [ 
        "Electronics", 
        "Accessories", 
        "Office", 
        "Electronics", 
        "Electronics", 
        "Accessories", 
        "Accessories", 
        "Office", 
        "Electronics", 
        "Accessories" 
    ], 
 
    "Region": [ 
        "North", 
        "South", 
        "East", 
        "West", 
        "North", 
        "South", 
        "East", 
        "West", 
        "North", 
        "South" 
    ], 
 
    "Quantity": [ 
        2, 
        5, 
        3, 
        4, 
        1, 
        2, 
        6, 
        2, 
        3, 
        5 
    ], 
 
    "Sales": [ 
        50000, 
        2500, 
        9000, 
        30000, 
        55000,         16000, 
        3000, 
        6000, 
        45000, 
        2500 
    ], 
 
    "Profit": [ 
        10000, 
        500, 
        1500, 
        6000, 
        11000, 
        3000, 
        None, 
        1000, 
        9000, 
        500 
    ] 
}) 
  
 
print("ORIGINAL DATASET") 
display(df) 
 
 
 
display(df.head()) 
 
 
# 4. DATASET SHAPE 
 
print("DATASET SHAPE") 
print(df.shape) 
 
 
# 5. COLUMN NAMES 
 
print("COLUMN NAMES") 
print(df.columns) 
 
 
# 6. DATA TYPES 
 
print("DATA TYPES") 
print(df.dtypes) 
 
 
# 7. DESCRIPTIVE STATISTICS 
 
print("DESCRIPTIVE STATISTICS") 
display(df.describe()) 
 
# 8. MISSING VALUES 
 
print("MISSING VALUES") 
print(df.isnull().sum()) 
 
 
# 9. ROWS CONTAINING MISSING VALUES 
 
print("ROWS CONTAINING MISSING VALUES") 
display(df[df.isnull().any(axis=1)]) 
 
 
# 10. TOTAL DUPLICATE RECORDS 
 
print("TOTAL DUPLICATE RECORDS") 
print(df.duplicated().sum()) 
 
 
# 11. DUPLICATE RECORDS 
 
print("DUPLICATE RECORDS") 
display(df[df.duplicated()]) 

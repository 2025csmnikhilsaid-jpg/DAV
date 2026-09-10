import pandas as pd 
 
 
# 9. Create Sample Data 
 
data = { 
    "Name": ["Asha", "Ravi", "Meera", "Karan"], 
    "Marks": [88, 72, 91, 65], 
    "Branch": ["CSE", "ECE", "CSE", "ISE"] 
} 
 
 
# 10. Create a DataFrame 
 
df = pd.DataFrame(data) 
 
print("\n--- Pandas DataFrame ---") 
print(df) 
 
 
# 11. Column Indexing 
 
print("\n--- Column Indexing ---") 
 
print("Name Column:") 
print(df["Name"]) 
 
print("\nMarks Column:") 
print(df["Marks"]) 
 
 
# 12. Row Indexing 
 
print("\n--- Row Indexing ---") 
 
print("First Row:") 
print(df.iloc[0]) 
 
print("\nThird Row:") 
print(df.iloc[2]) 
 
 
# 13. Access a Specific Value 
 
print("\n--- Specific Value ---") 
 
print("Marks of first student:", df.iloc[0, 1]) # 14. DataFrame Row Slicing 
 
print("\n--- Row Slicing ---") 
 
print("First two rows:") 
print(df.iloc[0:2]) 
 
 
# 15. Row and Column Slicing 
 
print("\n--- Row and Column Slicing ---") 
 
print("First three rows with Name and Marks:") 
print(df.iloc[0:3, [0, 1]]) 
 
 
# 16. Filtering Data 
 
print("\n--- Data Filtering ---") 
 
result = df[df["Marks"] > 70] 
 
print("Students with Marks greater than 70:") 
print(result) 

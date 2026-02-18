import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Read Excel file
data = pd.read_excel(r"C:\\Users\\Tejeshewini\\OneDrive\\Desktop\\harsha\\data1.xlsx")

# Preview data
print(data.head())
print(data.tail())

# Rename column
data1 = data.rename(columns={"Customer Fname": "firstname"})
print(data1)

# Handle missing Row_Id
data["Row_Id"] = data["Row_Id"].fillna("C_575488")
data["Row_Id"] = data["Row_Id"].str.split("_").str[1]

# Convert Sales to string
data["Sales"] = data["Sales"].astype(str)

# Check data types
print(data.dtypes)

# MySQL connection
username = "root"
password =quote_plus("harsha@2005")

host = "localhost"
port = 3306
database = "mysql"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Upload to MySQL
data.to_sql("data700", con=engine, if_exists="replace", index=False)

print("done")
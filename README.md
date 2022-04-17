## ETL 

# Repository structure
- data: contains CO2 emissions data in csv format
- mongodb: contains MongoDB Compass screenshot of the Database
- src: contains src.py file with functions
- main.ipynb code with complete ETL process
- .gitignore

# Main
1. Creating a dataframe with basic country info (from csv file)
2. Get indicator codes from World Bank website (web scraping)
3. Country data from World Bank API (2010) (using World Bank's API)
4. Creatinng CO2 emissions dataframe (kaggle csv file)
5. Loading dataframes into local MongoDB

# Resources
- Pandas
- Selenium webdriver
- Pymongo
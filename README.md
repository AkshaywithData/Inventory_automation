# Inventory Automation

## Project Overview

This project demonstrates a complete inventory automation process.

- Reads multiple excel files
- Cleans inventory data
- Removes duplicate records
- Handles missing stock values
- Standardizes category names
- Calculates inventory value
- Generates inventory KPIs and charts
- Archives processed source files
- Generates Excel reports
- Loads processed data into MySQL


## Technologies used

- Python
- Pandas
- Glob
- Shutil
- Matplotlib
- Os
- SQLAlchemy
- Logging
- PyMySQL
- Python-dotenv


## Automation workflow
```
Excel Source Files
        ↓
     Read Excel
        ↓
    Clean Data
        ↓
 Remove Duplicates
        ↓
 Handle Missing Stock
        ↓
 Standardize Categories
        ↓
 Calculate Inventory Value
        ↓
     KPIs
        ↓
     Graphs
        ↓
   Excel Report
        ↓
      MySQL
```


## How to Run

1. Place Excel files in the `Data/Source` folder.

2. Install the required libraries:
   pip install -r requirements.txt

3. Configure your database credentials in '.env'.

4. Run the project:
  Inventory_automation.py


## Project Structure

```
Inventory-Automation/
│
├── LICENSE
├── .env.example
├── .gitignore
├── Inventory_Automation.py
├── README.md
├── requirements.txt
├── inventory.log
│
├── Images/
│   ├── Inventory_dashboard.png
│   ├── Excel_report.png
│   └── Mysql_table.png
│
├── Data/
│   ├── Source/
│   ├── clean_files/
│   └── archive/
│  
└── Final Reports/
    ├── Charts/
    │   └── inventory_dashboard.png
    └── Inventory_Report.xlsx       
```

## Output

The project automatically generates:

- Cleaned Excel files
- Inventory data
- Low stock report
- Category-wise stock summary
- Inventory report in Excel
- MySQL database table
- Archived source files

## Future Improvement

- Improve logging and error handling
- Add configuration file for customizable settings
- Add SQL-based inventory analysis
- Add automated scheduling
- Add low-stock email notifications 
- Add API integration

## Author

Akshay
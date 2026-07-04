# Inventory automation

## Project Overview

This project shows complete inventory automation process

- reads multiple excel files
- cleans data
- remove duplecate records
- fill missing stock values
- Standardize category names
- generate charts and kpis
- archive processed month files
- saves cleaned reports in excel sheets
- saves data to Mysql




## Technologies used

- pyhton
- pandas
- glob
- shutil
- matplotlib
- os
- sqlalchemy
- logging
- pymysql


## How to Run

1. Place Excel files in the `Data/Source` folder.
2. Install the required libraries:
   ```bash
   pip install pandas numpy openpyxl matplotlib sqlalchemy 
   ```
3. Run the project:
   ```bash
  Inventory_automation.py
   ```

## Project Structure

```text
Inventory-Automation/
│
├── Inventory_Automation.py
├── README.md
├── requirements.txt
├── inventory.log
│
├── Images/
│   ├── Inventory_dashboard.png
│   ├── Excel_report.png
│   └── Mysql_table.png
├
│── Data/
│   ├── Source/
│   ├── clean_files/
│   └── archive/
│  
└── Final Reports/
    ├── Charts/
    │   └── inventory_dastboard.png
    └── Inventory_Report.xlsx       
```

## Output

The project automatically generates:

Cleaned Excel files
Inventory data
Low stock report
Category-wise stock summary
Inventory report in Excel
MySQL database table
Archived source files

## Author

Akshay
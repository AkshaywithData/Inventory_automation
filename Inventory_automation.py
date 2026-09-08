import pandas as pd
import os
import shutil
import matplotlib.pyplot as plt
import glob
import numpy as np
from sqlalchemy import create_engine
import logging
from dotenv import load_dotenv

load_dotenv() 

logging.basicConfig(
    filename = "inventory.log", 
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

files = glob.glob("Data/Source/*xlsx")

cleaned = []

def clean_data(file):
    
    logging.info(f"Cleaning started for {file}")

    df = pd.read_excel(file)
        
    df.drop_duplicates(inplace = True)

    df.dropna(how = "all", inplace = True)
        
    df["Stock"] = df["Stock"].fillna(0)
        
    df["Category"] = df["Category"].str.strip().str.title()
        
    cleaned.append(df)

    logging.info(f"Cleaning completed for {file}")

    return df

def save_file(df, file):

    os.makedirs("Data/clean_files/", exist_ok = True)

    os.makedirs("Data/archive/", exist_ok = True)

    shutil.move(file,"Data/archive/"+ os.path.basename(file))

    output = os.path.join("Data/clean_files",
    os.path.basename(file).replace(".xlsx", "_new.xlsx"))
        
    df.to_excel(output, index = False)

    logging.info(f"Saved cleaned file: {output}")

def generate_kpis_charts():

    logging.info("Generating KPIs and charts")  

    final_df = pd.concat(cleaned, ignore_index= True)

    #low stock
    low_stock = final_df[final_df["Stock"]<10]

    #category inventory

    category_stock = final_df.groupby("Category")["Stock"].sum()

    # Product value
    final_df["inventory value"] = final_df["Stock"]* final_df["Price"]

    inventory_value = final_df["inventory value"].sum()

    kpi = {
    "Total Inventory Value": inventory_value,
    "Low Stock Products": len(low_stock),
    "Total Categories": final_df["Category"].nunique()
    }

    os.makedirs("Final Report/Charts", exist_ok=True)

    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)

    plt.bar(category_stock.index,
            category_stock.values)
    

    plt.title("Category Stock")

    plt.subplot(1,2,2)

    plt.bar(low_stock["Product"],
            low_stock["Stock"])

    plt.title("Low Stock Products")

    plt.tight_layout()

    plt.savefig("Final Report/Charts/inventory_dashboard.png", dpi=300, bbox_inches="tight")
    plt.close()

    logging.info("Charts and kpis generated successfully")

    return final_df, low_stock, category_stock, kpi

def generate_excel(final_df, low_stock, category_stock, kpi):

    os.makedirs("Final Report", exist_ok=True)

    kpi_df = pd.DataFrame(list(kpi.items()),columns=["KPI", "Value"])       

    with pd.ExcelWriter("Final Report/Inventory_report.xlsx") as writer:

        final_df.to_excel(writer,sheet_name ="Inventory", index = False)
        
        low_stock.to_excel(writer, sheet_name  ="Low_stock", index = False)
        
        category_stock.reset_index().to_excel(writer, sheet_name = "Category_stock", index = False)

        kpi_df.to_excel(writer, sheet_name="KPIs", index=False)

    logging.info("Excel report created successfully")

def savein_sql(final_df):

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")

    engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )  

    final_df.to_sql("inventory_stock", engine, if_exists="replace", index=False)

    engine.dispose()

    logging.info("Data loaded into MySQL successfully")

if not files:
        logging.warning("No files found to process.")
        print("No files found.")
        exit()

for file in files:

    df = clean_data(file)

    save_file(df, file)

final_df, low_stock, category_stock, kpi = generate_kpis_charts()

generate_excel(final_df, low_stock, category_stock, kpi)

savein_sql(final_df)

logging.info(f"All files processed")






    
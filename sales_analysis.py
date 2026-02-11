#Global SuperStore Sales and Profitable Analysis
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
   "postgresql+psycopg2://postgres:Chokhmah1@localhost:5432/sales_analysis"
)


#Reading Files
file_path = "online_retail_II.xlsx"

df1 = pd.read_excel(file_path,sheet_name=0)
df2 = pd.read_excel(file_path,sheet_name=1)

df = pd.concat([df1,df2], ignore_index=True)

#Columns Work

df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ","_")
) 

df = df.rename(columns={
    "stockcode":"stock_code",
    "invoicedate":"invoice_date"

})




#Removing Missing rows

df = df.dropna(subset=["customer_id","description"])


#Removing Cancelled Orders
df["invoice"].astype(str).str.startswith("C").sum()
df = df[~df["invoice"].astype(str).str.startswith("C")]

#Removing Negative Quantities and Price

df = df[df["quantity"] > 0]
df = df[df["price"] > 0]

#StockCode Column
invalid_code = ["ADJUST","ADJUST2","AMAZONFEE"
                                ,"B","BANK CHARGES","C2","C3","D","DOT",
                                "GIFT","gift_0001_10","gift_0001_20","gift_0001_30","gift_0001_40","gift_0001_50",
                                "gift_0001_60","gift_0001_70","gift_0001_80","gift_0001_90","M","PADS","POST","S","SP1002","TEST001","TEST002"
    
]
df = df[~df["stock_code"].isin(invalid_code)]

#Feature Engineering
#Revenu creation
df["revenue"] = df["quantity"] * df["price"]

df["invoice_date"] = pd.to_datetime(df["invoice_date"], errors = "coerce")
df["year"] = df["invoice_date"].dt.year
df["month"] = df["invoice_date"].dt.month
df["year_month"] = df["invoice_date"].dt.to_period("M").astype(str)
#Total Spend Per Customer

customer_summary = df.groupby("customer_id").agg(
total_revenue = ("revenue", "sum"),
total_orders = ("invoice", "nunique"),
total_quantity = ("quantity","sum")).reset_index()




df.to_sql(
    name="sales_data",
    con=engine,
    if_exists="replace",
    index=False
)

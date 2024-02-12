import sys
import tabula
# from openAi import chatGPT
from bankExtractionScripts import sbi
# import pandas as pd


# Path to your PDF file
# filepath = "../uploads/Account Statement.pdf"
# pdf_password ="1906@1564"
filepath = str(sys.argv[1])
pdf_password =str(sys.argv[2])
query =str(sys.argv[3])

tables  = tabula.read_pdf(filepath,
                       pages='all',
                       silent=True,
                       password=pdf_password,
                       pandas_options={
                           'header': None
                       })
                       
# Convert DataFrames to lists of lists
rows = []
for table in tables:
    rows.extend(table.values.tolist())
result,csvLocation,dataFrame=sbi.sbiFunction(rows)

# gptResponse=chatGPT.functionOpen(result)





print(dataFrame)

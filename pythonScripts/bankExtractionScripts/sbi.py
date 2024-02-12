import pandas as pd

def sbiFunction(rows):
    df=pd.DataFrame(rows)
    df.replace(float('nan'), '', inplace=True)
    list_of_lists = df.values.tolist()   
    headers = [['Date', 'Details', "", 'Debit', 'Credit', "", 'Balance'],['Date', 'Details', '', 'Debit', '', 'Credit', 'Balance']
    ,['', '', 'Ref No./Cheque', '', '', '', ''],['', '', 'No', '', '', '', '']]

    valid_transactions = [] 

    # iterate over all rows to remove headers
    for row in list_of_lists:
        if row not in headers:
            valid_transactions.append(row)
        
    # merging multiline details
    dateIndx = []
    startEndInd = []

    prev=-1
    # ind2=-1

    # storing indexes
    for index,row in enumerate(valid_transactions):
        # print(index)
        if row[0]!='':
            dateIndx.append(index)
        if row[1].startswith('TRANSFER'):
            if prev==-1:
                prev=index
                continue
            if index-1 in dateIndx:
                startEndInd.append([prev,index-2])
                prev=index
                continue
            startEndInd.append([prev,index-1])
            prev=index

    if len(valid_transactions)-1 in dateIndx:
        startEndInd.append([prev,index-2])
        prev=index

    if len(valid_transactions)-1 not in dateIndx:
        startEndInd.append([prev,index])
        prev=index


    result=[]

    i=0
    j=0

    # merging final using indexes
    while i < len(dateIndx) and j < len(startEndInd):
            if dateIndx[i]>startEndInd[j][0] and dateIndx[i]<startEndInd[j][1]:
                if len(valid_transactions[dateIndx[i]])<7:
                    i+=1
                    j+=1
                    continue
                temp=[valid_transactions[dateIndx[i]][0],valid_transactions[startEndInd[j][0]][1]+valid_transactions[dateIndx[i]][1]+valid_transactions[startEndInd[j][1]][1],valid_transactions[dateIndx[i]][2],valid_transactions[dateIndx[i]][3],valid_transactions[dateIndx[i]][4],valid_transactions[dateIndx[i]][5],valid_transactions[dateIndx[i]][6]  ]
                result.append(temp)
                i+=1
                j+=1
            elif dateIndx[i]<startEndInd[j][0]:
                #  print("jj")
                #  if valid_transactions[dateIndx[i]][1]=='':
                #       print(valid_transactions[dateIndx[i]][1])
                temp=[valid_transactions[dateIndx[i]][0],valid_transactions[dateIndx[i]][1],valid_transactions[dateIndx[i]][2],valid_transactions[dateIndx[i]][3],valid_transactions[dateIndx[i]][4],valid_transactions[dateIndx[i]][5],valid_transactions[dateIndx[i]][6]  ]
                result.append(temp)
                i+=1

    # conversion in .csv
    header_names = ['Date', 'Details','Ref','Debit','Credit1',"Credit2",'Balance']
    csv_file_name="statement.csv"
    pd.DataFrame(result).to_csv('./storage/csv/'+csv_file_name, index=False, header=header_names)
    json_data = pd.DataFrame(result).to_json(orient="records")

    

    # Specify the file path where you want to save the JSON file
    json_file_path = "./storage/json/output.json"

    # Write the JSON data to a file
    with open(json_file_path, "w") as json_file:
        json_file.write(json_data)

    return json_data,csv_file_name,result

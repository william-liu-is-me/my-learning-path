import pandas as pd

# this is for remove the existing client and then append new PSSP into the master file.

data1 = pd.read_excel('May.xlsx',converters = {i: str for i in range(11,14)})

data2 = pd.read_excel('sample_result.xlsx',converters = {i: str for i in range(11,14)})

sin_list1 = data1['SIN'].tolist()
sin_list2 = data2['SIN'].tolist()


'''
this function is to capture data that will be removed from the master sheet.
'''
def remove_list(n):
    return n in sin_list2


data3 = data1.loc[data1['SIN'].apply(remove_list)]

data4 = data3.copy()

#data3.to_excel('removed clients.xlsx', sheet_name = 'remove list')


control_sheet_data = pd.DataFrame(columns = ['NAME', 'SIN NUMBER', 'GROSS', 'TAX', 'NET', 'REASON'])

data3 = data3.append(data2, ignore_index = True)

#print(data3)
#create the control sheet
for i in data3.index:
    control_sheet_data.at[i,'NAME'] = data3.at[i,'INITIALS'] + data3.at[i,'LAST NAME']
    control_sheet_data.at[i,'SIN NUMBER'] = data3.at[i,'SIN']
    control_sheet_data.at[i,'GROSS'] = data3.at[i,'GROSS AMOUNT PAYABLE']
    control_sheet_data.at[i,'TAX'] = data3.at[i,'TAX TO BE DEDUCTED']
    control_sheet_data.at[i,'NET'] = data3.at[i,'NET AMOUNT PAYABLE']

#data3.to_excel('removed clients.xlsx', sheet_name = 'draft control sheet')

with pd.ExcelWriter('Removed clients.xlsx') as writer:
    data4.to_excel(writer, sheet_name = 'remove list')
    control_sheet_data.to_excel(writer,sheet_name = 'draft control sheet')
    
'''
function below is to attach all updated PSSP clients into the master sheet. note that any change can be captured,
except the deceased pensioner. manual intervention required to remove the deceased pensioner's record.(if survivor exists,
this function can add survivor records automatically.)
'''

for i in sin_list2:
    if i in sin_list1:
        data1 = data1[data1.SIN != i]


data1 = data1.append(data2, ignore_index = True)

data1.set_index('COUNT', inplace = True)
data1.to_excel('combine.xlsx')



#skip below
'''
for j in range(len(data1.index)):
    data1.at[j,'COUNT'] = j+1
data1[['COUNT']] = data1[['COUNT']].astype('int64') 
print(data1.COUNT.dtypes)
'''


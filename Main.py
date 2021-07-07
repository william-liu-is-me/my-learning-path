import pandas as pd

'''
this is to consolidate the data from extract into data that can be used to prepare master sheet and control sheet.
'''

data = pd.read_excel('PSSP Data extract.xlsx',sheet_name = 'extract')

target_dataframe = pd.read_excel('PSSP Data extract.xlsx',sheet_name = 'required')


def combine_address(index):
    #combine extract address into required address, feed in the index of the extract
    address = ''
    for i in range(1,4):
        location = 'STREET_LINE_'+str(i)
        if type(data.at[index,location]) == str:
            address += data.at[index,location]+' '

    target_dataframe.at[index,'ADDRESS'] = address

def bank_number_revise(index):
    #to make the digital 3 
    target_dataframe.at[index,'BANK NUMBER'] =str(data.at[index,'BANK_NUMBER'])
    if len(target_dataframe.at[index,'BANK NUMBER']) != 3:
        target_dataframe.at[index,'BANK NUMBER'] = '0'*(3-len(target_dataframe.at[index,'BANK NUMBER']))+\
                                            target_dataframe.at[index,'BANK NUMBER']
    

def transit_number_revise(index):
    #to make the digital 5
    target_dataframe.at[index,'TRANSIT NUMBER'] =str(data.at[index,'TRANSIT_NUMBER'])
    if len(target_dataframe.at[index,'TRANSIT NUMBER']) != 5:
        target_dataframe.at[index,'TRANSIT NUMBER'] = '0'*(5-len(target_dataframe.at[index,'TRANSIT NUMBER']))+\
                                            target_dataframe.at[index,'TRANSIT NUMBER']
    
def account_number_check():
    #this must be check manually as you never know there is 0 or not.
    pass

def first_name_to_initials(index):
    #this is for initials
    first_name = str(data.at[index,'FIRST_NAME'])
    first_name = first_name.split()
    initial = str()
    for i in first_name:
        initial += i[0]+'.'+' '

    target_dataframe.at[index,'INITIALS'] = initial


def combine_city_province(index):
    result = data.at[index,'CITY'] +', ' + data.at[index,'PROVINCE']
    target_dataframe.at[index,'CITY PROVINCE'] = result

def all_other_info_move(index):
    #last name, postal code, gross, tax, net, #title to be added later

    target_dataframe.at[index,'LAST NAME']=data.at[index,'LAST_NAME']
    target_dataframe.at[index,'TITLE']=data.at[index,'TITLE']
    target_dataframe.at[index,'SIN']=data.at[index,'CLIENT_SIN']
    target_dataframe.at[index,'POSTAL CODE']=data.at[index,'POSTAL_CODE']
    target_dataframe.at[index,'GROSS AMOUNT PAYABLE']=data.at[index,'MONTHLY_GROSS_PSSP_PENSION_AMT']
    data['MONTHLY_PSSP_TAX_DEDUCTION_AMT'] = data['MONTHLY_PSSP_TAX_DEDUCTION_AMT'].fillna(0)
    target_dataframe.at[index,'TAX TO BE DEDUCTED']=data.at[index,'MONTHLY_PSSP_TAX_DEDUCTION_AMT']
    target_dataframe.at[index,'ACCOUNT NUMBER']=data.at[index,'ACCOUNT_NUMBER']
    target_dataframe.at[index,'NET AMOUNT PAYABLE']=target_dataframe.at[index,'GROSS AMOUNT PAYABLE'] - \
                                                    target_dataframe.at[index,'TAX TO BE DEDUCTED']

def change_color(dat, c ='yellow'):
    #highlight function. may not be used.
    return [f'background-color:{c}' for i in dat]

def ITA_Package(list_of_ITA):
    for i in list_of_ITA:
        combine_address(i)
        bank_number_revise(i)
        transit_number_revise(i)
        first_name_to_initials(i)
        combine_city_province(i)
        all_other_info_move(i)

    #set index
    target_dataframe.set_index('COUNT',inplace = True)


    print('it is working')

ITA_Package(data.index)


'''
target_dataframe.at[target_dataframe.index[-1]+2, 'NET AMOUNT PAYABLE'] = target_dataframe['NET AMOUNT PAYABLE'].sum()
target_dataframe = target_dataframe.style.apply(change_color, axis = 0, subset = ['ACCOUNT NUMBER'])
'''

target_dataframe.to_excel('Sample_Result.xlsx',sheet_name = 'for MGS draft')



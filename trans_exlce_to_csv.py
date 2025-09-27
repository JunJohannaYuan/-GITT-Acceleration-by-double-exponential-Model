'''
This code is used to transform the excel files in the raw data folder of GITT to csv files, 
'''

import pandas as pd
import glob
import warnings

path = '...' # the path of raw excel folder
raw_files = glob.glob(path + "*.xlsx")
path_csv = '...' # the path of save csv folder
csvfiles = glob.glob(path_csv + "*.csv")

'''ignore warnings and transform excel files to csv files'''
warnings.simplefilter('ignore')



'''This part of code is used to transform all excel files in the raw data folder to csv files'''
for file in raw_files:
    print('This is number %d file' % (raw_files.index(file)+1), file)
    try:
        excel_file = pd.ExcelFile(file)
        sheet_names = excel_file.sheet_names[-1]       
        print(sheet_names)
        file_read = pd.read_excel(excel_file, sheet_name = sheet_names)
        file_name = file.split('/')[-1].split('.')[0]
        file_read.to_csv(path_csv + file_name +'.csv' , index = False)
    except:
        print('there is something wrong with the file transformation')
    
print('all excel files have been transformed to csv files')


'''This part of code is used to transform a single excel file 
in the raw data folder to csv file in case of occasional situation'''
def transform_to_csv(file):    #need give the special file path and name
    try:
        excel_file = pd.ExcelFile(file)
        print('done1')
        sheet_names = excel_file.sheet_names[-1]
        print(sheet_names)
        file_read = pd.read_excel(excel_file, sheet_name = sheet_names)
        print('done3')
        file_name = file.split('/')[-1].split('.')[0]
        file_read.to_csv(path_csv + file_name +'.csv' , index = False)
        print('the file have been transformed to csv file')
    except:
        print('there is something wrong with the file transformation')

#transform_to_csv('.../gitt_2_1_20C_15min1h_20241026.xlsx')
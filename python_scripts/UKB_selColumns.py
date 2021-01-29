#!/usr/bin/python

'''
9 May 2020 

Aim: Extract specific columns from large UKB phenotype csv data

column input: -c -colums 
raw data input: -i -input
output, curated data: -o -output

I also need to input the column ids...

The structure of the data column name (UID) is X-Y.Z 
The format for standard data fields is field_id-instance_index.array_index with genomic
SNPs begin prefixed by "affy". For this script, I will always use the last instance, but for the MRI one, I might need to change this...
instance
index is used to distinguish data for a field which was gathered at different times, and the array index is used to distinguish multiple
pieces of data for that field which were gathered at the same time

to run: 

python3 
'''

import pandas as pd
import argparse

def UKB_select_rows(input_dt,col_list,output_dt):
    input_name = str(''.join(input_dt))
    output_name = str(''.join(output_dt))
    col_list_name = str(''.join(col_list))

    #create the list of columns to select 
    col_df = pd.read_csv(col_list_name, sep = ',', usecols = ["FieldID","Instances",'Array'])
    
    #this is the array of columns to select, dont forget to include eid...
    col_list_selected = ['eid']

    #here I make a loop to collect all instances + arrays of a field
    for index, row in col_df.iterrows():
        # range automatically goes from 0 to n-1
        instance_list = list(range(0,row['Instances'].astype(int)))
        list_single_field = []
        for instance_item in instance_list:
            field_instance = [row['FieldID'].astype(str) + "-" + str(instance_item)]
            list_single_field = list_single_field + field_instance
            array_list = list(range(0,row['Array'].astype(int)))
            for fi_item in list_single_field:
                for array_item in array_list:
                    field_instance_array = [str(fi_item) + "." + str(array_item)]
                    col_list_selected = col_list_selected + field_instance_array
                
    #print(len(col_list_selected))
    #col_df['UID'] = col_df["FieldID"].astype(str) + "-" + col_df["Instances"].astype(str) + "." + col_df['Array'].astype(str)
    #selected_UID_list = col_df['UID'].tolist()
    
    # read the large csv file with specified chunksize 
    #I tried with many chunksizes... 
    df_chunk = pd.read_csv(input_name, sep = ',', chunksize=20000, dtype={'eid': int},encoding= 'unicode_escape', usecols = col_list_selected)

    # Each chunk is in df format -> save them 
    # only write header once...
    write_header = True
    for chunk in df_chunk:
        print("20K done, still running...")
        chunk.to_csv(output_name, mode='a', index=False, header=write_header)
        write_header = False


parser = argparse.ArgumentParser(description='Select specific columns from large UKB phenotype csv data')
parser.add_argument('-i', '--input_dt', required=True, nargs='+')
parser.add_argument('-c', '--col_list', required=True, nargs='+')
parser.add_argument('-o', '--output_dt', required=True, nargs='+')
args = parser.parse_args()

if __name__ == '__main__': 
    UKB_select_rows(args.input_dt, args.col_list, args.output_dt)
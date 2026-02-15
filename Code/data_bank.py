from huggingface_hub import hf_hub_download
import pandas as pd
import os
import csv
import copy
import json

data_source_file_path = hf_hub_download(
    repo_id="nguha/legalbench", 
    filename="data/unfair_tos/test.tsv", 
    repo_type="dataset"
)

def load_data():
    df = pd.read_csv(data_source_file_path, sep='\t')
    return df

def is_file_exits(filename: str):
    return os.path.exists(filename)

def open_result_file(filename: str, fields: list):
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
    
def josn_processing(responce:str):
    try:
        data = json.loads(responce, strict=False)
        return data
    except (ValueError, TypeError):
        print('response is not in JSON format')
        return None
    
    
def save_result(filename: str, result: []):
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(result)
        
def load_result_data(file_path_str: str):
    df = pd.read_csv(file_path_str, sep=',')
    return df
"""
Author: Charles Liu

Program: Intro to Cloud Computing Assignment 3; Bulk Uploading to ElasticSearch python code

Date: 6/29/2022

"""
from variables import *
import pandas as pd
from requests_aws4auth import AWS4Auth
import boto3
import requests
import openpyxl
import csv
import string


f = open('ES.csv')

data = csv.reader(f)

idx = 0

char_to_remove = '[]"'

host = ES_URL
path = 'posts/_doc/'
region = 'us-east-1'
service = 'es'
#credentials = boto3.Session().get_credentials()
#awsauth = AWS4Auth(region, service, session_token=credentials.token)


def clean_string(str):
    new_str = ""
    if str != '[""]':
        for char in str:
            if (not char in char_to_remove):
                new_str += char
    else:
        new_str = str
    return new_str


next(data)

for i in data:
    id = int(i[0])
    tags = []
    for index in range(1,len(i)):
        add_str = clean_string(i[index])
        tags.append(add_str)
    print ("#:", idx, " id:", id, " tags:", tags, "\n")
    payload = {"id": id, "tags": tags}
    url = host+path+str(idx+1)+'/'
    r = requests.post(url, auth=(USER, PASS), json = payload)
    print(r.text, "\n")
    idx += 1
    if idx == 1200:
        break



f.close()









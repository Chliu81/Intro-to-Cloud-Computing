import json
import boto3
from datetime import datetime

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
    table = dynamodb.Table('Posts')
    
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    
    post = event['content']
    data = client.put_item(TableName = 'Posts', Item = {"ID": {'N':'1'}, "Date": {'S':date}, "Post":{'S':post}})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'Successfully uploaded': post, 'date': date, 'ID': 1})
    }

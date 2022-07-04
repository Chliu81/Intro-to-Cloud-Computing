import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
    table = dynamodb.Table('Posts')
    
    response = table.scan()
    
    data = response['Items']
    
    for ele in data:
        tags = ele["tags"]
    
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    
    post = event["content"]
    
    return {
        'statusCode': 200,
        'body': json.dumps({'Successfully uploaded': post, 'date': date, 'ID': 1})
    }
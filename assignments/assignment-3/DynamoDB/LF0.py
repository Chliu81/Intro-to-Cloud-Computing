import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
table = dynamodb.Table('Posts')

batch = table.batch_writer()

batch.put_item
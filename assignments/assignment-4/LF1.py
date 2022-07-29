
import requests
from datetime import datetime
import boto3
import json
#from requests_aws4auth import AWS4Auth


region = 'us-east-1' # For example, us-west-1
service = 'es'
#credentials = boto3.Session().get_credentials()
#awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://search-post1-xx3ised4hmqhtgwx22ar7o5lsa.us-east-1.es.amazonaws.com/' # The OpenSearch domain endpoint with https://
index = 'posts'
url = host + '/' + index + '/_search'

headers = { "Content-Type": "application/json"}

# Lambda execution starts here
def lambda_handler(event, context):

    # Put the user query into the query DSL for more accurate search results.
    # Note that certain fields are boosted (^).
    
    # Get Lex Client
    lex_client = boto3.client('lex-runtime')
    
    print('event: ', json.dumps(event))
    
    #processed_query = event['queryStringParameters']['q']
    query = event['queryStringParameters']['q']
    
    processed_query_1 = lex_client.post_text(
        botName='assignment_four',
        botAlias="SearchPostsLex",
        userId="cl5522",
        inputText=query
    )
    
    print(processed_query_1)
    
    processed_query = processed_query_1['slots']['Tag']
    
    query = {
        "size": 25,
        "query": {
            "multi_match": {
                "query": processed_query,
                "fields": ["tags"]
            }
        }
    }

    path = 'https://search-post1-xx3ised4hmqhtgwx22ar7o5lsa.us-east-1.es.amazonaws.com/posts/_doc/_search?q=tags:' + processed_query

    #result = requests.get(url, headers=headers, auth=('charles', 'Aa12345!'), data = json.dumps(query))
    response = requests.get(path, headers=headers, auth=('charles', 'Aa12345!'))
    
    #print(response.text)
    dict1 = json.loads(response.text)
    
    processed_response = dict1['hits']['hits']
    
    
    #print(processed_response)

    client = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
    table = dynamodb.Table('Posts')
    
    post_list = []
    
    for ele in processed_response:
        
        id = ele['_source']['id']
        #print(type(id))
        
        
        data = client.get_item(
            TableName='Posts',
            Key={
                'ID': {
                  'N': str(id)
                }
            }
        )
        
        post = data['Item']['Post']['S']
        #print(post, '\n')
        post_list.append(post)
      
  
    
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    result = json.dumps({'Successfully Searched': post_list, 'date': date})
    
    
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "multiValueHeaders": {},
        "body": result,
        "isBase64Encoded": False
    }
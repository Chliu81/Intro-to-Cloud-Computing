import boto3

client = boto3.client('dynamodb', region_name = 'us-east-1')


try:
    resp = client.create_table(

        TableName = "Posts",

        KeySchema = [
            {
                "AttributeName": "ID",
                "KeyType": "HASH"
            },

        ],

        AttributeDefinitions = [
            {
                "AttributeName": "ID",
                "AttributeType": "N"
            },
        ],

        ProvisionedThroughput = {
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )

    

    print("Table was created successfully!")
    
except Exception as e:
    print ("Error creating table: ")
    print (e)
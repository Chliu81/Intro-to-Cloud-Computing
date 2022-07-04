import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
table = dynamodb.Table('Posts')

batch = table.batch_writer()

data = open("data.csv.CSV", "r", encoding= "latin-1")

lines = data.readlines()

data.close()

for line in lines:
    line.split(',')

for idx in range(1, 5):
    id = int(lines[idx][0])
    date = lines[idx][1]
    post = lines[idx][2]
    batch.put_item(Item = {"ID": id, "Date": date, "Post": post})
    print("Successfully Posted #", idx, "id: ", id, "date: ", date, "post: ", post, "\n")
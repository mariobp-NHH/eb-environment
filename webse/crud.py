import boto3

db = boto3.resource('dynamodb', region_name='eu-north-1')
table = db.Table('signuptable')

# Get item
response = table.get_item(Key={'email':'mario@demo.com'})
print(response['Item'])

# Put item
table.put_item(
  Item={
    'email': 'jane@demo.com',
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25
  }
)

# put item
table.put_item(
    Item={
        'email': 'jane@doe.com',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)

# update item
table.update_item(
    Key={'email': 'jane@doe.com'},
    UpdateExpression='SET age = :val',
    ExpressionAttributeValues={':val': 16}
)

# update item
table.update_item(
    Key={'email': 'jane@demo.com'},
    UpdateExpression='SET age = :val',
    ExpressionAttributeValues={':val': 21}
)

# delete items
table.delete_item(Key={'email': 'jane@doe.com'})
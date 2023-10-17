import json
import boto3

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the DynamoDB table name
table_name = 'CartTable'

def lambda_handler(event, context):
    # Extract request data from the event
    request_body = json.loads(event['body'])
    user_id = request_body['userId']
    cart_items = request_body['cartItems']

    # Update the user's cart in DynamoDB
    response = dynamodb.update_item(
        TableName=table_name,
        Key={
            'UserId': {'S': user_id}
        },
        UpdateExpression='SET Cart = :cart',
        ExpressionAttributeValues={
            ':cart': {'S': json.dumps(cart_items)}
        }
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Cart updated successfully'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

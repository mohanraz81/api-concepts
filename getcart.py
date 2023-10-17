import json,boto3,decimal



class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
        
        
awsregion="us-east-1"
TableName="CartTable"


dynamodb=boto3.resource('dynamodb',region_name=awsregion)
table=dynamodb.Table(TableName)
  
def lambda_handler(event, context):
  print(event)
  response = table.get_item(
                        Key={
                            'userid': event['userid']
                        }
                      )
  response=json.loads(json.dumps(response,cls=DecimalEncoder))
  successmessage={
      "status": 200,
      "statusmessage": "Got Cart", 
      "response": response
  }
  return(successmessage) 

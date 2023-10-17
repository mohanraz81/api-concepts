import boto3

# Specify your AWS region and API Gateway name
aws_region = 'us-east-1'
api_name = 'cart'

# Load your Swagger definition from a YAML file
swagger_definition_file = 'cart-openapidef.yaml'

# Initialize the API Gateway client
apigateway = boto3.client('apigateway', region_name=aws_region)

# Read the Swagger definition from the YAML file
with open(swagger_definition_file, 'r') as swagger_file:
    swagger_definition = swagger_file.read()

# Create the API Gateway REST API
try:
    response = apigateway.import_rest_api(
        body=swagger_definition,
        failOnWarnings='WARN'
    )
    api_id = response['id']
    print(f'API Gateway with ID {api_id} created successfully.')
except Exception as e:
    print(f'Error creating API Gateway: {str(e)}')

#!/bin/bash

# Replace these values with your own
ROLE_NAME="<your-role-name>"
LAMBDA_FUNCTION_NAME="<your-lambda-function-name>"
DYNAMODB_TABLE_NAME="<your-dynamodb-table-name>"

# Create an IAM role for the Lambda function
echo "Creating IAM role..."
aws iam create-role --role-name $ROLE_NAME --assume-role-policy-document file://lambda-trust-policy.json

# Attach a policy to the role that grants access to DynamoDB
echo "Attaching DynamoDB policy to IAM role..."
aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess

# Create a Lambda execution role
echo "Creating Lambda execution role..."
aws lambda create-function --function-name $LAMBDA_FUNCTION_NAME \
    --runtime python3.8 \
    --role arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/$ROLE_NAME \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda_function.zip \
    --environment "Variables={DYNAMODB_TABLE_NAME=$DYNAMODB_TABLE_NAME}"

echo "Lambda function $LAMBDA_FUNCTION_NAME created."

# Clean up temporary files
rm lambda-trust-policy.json

echo "Shell script execution completed."

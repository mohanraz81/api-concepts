#!/bin/bash

# Set your AWS region and table name
aws_region="us-east-1"
table_name="CartTable"

# Define the table schema
schema='
  {
    "TableName": "'$table_name'",
    "KeySchema": [
      { "AttributeName": "UserId", "KeyType": "HASH" }
    ],
    "AttributeDefinitions": [
      { "AttributeName": "UserId", "AttributeType": "S" }
    ],
    "BillingMode": "PAY_PER_REQUEST"
  }
'

# Create the DynamoDB table with On-Demand capacity mode
aws dynamodb create-table --region $aws_region --cli-input-json "$schema"

# Check for table creation status
table_status=$(aws dynamodb wait table-exists --region $aws_region --table-name $table_name)

if [ "$table_status" == "SUCCESS" ]; then
  echo "DynamoDB table $table_name created successfully with On-Demand capacity mode."
else
  echo "Failed to create DynamoDB table 

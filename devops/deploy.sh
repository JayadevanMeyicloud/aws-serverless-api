#!/bin/bash

set -e  # stop script if any command fails

echo "============================"
echo "🚀 SAM BUILD START"
echo "============================"

sam build

echo "============================"
echo "🚀 SAM DEPLOY START"
echo "============================"

sam deploy \
  --stack-name sam-serverless-learnings \
  --region ap-south-1 \
  --capabilities CAPABILITY_IAM \
  --no-confirm-changeset \
  --no-fail-on-empty-changeset \
  --resolve-s3 \
  --s3-prefix sam-serverless-learnings

echo "============================"
echo "✅ DEPLOY COMPLETED"
echo "============================"
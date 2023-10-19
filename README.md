# aws-codebuild-python-lambda

```
aws lambda create-function --function-name aws-codebuild-python-lambda \
  --runtime python3.8 \
  --handler lambda_handler \
  --role arn:aws:iam::506236563550:role/aws-codebuild-python-lambda \
  --zip-file fileb://your-lambda-deployment-package.zip

aws iam create-role --role-name aws-codebuild-python-lambda --assume-role-policy-document file://lambda-execution-trust-policy.json
aws iam put-role-policy --role-name aws-codebuild-python-lambda --policy-name LambdaExecutionPolicy --policy-document file://lambda-execution-policy.json
aws iam update-assume-role-policy --role-name aws-codebuild-python-lambda --policy-document file://lambda-execution-trust-policy.json


aws iam create-policy --policy-name AWSCodeBuild_CloudWatchLogs --policy-document file://aws_code_build_cloudwatch_logs.json



aws iam create-role --role-name AWS_CODEBUILD_SERVICE_ROLE --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "codebuild.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}'

AWSCodeBuild_CloudWatchLogs policy


aws iam attach-role-policy --role-name AWS_CODEBUILD_SERVICE_ROLE --policy-arn arn:aws:iam::aws:policy/service-role/AWSCodeBuild_CloudWatchLogs


aws codebuild create-project --cli-input-json file://codebuild-project.json
aws codebuild start-build --project-name aws-codebuild-python-lambda
```
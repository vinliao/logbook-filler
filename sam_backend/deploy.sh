#!/bin/bash
sam build -u
sam package --s3-bucket logbook-bucket --output-template-file packaged.yaml
sam deploy --template-file ./packaged.yaml --stack-name logbook-stack --capabilities CAPABILITY_IAM --region ap-southeast-1

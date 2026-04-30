\# Cloud Resume API ☁️



A serverless resume API built on AWS as part of the Cloud Resume Challenge.



\## Architecture

\- \*\*AWS Lambda\*\* — Python function that serves resume data

\- \*\*API Gateway\*\* — REST endpoint

\- \*\*DynamoDB\*\* — stores resume data

\- \*\*S3\*\* — hosts the static resume website

\- \*\*SAM/CloudFormation\*\* — Infrastructure as Code



\## Live Links

\- 🌐 Website: https://madison-kennedy-resume.s3.us-east-1.amazonaws.com/index.html

\- 🔗 API: https://ihxkbdrihk.execute-api.us-east-1.amazonaws.com/Prod/resume



\## Deploy

```bash

sam build

sam deploy

```


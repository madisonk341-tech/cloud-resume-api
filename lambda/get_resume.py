import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ResumeData')

SECTIONS = ['meta', 'skills', 'education', 'certifications', 'experience', 'projects']

def convert(obj):
    # DynamoDB returns Python sets for SS types — convert everything to JSON-safe types
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, list):
        return [convert(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert(v) for k, v in obj.items()}
    return obj

def handler(event, context):
    try:
        resume = {}
        for section in SECTIONS:
            response = table.get_item(Key={'section': section})
            if 'Item' in response:
                resume[section] = convert(response['Item'])

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(resume)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
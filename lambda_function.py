import boto3
import base64
import json

def lambda_handler(event, context):
    try:
        client = boto3.client('textract')

        # The body is a JSON string, so parse it into a dictionary
        body = json.loads(event.get('body', '{}'))

        # Extract the 'image_data' field from the parsed body
        image_data = body.get('image_data')
        if not image_data:
            return {
                'statusCode': 400,
                'body': json.dumps('No image data provided')
            }

        # Decode the base64 image
        image_bytes = base64.b64decode(image_data)

        # Using Textract to analyze the document
        response = client.analyze_document(Document={'Bytes': image_bytes}, FeatureTypes=['TABLES', 'FORMS'])

        # Extracting text
        blocks = response['Blocks']
        text = ""
        for block in blocks:
            if block['BlockType'] == 'WORD' or block['BlockType'] == 'LINE':
                text += block['Text'] + ' '

        return {
            'statusCode': 200,
            'body': json.dumps(text)
        }

    except KeyError as e:
        # Handle missing data
        return {
            'statusCode': 400,
            'body': json.dumps(f"Missing key: {e.args[0]}")
        }
    except Exception as e:
        # Handle other exceptions
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

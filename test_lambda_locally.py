from lambda_function import lambda_handler
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

if __name__ == "__main__":
    # Path to your image
    image_path = '/Users/safrout/Desktop/simpleText.png'

    # Create test event
    test_event = {
        "image_data": encode_image_to_base64(image_path)
    }

    # Call the Lambda handler
    response = lambda_handler(test_event, None)

    # Print the response
    print(response)
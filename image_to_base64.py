import base64

def convert_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# Replace 'path_to_your_image.jpg' with the path to your actual image file
base64_string = convert_image_to_base64('simpleText.png')

# Optionally, save this string to a file
with open('image_base64.txt', 'w') as file:
    file.write(base64_string)

import argparse
import os
import re
import requests

# Command line arguments
parser = argparse.ArgumentParser(description='Generate images using the DALL-E 2 API.')
parser.add_argument('prompt', help='The prompt to use for generating the image.')
args = parser.parse_args()

# API setup
with open('api_key.txt', 'r') as f:
    api_key = f.read().strip()
endpoint = 'https://api.openai.com/v1/images/generations'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}',}

# Image generation
def generate_image(prompt, cleaned_title):
    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=data)

    # Check for errors
    if response.status_code != 200:
        print(f"Error generating image: {response.json()['error']}")
        return None

    # Extract the image URL from the response
    image_url = response.json()['data'][0]['url']

    # Download the image and save it to the specified file path
    image_file = f"{cleaned_title}.png"
    image_path = os.path.join('assets', 'images', image_file)
    response = requests.get(image_url)
    with open(image_path, 'wb') as f:
        f.write(response.content)
    print(f"Generated {prompt} and saved it to '{image_path}'")

    # Update the image path in the Jekyll post
    post_path = os.path.join('_posts', f"{cleaned_title}.md")
    update_image_in_post(post_path, f"/assets/images/{image_file}")
    print(f"Updated image for post: {cleaned_title}")

    # Return the file path of the saved image
    return image_file


if __name__ == '__main__':
    post_title = args.prompt
    prompt = f"An image for a post titled '{post_title}'"
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')
    generate_image(prompt, cleaned_title)

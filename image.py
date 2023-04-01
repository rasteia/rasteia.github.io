import argparse
import frontmatter
import os
import requests
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--existingnew', action='store_true')
args = parser.parse_args()

api_key = open("C:\\Users\\darde\\code\\ap.txt", "r").readline().strip()
endpoint = "https://api.openai.com/v1/images/generations"

def generate_image(title):
    prompt = f"Create an image of {title}"
    payload = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "256x256",
        "response_format": "url"
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['data'][0]['url']

def generate_image_for_post(posts_dir, post_filename):
    post_path = os.path.join(posts_dir, post_filename)
    with open(post_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    title = post.metadata['title']
    image_url = generate_image(title)
    image_file = f"{title.replace(' ', '_')}.jpg"
    image_path = os.path.join('./assets/images', image_file)
    response = requests.get(image_url, stream=True)
    response.raw.decode_content = True
    with open(image_path, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
    update_image_filename(post_path, image_file)
    print(f"Generated image for {title} and saved it to {image_path}")

def update_image_filename(post_path, image_file):
    with open(post_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    post.metadata['image'] = f'/assets/images/{image_file}'
    with open(post_path, 'w', encoding='utf-8') as f:
        frontmatter.dump(post, f)
    print(f"Updated image filename in {post_path}")
    
def move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, existing_new=False):
    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            post_path = os.path.join(src_dir, file)
            if existing_new:
                generate_image_for_post(src_dir, file)
            dest_path = os.path.join(dest_dir, file)
            add_template_to_post(post_path, template_path)
            move_post(post_path, dest_path)
            process_post(dest_path, tts_script_path)

def main():
    if args.existingnew:
        for file in os.listdir('./_posts'):
            if file.endswith('.md'):
                post_path = os.path.join('./_posts', file)
                generate_image_for_post(post_path)
    else:
        title = args.title
        image_url = generate_image(title)
        image_file = f"{title.replace(' ', '_')}.jpg"
        image_path = os.path.join('./assets/images', image_file)
        response = requests.get(image_url, stream=True)
        response.raw.decode_content = True
        with open(image_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        print(f"Generated image for '{title}' and saved it to {image_path}")

    main()

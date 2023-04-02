---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-debugging
  image generator jekyll.mp3\" type=\"audio/mpeg\">\n              Your browser does
  not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/2023-04-01-debugging-image-generator-jekyll.png
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Debugging Image Generator Jekyll
---

Yes, we can modify `image.py` to accept a `--prompt` flag that specifies the prompt to use when generating the image. Here's an updated version of `image.py` with the `--prompt` flag implemented:

```
pythonCopy codeimport requests, json, os, argparse, re
import frontmatter

# Command line arguments
parser = argparse.ArgumentParser(description='Generate images using the DALL-E 2 API.')
parser.add_argument('--all', action='store_true', help='Generate images for all posts.')
parser.add_argument('--select', nargs='+', help='Generate images for selected posts.')
parser.add_argument('--new', action='store_true', help='Generate images for new posts.')
parser.add_argument('--prompt', help='The prompt to use for generating the image.')
args = parser.parse_args()

# API setup
with open('C:/Users/darde/code/ap.txt', 'r') as f:
    api_key = f.read().strip()
endpoint = 'https://api.openai.com/v1/images/generations'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}',}

# Image generation
def generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file


# Image update in post
def update_image_in_post(post_path, image_path):
    # Load the post content from the file
    with open(post_path, 'r', encoding='utf-8') as f:
        post_content = f.read()

    # Parse the frontmatter and update the image field
    post = frontmatter.loads(post_content)
    post['image'] = image_path

    # Write the updated content back to the file
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post) + post.content)


# Process posts
if args.all:
    posts_dir = '_posts'
elif args.select:
    posts_dir = '_posts'
    selected_posts = [f"{post}.md" for post in args.select]
elif args.new:
    posts_dir = 'C:/Users/darde/Downloads/jekyllposts'
else:
    print("No posts selected. Please specify --all, --select, or --new.")
    exit()

for file in os.listdir(posts_dir):
    if not file.endswith('.md'):
        continue
    if args.select and file not in selected_posts:
        continue
    post_path = os.path.join(posts_dir, file)

```

1 / 1

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)![Daniel Darden](https://chat.openai.com/_next/image?url=https%3A%2F%2Fs.gravatar.com%2Favatar%2Ffd80a1ccc4646ffe2f40a00e9db3aff3%3Fs%3D480%26r%3Dpg%26d%3Dhttps%253A%252F%252Fcdn.auth0.com%252Favatars%252Fdd.png&w=64&q=75)

and thenupdate newpost.py like this? os.system(f"python {photo\_script\_path} --prompt {post\_title}")

1 / 1

Yes, that should work. You can modify the `generate_image` function in `image.py` to accept a `prompt` argument and use it in the API request to generate the image. Here's an example:

```
pythonCopy codedef generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file

```

Then, in `newpost.py`, you can modify the `move_and_process_posts` function to pass the post title as the `prompt` argument to `image.py` using the `subprocess` module:

```
pythonCopy codeimport subprocess

def move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            print(f"Processing {file}...")

            src_file_path = os.path.join(src_dir, file)
            with open(src_file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            with open(template_path, 'r', encoding='utf-8') as f:
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

            # Remove the original file from the source directory
            os.remove(src_file_path)
            print(f"Moved {file} to {dest_file_path}")

            # Run tts.py
            print(f"Running tts.py for {file}...")
            os.system(f"python {tts_script_path}")

            # Run image.py
            post_title = os.path.splitext(file)[0].replace('-', ' ').title()
            print(f"Running image.py for {file}...")
            subprocess.run(['python', photo_script_path, '--prompt', post_title])

```

This should pass the post title as the `prompt` argument to `image.py`

1 / 1Yes, we can modify `image.py` to accept a `--prompt` flag that specifies the prompt to use when generating the image. Here's an updated version of `image.py` with the `--prompt` flag implemented:

```
pythonCopy codeimport requests, json, os, argparse, re
import frontmatter

# Command line arguments
parser = argparse.ArgumentParser(description='Generate images using the DALL-E 2 API.')
parser.add_argument('--all', action='store_true', help='Generate images for all posts.')
parser.add_argument('--select', nargs='+', help='Generate images for selected posts.')
parser.add_argument('--new', action='store_true', help='Generate images for new posts.')
parser.add_argument('--prompt', help='The prompt to use for generating the image.')
args = parser.parse_args()

# API setup
with open('C:/Users/darde/code/ap.txt', 'r') as f:
    api_key = f.read().strip()
endpoint = 'https://api.openai.com/v1/images/generations'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}',}

# Image generation
def generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file


# Image update in post
def update_image_in_post(post_path, image_path):
    # Load the post content from the file
    with open(post_path, 'r', encoding='utf-8') as f:
        post_content = f.read()

    # Parse the frontmatter and update the image field
    post = frontmatter.loads(post_content)
    post['image'] = image_path

    # Write the updated content back to the file
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post) + post.content)


# Process posts
if args.all:
    posts_dir = '_posts'
elif args.select:
    posts_dir = '_posts'
    selected_posts = [f"{post}.md" for post in args.select]
elif args.new:
    posts_dir = 'C:/Users/darde/Downloads/jekyllposts'
else:
    print("No posts selected. Please specify --all, --select, or --new.")
    exit()

for file in os.listdir(posts_dir):
    if not file.endswith('.md'):
        continue
    if args.select and file not in selected_posts:
        continue
    post_path = os.path.join(posts_dir, file)

```

1 / 1

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)![Daniel Darden](https://chat.openai.com/_next/image?url=https%3A%2F%2Fs.gravatar.com%2Favatar%2Ffd80a1ccc4646ffe2f40a00e9db3aff3%3Fs%3D480%26r%3Dpg%26d%3Dhttps%253A%252F%252Fcdn.auth0.com%252Favatars%252Fdd.png&w=64&q=75)

and thenupdate newpost.py like this? os.system(f"python {photo\_script\_path} --prompt {post\_title}")

1 / 1

Yes, that should work. You can modify the `generate_image` function in `image.py` to accept a `prompt` argument and use it in the API request to generate the image. Here's an example:

```
pythonCopy codedef generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file

```

Then, in `newpost.py`, you can modify the `move_and_process_posts` function to pass the post title as the `prompt` argument to `image.py` using the `subprocess` module:

```
pythonCopy codeimport subprocess

def move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            print(f"Processing {file}...")

            src_file_path = os.path.join(src_dir, file)
            with open(src_file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            with open(template_path, 'r', encoding='utf-8') as f:
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

            # Remove the original file from the source directory
            os.remove(src_file_path)
            print(f"Moved {file} to {dest_file_path}")

            # Run tts.py
            print(f"Running tts.py for {file}...")
            os.system(f"python {tts_script_path}")

            # Run image.py
            post_title = os.path.splitext(file)[0].replace('-', ' ').title()
            print(f"Running image.py for {file}...")
            subprocess.run(['python', photo_script_path, '--prompt', post_title])

```

This should pass the post title as the `prompt` argument to `image.py`

1 / 1Yes, we can modify `image.py` to accept a `--prompt` flag that specifies the prompt to use when generating the image. Here's an updated version of `image.py` with the `--prompt` flag implemented:

```
pythonCopy codeimport requests, json, os, argparse, re
import frontmatter

# Command line arguments
parser = argparse.ArgumentParser(description='Generate images using the DALL-E 2 API.')
parser.add_argument('--all', action='store_true', help='Generate images for all posts.')
parser.add_argument('--select', nargs='+', help='Generate images for selected posts.')
parser.add_argument('--new', action='store_true', help='Generate images for new posts.')
parser.add_argument('--prompt', help='The prompt to use for generating the image.')
args = parser.parse_args()

# API setup
with open('C:/Users/darde/code/ap.txt', 'r') as f:
    api_key = f.read().strip()
endpoint = 'https://api.openai.com/v1/images/generations'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}',}

# Image generation
def generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file


# Image update in post
def update_image_in_post(post_path, image_path):
    # Load the post content from the file
    with open(post_path, 'r', encoding='utf-8') as f:
        post_content = f.read()

    # Parse the frontmatter and update the image field
    post = frontmatter.loads(post_content)
    post['image'] = image_path

    # Write the updated content back to the file
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post) + post.content)


# Process posts
if args.all:
    posts_dir = '_posts'
elif args.select:
    posts_dir = '_posts'
    selected_posts = [f"{post}.md" for post in args.select]
elif args.new:
    posts_dir = 'C:/Users/darde/Downloads/jekyllposts'
else:
    print("No posts selected. Please specify --all, --select, or --new.")
    exit()

for file in os.listdir(posts_dir):
    if not file.endswith('.md'):
        continue
    if args.select and file not in selected_posts:
        continue
    post_path = os.path.join(posts_dir, file)

```

1 / 1

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)![Daniel Darden](https://chat.openai.com/_next/image?url=https%3A%2F%2Fs.gravatar.com%2Favatar%2Ffd80a1ccc4646ffe2f40a00e9db3aff3%3Fs%3D480%26r%3Dpg%26d%3Dhttps%253A%252F%252Fcdn.auth0.com%252Favatars%252Fdd.png&w=64&q=75)

and thenupdate newpost.py like this? os.system(f"python {photo\_script\_path} --prompt {post\_title}")

1 / 1

Yes, that should work. You can modify the `generate_image` function in `image.py` to accept a `prompt` argument and use it in the API request to generate the image. Here's an example:

```
pythonCopy codedef generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file

```

Then, in `newpost.py`, you can modify the `move_and_process_posts` function to pass the post title as the `prompt` argument to `image.py` using the `subprocess` module:

```
pythonCopy codeimport subprocess

def move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            print(f"Processing {file}...")

            src_file_path = os.path.join(src_dir, file)
            with open(src_file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            with open(template_path, 'r', encoding='utf-8') as f:
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

            # Remove the original file from the source directory
            os.remove(src_file_path)
            print(f"Moved {file} to {dest_file_path}")

            # Run tts.py
            print(f"Running tts.py for {file}...")
            os.system(f"python {tts_script_path}")

            # Run image.py
            post_title = os.path.splitext(file)[0].replace('-', ' ').title()
            print(f"Running image.py for {file}...")
            subprocess.run(['python', photo_script_path, '--prompt', post_title])

```

This should pass the post title as the `prompt` argument to `image.py`

1 / 1Yes, we can modify `image.py` to accept a `--prompt` flag that specifies the prompt to use when generating the image. Here's an updated version of `image.py` with the `--prompt` flag implemented:

```
pythonCopy codeimport requests, json, os, argparse, re
import frontmatter

# Command line arguments
parser = argparse.ArgumentParser(description='Generate images using the DALL-E 2 API.')
parser.add_argument('--all', action='store_true', help='Generate images for all posts.')
parser.add_argument('--select', nargs='+', help='Generate images for selected posts.')
parser.add_argument('--new', action='store_true', help='Generate images for new posts.')
parser.add_argument('--prompt', help='The prompt to use for generating the image.')
args = parser.parse_args()

# API setup
with open('C:/Users/darde/code/ap.txt', 'r') as f:
    api_key = f.read().strip()
endpoint = 'https://api.openai.com/v1/images/generations'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}',}

# Image generation
def generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file


# Image update in post
def update_image_in_post(post_path, image_path):
    # Load the post content from the file
    with open(post_path, 'r', encoding='utf-8') as f:
        post_content = f.read()

    # Parse the frontmatter and update the image field
    post = frontmatter.loads(post_content)
    post['image'] = image_path

    # Write the updated content back to the file
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post) + post.content)


# Process posts
if args.all:
    posts_dir = '_posts'
elif args.select:
    posts_dir = '_posts'
    selected_posts = [f"{post}.md" for post in args.select]
elif args.new:
    posts_dir = 'C:/Users/darde/Downloads/jekyllposts'
else:
    print("No posts selected. Please specify --all, --select, or --new.")
    exit()

for file in os.listdir(posts_dir):
    if not file.endswith('.md'):
        continue
    if args.select and file not in selected_posts:
        continue
    post_path = os.path.join(posts_dir, file)

```

1 / 1

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)![Daniel Darden](https://chat.openai.com/_next/image?url=https%3A%2F%2Fs.gravatar.com%2Favatar%2Ffd80a1ccc4646ffe2f40a00e9db3aff3%3Fs%3D480%26r%3Dpg%26d%3Dhttps%253A%252F%252Fcdn.auth0.com%252Favatars%252Fdd.png&w=64&q=75)

and thenupdate newpost.py like this? os.system(f"python {photo\_script\_path} --prompt {post\_title}")

1 / 1

Yes, that should work. You can modify the `generate_image` function in `image.py` to accept a `prompt` argument and use it in the API request to generate the image. Here's an example:

```
pythonCopy codedef generate_image(prompt, post_title):
    # Clean up the post title to remove invalid characters
    cleaned_title = re.sub(r'[^\w\s-]', '', post_title).strip().lower().replace(' ', '-')

    # Set up the prompt and model parameters
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512',
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

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

    # Return the file path of the saved image
    return image_file

```

Then, in `newpost.py`, you can modify the `move_and_process_posts` function to pass the post title as the `prompt` argument to `image.py` using the `subprocess` module:

```
pythonCopy codeimport subprocess

def move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            print(f"Processing {file}...")

            src_file_path = os.path.join(src_dir, file)
            with open(src_file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            with open(template_path, 'r', encoding='utf-8') as f:
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

            # Remove the original file from the source directory
            os.remove(src_file_path)
            print(f"Moved {file} to {dest_file_path}")

            # Run tts.py
            print(f"Running tts.py for {file}...")
            os.system(f"python {tts_script_path}")

            # Run image.py
            post_title = os.path.splitext(file)[0].replace('-', ' ').title()
            print(f"Running image.py for {file}...")
            subprocess.run(['python', photo_script_path, '--prompt', post_title])

```

This should pass the post title as the `prompt` argument to `image.py`

1 / 1
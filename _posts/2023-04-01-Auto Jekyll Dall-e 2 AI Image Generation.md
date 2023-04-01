---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Auto
  Jekyll Dall-e 2 AI Image Generation.mp3\" type=\"audio/mpeg\">\n              Your
  browser does not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/cpunk3.jfif
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Auto Jekyll Dall E 2 Ai Image Generation
---

Let me provide the complete code for `photo.py` that integrates with `postprocess.py` as you requested.

```
import argparse import frontmatter import os import requests import shutil parser = argparse.ArgumentParser() parser.add\_argument('--existingnew', action='store\_true') args = parser.parse\_args() api\_key = open("C:\\\\Users\\\\darde\\\\code\\\\ap.txt", "r").readline().strip() endpoint = "https://api.openai.com/v1/images/generations" def generate\_image(title): prompt = f"Create an image of {title}" payload = { "model": "image-alpha-001", "prompt": prompt, "num\_images": 1, "size": "256x256", "response\_format": "url" } headers = { "Authorization": f"Bearer {api\_key}", "Content-Type": "application/json" } response = requests.post(endpoint, json=payload, headers=headers) response.raise\_for\_status() return response.json()\['data'\]\[0\]\['url'\] def generate\_image\_for\_post(posts\_dir, post\_filename): post\_path = os.path.join(posts\_dir, post\_filename) with open(post\_path, 'r', encoding='utf-8') as f: post = frontmatter.load(f) title = post.metadata\['title'\] image\_url = generate\_image(title) image\_file = f"{title.replace(' ', '\_')}.jpg" image\_path = os.path.join('./assets/images', image\_file) response = requests.get(image\_url, stream=True) response.raw.decode\_content = True with open(image\_path, 'wb') as f: shutil.copyfileobj(response.raw, f) update\_image\_filename(post\_path, image\_file) print(f"Generated image for {title} and saved it to {image\_path}") def update\_image\_filename(post\_path, image\_file): with open(post\_path, 'r', encoding='utf-8') as f: post = frontmatter.load(f) post.metadata\['image'\] = f'/assets/images/{image\_file}' with open(post\_path, 'w', encoding='utf-8') as f: frontmatter.dump(post, f) print(f"Updated image filename in {post\_path}") def move\_and\_process\_posts(src\_dir, dest\_dir, template\_path, tts\_script\_path, existing\_new=False): for file in os.listdir(src\_dir): if file.endswith('.md'): post\_path = os.path.join(src\_dir, file) if existing\_new: generate\_image\_for\_post(src\_dir, file) dest\_path = os.path.join(dest\_dir, file) add\_template\_to\_post(post\_path, template\_path) move\_post(post\_path, dest\_path) process\_post(dest\_path, tts\_script\_path) def main(): if args.existingnew: for file in os.listdir('./\_posts'): if file.endswith('.md'): post\_path = os.path.join('./\_posts', file) generate\_image\_for\_post(post\_path) else: title = args.title image\_url = generate\_image(title) image\_file = f"{title.replace(' ', '\_')}.jpg" image\_path = os.path.join('./assets/images', image\_file) response = requests.get(image\_url, stream=True) response.raw.decode\_content = True with open(image\_path, 'wb') as f: shutil.copyfileobj(response.raw, f) print(f"Generated image for '{title}' and saved it to {image\_path}") if \_\_name\_\_ == '\_\_main\_\_': main()
---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Jekyll
  Workflow test.mp3\" type=\"audio/mpeg\">\n              Your browser does not support
  the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/2023-04-01-jekyll-workflow-test.png
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Jekyll Workflow Test
---

def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")def generate\_image(prompt, cleaned\_title): \# Set up the prompt and model parameters data = { 'model': 'image-alpha-001', 'prompt': prompt, 'num\_images': 1, 'size': '512x512', } \# Make the API request response = requests.post(endpoint, headers=headers, data=data) \# Check for errors if response.status\_code != 200: print(f"Error generating image: {response.json()\['error'\]}") return None \# Extract the image URL from the response image\_url = response.json()\['data'\]\[0\]\['url'\] \# Download the image and save it to the specified file path image\_file = f"{cleaned\_title}.png" image\_path = os.path.join('assets', 'images', image\_file) response = requests.get(image\_url) with open(image\_path, 'wb') as f: f.write(response.content) print(f"Generated {prompt} and saved it to '{image\_path}'")
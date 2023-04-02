---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Jekyll
  Workflow Streamlined Debugging Continued..mp3\" type=\"audio/mpeg\">\n              Your
  browser does not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/2023-04-01-jekyll-workflow-streamlined-debugging-continued.png
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Jekyll Workflow Streamlined Debugging Continued.
---

The error is caused by `post_title` not being defined. You can fix this by setting `post_title` before calling `os.system()`. Here's the updated `main()` function for `newpost.py`:

```
pythonCopy codedef main():
    src_dir = 'C:/Users/darde/Downloads/jekyllposts'
    dest_dir = './_posts'
    template_path = './templatehead.txt'
    tts_script_path = './tts.py'
    photo_script_path = './image.py'

    while True:
        # Check for new files every 10 seconds
        time.sleep(10)

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

                # Set post_title variable
                post_title = os.path.splitext(file)[0].replace('-', ' ').title()

                # Run tts.py
                print(f"Running tts.py for {file}...")
                os.system(f"python {tts_script_path}")

                # Run image.py
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --prompt \"{post_title}\"")

```

This sets the `post_title` variable before running `os.system()` with the updated `image.py` command.The error is caused by `post_title` not being defined. You can fix this by setting `post_title` before calling `os.system()`. Here's the updated `main()` function for `newpost.py`:

```
pythonCopy codedef main():
    src_dir = 'C:/Users/darde/Downloads/jekyllposts'
    dest_dir = './_posts'
    template_path = './templatehead.txt'
    tts_script_path = './tts.py'
    photo_script_path = './image.py'

    while True:
        # Check for new files every 10 seconds
        time.sleep(10)

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

                # Set post_title variable
                post_title = os.path.splitext(file)[0].replace('-', ' ').title()

                # Run tts.py
                print(f"Running tts.py for {file}...")
                os.system(f"python {tts_script_path}")

                # Run image.py
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --prompt \"{post_title}\"")

```

This sets the `post_title` variable before running `os.system()` with the updated `image.py` command.The error is caused by `post_title` not being defined. You can fix this by setting `post_title` before calling `os.system()`. Here's the updated `main()` function for `newpost.py`:

```
pythonCopy codedef main():
    src_dir = 'C:/Users/darde/Downloads/jekyllposts'
    dest_dir = './_posts'
    template_path = './templatehead.txt'
    tts_script_path = './tts.py'
    photo_script_path = './image.py'

    while True:
        # Check for new files every 10 seconds
        time.sleep(10)

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

                # Set post_title variable
                post_title = os.path.splitext(file)[0].replace('-', ' ').title()

                # Run tts.py
                print(f"Running tts.py for {file}...")
                os.system(f"python {tts_script_path}")

                # Run image.py
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --prompt \"{post_title}\"")

```

This sets the `post_title` variable before running `os.system()` with the updated `image.py` command.The error is caused by `post_title` not being defined. You can fix this by setting `post_title` before calling `os.system()`. Here's the updated `main()` function for `newpost.py`:

```
pythonCopy codedef main():
    src_dir = 'C:/Users/darde/Downloads/jekyllposts'
    dest_dir = './_posts'
    template_path = './templatehead.txt'
    tts_script_path = './tts.py'
    photo_script_path = './image.py'

    while True:
        # Check for new files every 10 seconds
        time.sleep(10)

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

                # Set post_title variable
                post_title = os.path.splitext(file)[0].replace('-', ' ').title()

                # Run tts.py
                print(f"Running tts.py for {file}...")
                os.system(f"python {tts_script_path}")

                # Run image.py
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --prompt \"{post_title}\"")

```

This sets the `post_title` variable before running `os.system()` with the updated `image.py` command.
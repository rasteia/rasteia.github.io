---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-debugging
  jekyll newpost.py automatic post formatting.mp3\" type=\"audio/mpeg\">\n              Your
  browser does not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/2023-04-01-debugging-jekyll-newpostpy-automatic-post-formatting.png
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Debugging Jekyll Newpost.Py Automatic Post Formatting
---

how do i add the right flag in newpost.py to properly call the image.py do i use the new flag?

4 / 4

Yes, you can use the `--new` flag to call the `image.py` script with the newly created post. You can modify the `move_and_process_posts` function in `newpost.py` to include the `--new` flag when calling `image.py`:

```
pythonCopy codedef move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    while True:
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
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --new")

        # Wait for 5 seconds before checking for new files again
        time.sleep(5)

```

This will call `image.py` with the `--new` flag for each newly created post in the source directory.how do i add the right flag in newpost.py to properly call the image.py do i use the new flag?

4 / 4

Yes, you can use the `--new` flag to call the `image.py` script with the newly created post. You can modify the `move_and_process_posts` function in `newpost.py` to include the `--new` flag when calling `image.py`:

```
pythonCopy codedef move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    while True:
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
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --new")

        # Wait for 5 seconds before checking for new files again
        time.sleep(5)

```

This will call `image.py` with the `--new` flag for each newly created post in the source directory.how do i add the right flag in newpost.py to properly call the image.py do i use the new flag?

4 / 4

Yes, you can use the `--new` flag to call the `image.py` script with the newly created post. You can modify the `move_and_process_posts` function in `newpost.py` to include the `--new` flag when calling `image.py`:

```
pythonCopy codedef move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    while True:
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
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --new")

        # Wait for 5 seconds before checking for new files again
        time.sleep(5)

```

This will call `image.py` with the `--new` flag for each newly created post in the source directory.how do i add the right flag in newpost.py to properly call the image.py do i use the new flag?

4 / 4

Yes, you can use the `--new` flag to call the `image.py` script with the newly created post. You can modify the `move_and_process_posts` function in `newpost.py` to include the `--new` flag when calling `image.py`:

```
pythonCopy codedef move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
    while True:
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
                print(f"Running image.py for {file}...")
                os.system(f"python {photo_script_path} --new")

        # Wait for 5 seconds before checking for new files again
        time.sleep(5)

```

This will call `image.py` with the `--new` flag for each newly created post in the source directory.
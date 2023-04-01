---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Jekyll\
  \ Workflow File Location.mp3\" type=\"audio/mpeg\">\n              Your browser\
  \ does not support the audio element.\n            </audio>\n            "
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
title: Jekyll Workflow File Location
---
Where do i put the google actions workflow yaml code


To create a GitHub Actions workflow, you need to add the YAML code in a specific file within your Jekyll repository on GitHub. Follow these steps:

1.  In your Jekyll repository, create a new folder named `.github` (if it doesn't already exist) at the root level. Inside the `.github` folder, create another folder called `workflows`.
    
2.  Now, create a new file inside the `workflows` folder, and give it a descriptive name, such as `jekyll_deploy.yml`. You can create this file directly on GitHub or using your preferred code editor and then push it to your repository.
    
3.  Copy the provided YAML code for the GitHub Actions workflow (from the previous answer) and paste it into the `jekyll_deploy.yml` file. Save the file and commit the changes.
    

Your folder structure should look like this:

```
pythonCopy codeyour-jekyll-repo/
│
├── .github/
│   └── workflows/
│       └── jekyll_deploy.yml
│
├── _posts/
├── _layouts/
├── _config.yml
...

```

Once you've set up the workflow file in your repository, GitHub Actions will automatically start running the workflow whenever you push to the specified branch (in the provided example, it's the `master` branch). Make sure to adjust the YAML file to match your specific deployment and hosting requirements.
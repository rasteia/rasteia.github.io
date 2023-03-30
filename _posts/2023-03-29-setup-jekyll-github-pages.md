---
layout: post
title: "Setting Up a Site Hosted with GitHub Pages"
date: 2023-03-27
categories: jekyll github-pages
image: /assets/images/cpunk1.jfif
categories:
  - AI
  - tutorial
  - jekyll
  - site
tags:
  - categories
  - AI
  - tutorial
  - jekyll
  - site
---

<audio controls>
  <source src="/assets/audio/jekyll.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

If you want to set up a site hosted with GitHub Pages using Jekyll and Git, here are the steps you should follow:

1. Create a new repository on GitHub with the name `<your-github-username>.github.io`. This will be the repository that GitHub Pages uses to host your site.

2. Clone the repository to your local machine using the following command in your terminal:
```bash
git clone https://github.com/<your-github-username>/<your-github-username>.github.io.git
```

3. Create a new Jekyll site using the following command:

```bash
jekyll new .
```

This will create a new Jekyll site in the current directory.

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

5. Configure your GitHub Pages settings by going to the Settings tab in your repository, scrolling down to the GitHub Pages section, and selecting the main branch as the source.

6. Your site is now live at `<your-github-username>.github.io`! You can start customizing it by editing the files in your Jekyll site, committing your changes, and pushing them to the main branch of your repository.
Save this as a Markdown file with a filename in the format yyyy-mm-dd-setting-up-a-site-hosted-with-github-pages.md, and place it in your Jekyll _posts directory. Then, when you build your Jekyll site, this post will be included and published as a blog post on your site.
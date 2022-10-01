---
title: "Angular to GitHub Pages"
date: 2022-08-15
lastmod: 2022-08-15
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Deploying an application"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Angular", "Github Pages", "Host", "Github", "File Name Too Long"]
toc:
  enable: false
zhtw: false
---

![](https://miro.medium.com/max/1400/0*X1agMlR53hFryDvs)

Photo by  [Lautaro Andreani](https://unsplash.com/es/@lautaroandreani?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# Deploying an application

Run you project locally by

-   Download the source code from your StackBlitz project by clicking the  `Download Project`  icon in the left menu, across from  `Project`, to download your project as a zip archive.

or

-   Clone your Project from GitHub.

To run your project locally, you need the following installed on your computer:

-   [Node.js](https://nodejs.org/en).
-   The  [Angular CLI](https://cli.angular.io/). From the terminal, install the Angular CLI globally with:

npm install -g @angular/cli

then  `cd`  to your project
```
cd angular-ynqttp
```
To download and install npm packages, use the following npm CLI command:
```
npm install
```
Use the following CLI command to run your application locally:
```
ng serve
```
[Angular — Deploying an application](https://angular.io/start/start-deployment#building-and-hosting-your-application)

To build your application for production, use the  `build`  command. By default, this command uses the  `production`  build configuration.

[Easy Steps to Host an Angular App in GitHub Pages | Syncfusion Blogs](https://www.syncfusion.com/blogs/post/easy-steps-to-host-an-angular-app-in-github-pages.aspx)

In our case, the name of the repository I created is angular-app, so the command will be:
```
ng build --output-path docs --base-href /angular-app/
```
The output path is given as  **docs**  since we know GitHub Pages look for files in two folders,  **root**  and  **docs**. In  **root**  we have all other app data, so we can’t use it here. Instead, we have given a separate output folder named  **docs**  that we are going to use to host in GitHub Pages.

The **base-href**  is an important argument since we use it to set the base path for resolving relative URLs to stylesheets, scripts, and many other resources.

# How to solve “filename too long” error in git (Powershell and GitHub Application) for windows
```
error: lstat("node_modules/webdriver-js-extender/built/built/built/built/built/built/built/built/built/built/built/built/built/built/built/spec/command_tests/totally_real_apk.apk"): Filename too long
```
Open the  **Github Powershell**  or  **cmd.exe**  or  **Git Bash**(you need to have git as an environment variable) and execute the  [following command](https://ourcodeworld.com/articles/read/109/how-to-solve-filename-too-long-error-in-git-powershell-and-github-application-for-windows)  :
```
git config --system core.longpaths true
```
In my experience, you may be facing the issue:

> error: could not lock config file C:/Users/.gitconfig: Permission denied

You need to go the folder of Git Bash and check the  **Run this program as an administrator.**

![](https://miro.medium.com/max/1400/1*AOpUk3-pS-jeMF9ghpPdNg.png)

Then open  `Git Bash`  directly (not from  `cmd` or  `poershell` etc.) and type in  `git config — system core.longpaths true`  again.

The  `core.longpaths`  sould has been set to  `True`  .

Then you’re good to commit again:

`git add .`

`git commit`

in  [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor))  interface:

-   Type the subject of your commit on the first line. Remember to keep it short (not more than 50 characters). Leave a blank line after.
-   Write a detailed description of what happened in the committed change. Use multiple paragraphs and bullet points to give a detailed breakdown. Don’t write everything out on one line, instead, wrap text at 72 characters.
- [Press `Esc` and then type `:wq` to save and exit.](https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791)

`git push`

# Final and Example

[chienhsiang-hung/Getting-started-with-Angular: Created with StackBlitz ⚡️ (github.com)](https://github.com/chienhsiang-hung/Getting-started-with-Angular)

[Angular Getting Started (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/Getting-started-with-Angular/)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)
# Django SNS Toy Project

> This project is my Social Network Service toy project by Django.<br>
> In making this project, I was able to practice of Django to deal with it's framwork some well.<br>
> Beside this projcet, Furthermore, I would be some study with considering to qeury performance optimization like select or prefetched relation features.<br>
> And, Applying front-end framework like React to cool webpage, It is so nice and interesting one.<br>


## Contents
> 1. Project set-up
> 2. Project structure
> 3. Features
> 4. Webpage examples images

<br>

## 1. Project set-up
- IDE : **pycharm**(professional)
- Python version control manager : **pyenv** (python version 3.10)
- Dependency control manager : **poetry**
- Database : **sqlite3**(for the purpose of toy project)

<br>

## 2. Project structure
- project root
  - .git
  - poetry file
  - **src**
      - config (django project configuration files, ex. settings, urls etc.)
      - static
      - media
      - templates
      - accounts (Accounts App)
      - posts (Posting App)

  <br>

  ## 3. Features

  1. User Accounts
    - signup
    - login / logout
    - user profile image
    - edit user info  (editting posting is permitted by posting owner)
    - password change

  2. Posting
    - posting CRUD
    - posting tagging system (using 'taggit' library)
    - posting list by user and tag (with query string, ex. posts/?username=Hongildong&tag=바다)

  <br>

  

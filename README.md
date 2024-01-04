# 💻**Django SNS Toy Project**

This project is my Social Network Service toy project by Django.
In making this project, I was able to practice of Django to deal with it's framwork some well.<br>
Beside this projcet, Furthermore, I would be some study with considering to qeury performance optimization like select or prefetched relation features.<br>
And, Applying front-end framework like React to cool webpage, It is so nice and interesting one.<br>

<br>

### Contents
> 1. Project Set-up
> 2. Project Structure
> 3. Features
> 4. Some Logics Considered
> 5. Image Examples of Website

<br>

---

<br>

## 1. Project Set-up
- IDE : **pycharm**(professional)
- Python version control manager : **pyenv** (python version 3.10)
- Dependency control manager : **poetry**
- Database : **sqlite3**(for the purpose of toy project)

<br>

## 2. Project Structure
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

1. **User Accounts**
    - signup
    - login / logout
    - user profile image
    - edit user info  (editting posting is permitted by posting owner)
    - password change

<br>

2. **Posting**
    - posting CRUD
    - posting tagging system (using 'taggit' library)
    - posting list by user and tag (with query string, ex. posts/?username=Hongildong&tag=바다)

<br>

## 4. Some logics considered

1. **How to implement posting list by user or tag?**
  - I implements this, by URL query string. And override `get_queryset` in `ListTempleteView`
  - Through this, I can be to improve list template reusability.

// In PostListView
```
    def get_queryset(self):
        qs = super().get_queryset()
        username = self.request.GET.get('username')
        tag = self.request.GET.get('tag')
        print(tag)
        if username:
            qs = qs.filter(author__username=username)
            print(qs)
            if tag:
                qs = qs.filter(tags__name__in=[tag])
                print(tag)
            return qs
        return qs
```

2. **How to implement tag searching system?**
  - The models relations like,  `User` 1---N `Post` M---N `tags`.
  - I add function to `User` model to collecting all one users tags.

 // In User model
```
    def get_tags_all(self):
        tags_counter = defaultdict(int)
        for post in list(self.post_set.all()):
            tags = post.tags.all()
            for tag in tags:
                tags_counter[tag] += 1
        return tags_counter.items()
```  

## 5. Image Examples of Website
<details>
  <summary>Login page</summary>

  <img width="1198" alt="image" src="https://github.com/Kwon-sang/sns_prorject/assets/115248448/e035989d-6d0f-4d9f-99a8-3e5855bf32f6">
</details>

<details>
  <summary>Main page (After login) </summary>

  <img width="1199" alt="image" src="https://github.com/Kwon-sang/sns_prorject/assets/115248448/ed4dd767-ed2e-429a-a24e-1af4c8df98dc">
</details>

<details>
  <summary>Posting list page by User  (click to myname at top of page or posting user) </summary>

  <img width="1198" alt="image" src="https://github.com/Kwon-sang/sns_prorject/assets/115248448/1cdbbaf2-8b72-477c-92ea-33b1bc44a412">
</details>

<details>
  <summary>Posting list page by My Tag (click to sidebars tag) </summary>

  <img width="1199" alt="image" src="https://github.com/Kwon-sang/sns_prorject/assets/115248448/3555919c-bc81-4f3f-9cb4-e46d80bda349">
</details>

<details>
  <summary>Posting delete (This button showed only posting owner) </summary>

  <img width="1199" alt="image" src="https://github.com/Kwon-sang/sns_prorject/assets/115248448/77c044e9-d7e3-4589-ba74-bd7b1f21265d">
</details>

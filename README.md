# Django Persian documnetation

### FAQ:
- What exactly is this project?
  - This project is Persian translation of Django documentation.
- Which version of Django is the documentation for?
  - Currently Django 3.2.
- Do I need to know Sphinx to contribute?
  - In fact, you need very little knowledge in Sphinx to change the design of pages, but understanding the mechanism doesn't require background knowledge and in this level it's very simple.
- How I can help this project?
  - This project requires translation and front design for pages. Your knowledge in these fields will help the project. 
- Is there online resource of Django Persian documentation?
  - No, at the moment, the project is under development, it doesn't have an online source and only the offline project can be used

### Basic and simple project information:
  - The documentation is based on the latest LTS version of Django, which is currently **[3.2](https://github.com/django/django/tree/stable/3.2.x)** and this project is a translation of the docs that exist **[Here](https://docs.djangoproject.com/en/3.2/)**.
The full content of the documentation can also be viewed **[Here](https://docs.djangoproject.com/en/3.2/contents/)**  
  
  - **Steps to get things ready:**  
    * First of all, download this repo through the Git or this [link](https://github.com/amirilf/DjangoPersianDocumentation/archive/refs/heads/main.zip)
    * To work with it, you need to download Django 3.2 repository, which can be downloaded through this **[link](https://github.com/django/django/archive/refs/heads/stable/3.2.x.zip)** (It's about 14.3 MB ,make sure you download the repository version 3.2).
    * In the Django 3.2 repository folder, rename the `docs` folder to `django-docs` and copy that to the project folder which is `DjangoPersianDocumentation` (if you downloaded this repo via the link, there is probably a branch name at the end of the folder name, which you can change it to `DjangoPersianDocumentation` or continue anyway).
    * You no longer need the Django 3.2 repository folder so you can delete it (we only needed the `docs` folder)
    * Generally, we have a `django-docs` and `local-docs` folders in our project, the first one contains the original files of django-docs and the second one is the result of changes of our project. so by default these values are placed in the `local-project-creator.py` and `.gitignore` files. If you want to change their names (it's recommended not to change their names), you must also change the names in the `local-project-creator.py` and `.gitignore` files.
    * The project tree structure looks something like this:
      * DjangoPersianDocumentation  
        |- django-docs/ (ignored by .gitignore)  
        |- docs/  
        |- local-docs/ (ignored by .gitignore)  
        |- .gitignore  
        |- local-project-creator.py  
        |- ...
    * Our `local-docs` folder hasn't been created yet, and we need to apply the latest update of our project (`docs`) to `django-docs` then we can work with it. To create it, just run the `local-project-creator.py` module to create `local-docs`. Note that the default values in this file are `django-docs`,`docs` and `local-docs`. 

    * After doing the steps above, just enter the `local-docs` folder, run the `make.bat html` command to create html files from raw files. After a while, you can see that a folder called `_build` has been created. Inside that folder, you can see the `html` folder, which contains the project html files.
    * Just open index.html and see the result

### How to change and translate files?
  * Just translate the text files and then run the `make.bat html` command to make the project changes and you can see the new result again.
  * Finally, you can put the edited files with the same path structure in the `docs` folder of the project to save the changes.
  
   
<br>
Have a nice day 💗









<p align="center">
  <img src="https://repository-images.githubusercontent.com/450027908/72795f16-1b71-41f7-b00f-8a06822d520f" alt="DjPrDoc" width="30%">
  <p align="center">
  <b>
    Django Persian Documentation 
   </b>
  </p>
  <hr>
</p>

### FAQ:
- What exactly is this project?
  - This project is Persian translation of Django documentation.
- Which version of Django is the documentation for?
  - Currently Django 3.2.
- How I can help this project?
  - This project requires translation and front design for pages. Your knowledge in these fields will help the project. 
- Do I need to know Sphinx to contribute?
  - For translation you only need to replace the translated lines in the files and it doesn't require knowing the Sphinx at all, but for designing you need very little knowledge in Sphinx to change the design of pages, and understanding the mechanism doesn't require background knowledge and in this level it's very simple.
- Is the project available online?
  - No, at the moment, the project is under development, and only the offline project can be used. After the development of each general part, the project will be available online.

### Basic and simple project information:
  - The documentation is based on the latest LTS version of Django, which is currently **[3.2](https://github.com/django/django/tree/stable/3.2.x)** and this project is a translation of the docs that exist **[Here](https://docs.djangoproject.com/en/3.2/)**.
The full content of the documentation can also be viewed **[Here](https://docs.djangoproject.com/en/3.2/contents/)**  
  
  - **Steps to get things ready:**  
    * First of all, download this repo through the Git or this **[link](https://github.com/amirilf/DjangoPersianDocumentation/archive/refs/heads/main.zip)**
    * To work with it, you need to download Django 3.2 repository, which can be downloaded through this **[link](https://github.com/django/django/archive/refs/heads/stable/3.2.x.zip)** (It's about 14.3 MB, make sure you've downloaded version 3.2 of the repository).

    * In the Django 3.2 repository folder, rename the `docs` folder to `django-docs` and copy that to the project folder which is `DjangoPersianDocumentation` (if you downloaded this repo via the link, there is probably a branch name at the end of the folder name, which you can change it to `DjangoPersianDocumentation` or continue anyway).
    * You no longer need the Django 3.2 repository folder so you can delete it (we only needed the `docs` folder)
    * Generally, we have a `django-docs` and `local-docs` folders in our project, the first one contains the original files of Django documentation and the second one is the result of changes of our project. So by default these values are placed in the `local-project-creator.py` and `.gitignore` files. If you want to change their names (it's recommended not to change their names), you must also change the names in the `local-project-creator.py` and `.gitignore` files.
    * Our `local-docs` folder hasn't been created yet, and we need to merge the latest update of our project (`docs`) to `django-docs` then we can work with it. So just run the `local-project-creator.py` module to create `local-docs`. Note that the default values in this file are `django-docs`,`docs` and `local-docs`. 
    * After running the `local-project-creator.py`, project tree structure looks something like this:
      * DjangoPersianDocumentation  
        |- django-docs/ (ignored by .gitignore)  
        |- docs/  
        |- local-docs/ (ignored by .gitignore)  
        |- .gitignore  
        |- local-project-creator.py  
        |- ...
    * To work with documentation, you must install the Sphinx requirements. So first create your virtual environment and activate it (**[See how to do it](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)**, It's recommended to name your virtual environment `env`), and then install the project requirements with `pip install -r requirements.txt` command.

    * After doing the steps above, just enter the `local-docs` folder, run the `make.bat html` (or `make html`) command to create html files from raw files. After a while, you can see that a folder called `_build` has been created. Inside that folder, you can see the `html` folder, which contains the project html files.
    * Just open index.html and see the result

### How to change and translate files?
  * After making changes just run the `make.bat html` (or `make html`) command to merge changes and you can see the new result again.
  * Finally, put the edited files with the same path structure (e.g. if you changed in the `docs` folder of the project to save the changes.
<br>
Have a nice day 💗

# Algorithm and DS portal 
![](artwork/rect_banner.png)

>Algorithm and Data Structure server provides graphql API for algods portal [WIP] 

### First Setup
> this project depends on [Algopack-api](https://github.com/Aniket965/AlgoPack-api) 
 
####  Setup
 - Install dependencies ``` pip install -r requirements/dev.txt ```
 - Install Algopack-Api ``` npm install algopack -g ```
 - Build api in root folder ``` algopack build ```
 - Setup database from api ``` python create_db_from_repo.py ```

or just Run ```./setup.sh ```

### Run Project
``` python manage.py  runserver ```
- Goto [localhost:8000/graphql](http://127.0.0.1:8000/graphql) to try api.
- Intial run
    - ``` python manage.py makemigrations```
    - ``` python manage.py migrate```
    - ``` python manage.py run server```

Related Projects
- [Algo_ds_notes](https://github.com/jainaman224/Algo_Ds_Notes)
- [Algopack-api](https://github.com/Aniket965/AlgoPack-api)
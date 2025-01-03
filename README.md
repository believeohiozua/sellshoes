# sellshoes
An E-commerce poject 

- ![PIPELINE CHECKS](https://github.com/believeohiozua/sellshoes/actions/workflows/cicd.yml/badge.svg?branch=main)


## Docker Setup
- build the docker images by running `docker compose build` in the root directory
- start the application by running `docker compose up` in the root directory
- The application will be available at `http://127.0.0.1:8000`
- To run django management commands, run `docker compose exec api python manage.py <command>`
- or open the bash shell by running `docker compose exec api bash` and run the commands directly 
- to shutdown the application, run `docker compose down`
- to run tests, run `docker compose exec api python manage.py test`

- To run api test with semathesis 
```bash
    docker compose exec api schemathesis run http://127.0.0.1:8000/test/swagger.json -v
```

#### Postgress to workbench
- To connect to the postgres database from docker to the workbench
    - `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id` to get the ip address of the container
    - then use the connection string `postgres://dbuser:password@<container_ip>:5432/sellshoesdb` to connect to the database
- Or use the pgadmin configured in the docker-compose file to connect to pgadmin on your browser by following the example in this [video](https://www.youtube.com/watch?v=t8tIA1_CT_Q)



## Base setup
- To run this project as a base django app:
    - `echo 'DATABASE_URL="sqlite:///db.sqlite3"' >> ./sellshoes/.env` [make sure your db.sqlite3 is in the project root directory]
    - `poetry shell` to activate the virtual environment
    - `poetry install` to install the dependencies [This can be done just once per time]
    - `python manage.py migrate` to apply the migrations
    - `python manage.py runserver` to start the server
    - `python manage.py createsuperuser` to create a super user
    - `poetry add <package_name>` to add a new package to the project
    - `poetry remove <package_name>` to remove a package from the project
    - `pytest -v` to run the tests
    - `schemathesis run http://127.0.0.1:8000/test/swagger.json -v` to run the api tests with schemathesis




- Tasks: all tasks are in the [Tasks](./Tasks) folder.


## Technologies
* [Python](https://www.python.org/) : Programming language used for the application
* [postgres:13-alpine] (https://hub.docker.com/_/postgres) : Database used for the application
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration
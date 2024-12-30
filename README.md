# sellshoes
An E-commerce poject 

- ![PIPELINE CHECKS](https://github.com/believeohiozua/sellshoes/actions/workflows/cicd.yml/badge.svg?branch=main)


## Project Setup
- build the docker images by running `docker compose build` in the root directory
- start the application by running `docker compose up` in the root directory
- The application will be available at `http://127.0.0.1:8000`
- To run django management commands, run `docker compose exec api python manage.py <command>`
- or open the bash shell by running `docker compose exec api bash` and run the commands directly 
- to shutdown the application, run `docker compose down`
- to run tests, run `docker compose exec api python manage.py test`

- To run api test with semathesis 
```bash
    docker compose exec api schemathesis run https://127.0.0.1:8000/test/swagger.json --request-tls-verify=false -v
```

#### Postgress to workbench
- To connect to the postgres database from docker to the workbench
    - `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id` to get the ip address of the container
    - then use the connection string `postgres://dbuser:password@<container_ip>:5432/sellshoesdb` to connect to the database
- Or use the pgadmin configured in the docker-compose file to connect to pgadmin on your browser by following the example in this [video](https://www.youtube.com/watch?v=t8tIA1_CT_Q)


- Tasks: all tasks are in the [Tasks](./Tasks) folder.
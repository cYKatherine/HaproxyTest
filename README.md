# How to run it
## Create docker network:
```
$ docker network create nginx-kat
```

## Run the main application first:
```
$ cd flask_application
$ docker build -t flask-app .
$ docker run --name flask1 -it -p 27015:27015 -d --network nginx-kat main-flask-app
```

## Run the mirror application (continued from the previous steps):
```
$ docker run --name flask2 -it -p 27016:27015 -d --network nginx-kat main-flask-app
```

## Finally spin up Nginx:
```
$ cd ..
$ docker build -t custom-nginx .
$ docker run --name nginx-test-kat -d -p 8180:80 --network nginx-kat custom-nginx
```
## Notes
* Make sure to run `docker ps` to confirm the containers were spinned up properly and running.
* If the container does not run, try `docker logs [container name]` to investigate.
* `-p 8180:80` does port forwarding, which maps the localhost 8180 to docker port 80.
* When running the main application, `-p 27015:27015` maps localhost 27015 to docker port 27015
    * Docker port 27015 is defined in `/flask_application/Dockerfile`.
    * `EXPOSE 27015` allows the external traffic (outside docker) to access the 27015 port inside docker.
    * The 27015 in `CMD [ "flask", "run","--host","0.0.0.0","--port","27015"]` command runs the flask application on 27015 inside docker.
* The flask program simply counts and display the number of requests that hit the server.

# How to test it
* Go to localhost:8081, and hit the endpoint 10 times
* Go to localhost:27015 (the main server), should see number 11
* Go to localhost:27016 (the mirror server), should see number 11 (depending on the settings of Nginx)
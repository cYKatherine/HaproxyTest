# Preparation
Install `haproxy`:

`brew install haproxy`

# How to run it
First activate the virtual environment:

`. venv/bin/activate`

Then open two terminal and run:

`flask --app main run --port=27015` and `flask --app mirror run --port=27016`

Build `Dockerfile`

```
docker build -t my-haproxy .
docker run -it --rm --name haproxy-syntax-check my-haproxy haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg
```
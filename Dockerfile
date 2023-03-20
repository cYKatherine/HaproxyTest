FROM production.docker.adsrvr.org/ttd-hpc/haproxy-local-reverse-proxy/base:1.4.0

COPY ./mirror.cfg /etc/haproxy/mirror.cfg
COPY ./main.cfg /usr/local/etc/haproxy/haproxy.cfg

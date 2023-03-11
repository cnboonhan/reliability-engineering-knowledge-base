FROM registry.hub.docker.com/jupyter/minimal-notebook:latest

USER 0
RUN apt update
RUN apt install pgbadger python3 python3-pip postgresql-client -y

RUN chgrp -Rf root /home/$NB_USER && chmod -Rf g+w /home/$NB_USER
USER 1000

ENV NOTEBOOK_ARGS="--ServerApp.password='' --ServerApp.token=''"

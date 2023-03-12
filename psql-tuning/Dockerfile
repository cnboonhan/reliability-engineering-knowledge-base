FROM registry.hub.docker.com/jupyter/minimal-notebook:latest

USER 0
RUN apt update
RUN apt install pgbadger python3 python3-pip postgresql-client -y
RUN pip3 install faker psycopg2-binary tqdm

RUN chgrp -Rf root /home/$NB_USER && chmod -Rf g+w /home/$NB_USER
USER 1000

RUN echo 'PGPASSWORD=$POSTGRESQL_PASSWORD psql -U $POSTGRESQL_USER -h $POSTGRESQL_HOSTNAME' >> /home/$NB_USER/.bashrc

COPY notebooks/ /home/$NB_USER/notebooks/

ENV NOTEBOOK_ARGS="--ServerApp.password='' --ServerApp.token='' --ServerApp.ip='0.0.0.0' --ServerApp.root_dir='/var/lib/pgsql/data'"

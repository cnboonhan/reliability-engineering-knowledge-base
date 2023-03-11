FROM registry.hub.docker.com/library/ubuntu:latest

RUN apt update
RUN apt install pgbadger python3 python3-pip -y
RUN pip3 install jupyterlab

CMD [ "jupyter-lab", "--ip", "0.0.0.0", "--port", "8899", "--allow-root" , "--ServerApp.password=''", "--ServerApp.token=''", "--notebook-dir='/root'" ]

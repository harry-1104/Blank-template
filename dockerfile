FROM ubuntu
RUN apt update -y && apt install -y firefox
RUN snap install firefox
CMD firefox
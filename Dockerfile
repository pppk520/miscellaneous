FROM python:3.5

# from build-arg
ARG ARG_GOPARDIR
ARG ARG_GOROOT
ARG ARG_GOPATH

ENV GOPARDIR ${ARG_GOPARDIR}
ENV GOROOT ${ARG_GOROOT}
ENV GOPATH ${ARG_GOPATH}
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH

RUN env

RUN apt-get update

# python environment
RUN pip install pip==9.0.1

# dependencies
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# gophernotes dependencies
RUN apt-get install -y libzmq3-dev

# golang & gophernotes jupyter kernel
RUN mkdir -p ${ARG_GOPARDIR}
COPY install-go.sh /tmp/
RUN /bin/bash /tmp/install-go.sh

# install vim
RUN apt-get install -y vim
RUN apt-get install -y psmisc

COPY .vimrc /root

CMD ["/bin/bash"]

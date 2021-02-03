FROM ubuntu:18.04
MAINTAINER ivangtorre <igonzalez@vicomtech.org>

RUN apt-get update && \
    apt-get install -y \
        libportaudio2 \
        libportaudiocpp0 \
        libsndfile1-dev \
        portaudio19-dev \
        python3 \
        python3-dev \
        python3-pip

RUN pip3 install pyaudio

WORKDIR /workdir

COPY . .





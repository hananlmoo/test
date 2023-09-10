FROM python:3.8.16-slim-buster AS BASE

RUN apt-get update \
      && apt-get --assume-yes --no-install-recommends install \
      build-essential \
      curl \
      git \
      jq \
      libgomp1 \
      vim 

WORKDIR /app
RUN pip install plotly
RUN pip install pygame
RUN pip install pyopengl
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get install -y libgl1-mesa-dev libosmesa6-dev
# Upgrade pip version
RUN pip install --no-cache-dir --upgrade pip

# Install Rasa version 3.5.10
RUN pip install --no-cache-dir rasa

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml

CMD ["rasa", "run"]

FROM python:3.9

# Or your actual UID, GID on Linux if not the default 1000
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create user
RUN groupadd --gid $USER_GID $USERNAME
RUN useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

# Install software
RUN apt update
RUN apt install -y nodejs npm
RUN npm install -g less

# Install additional packages
RUN apt-get update && apt-get install -y fonts-liberation fonts-crosextra-carlito fonts-cabin fonts-roboto imagemagick poppler-utils tidy
RUN apt-get upgrade -y 

# install additional fonts
COPY fonts/**.zip .
RUN unzip JetBrainsMono-1.0.0.zip
RUN unzip open-sans.zip
RUN unzip Kalam.zip
RUN unzip -o open-sans-condensed.zip
RUN mv *.ttf /usr/share/fonts/
RUN fc-cache

# Install packages
ADD requirements.txt /
RUN pip install -r /requirements.txt
RUN rm /requirements.txt

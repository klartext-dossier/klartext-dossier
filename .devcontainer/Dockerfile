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
RUN apt install curl
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt install -y nodejs
RUN npm install -g less

# Install latest chrome dev package and fonts to support major charsets (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)
RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
      --no-install-recommends 

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

# Provide Documentation Generation
RUN npm install --global yarn 
RUN mkdir -p /opt/npm/node_modules/.bin
ENV PATH="/opt/npm/node_modules/.bin/:${PATH}"
RUN cd /opt/npm && yarn add @mermaid-js/mermaid-cli

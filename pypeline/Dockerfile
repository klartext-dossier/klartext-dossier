FROM python:3.12

# Or your actual UID, GID on Linux if not the default 1000
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create users
RUN groupadd --gid $USER_GID $USERNAME
RUN useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

# Install software
RUN apt update
RUN apt install -y curl
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
RUN apt-get install -y fonts-jetbrains-mono fonts-open-sans
RUN wget -q https://github.com/google/fonts/blob/main/ofl/kalam/Kalam-Bold.ttf https://github.com/google/fonts/blob/main/ofl/kalam/Kalam-Light.ttf https://github.com/google/fonts/blob/main/ofl/kalam/Kalam-Regular.ttf
RUN mv *.ttf /usr/share/fonts/
RUN fc-cache

# Install packages
RUN pip install --upgrade pip
ADD requirements.txt /
RUN pip install -r /requirements.txt
RUN rm /requirements.txt

# Provide documentation generation
RUN corepack enable
RUN mkdir -p /opt/npm/node_modules/.bin
ENV PATH="/opt/npm/node_modules/.bin/:${PATH}"
RUN npm install -g puppeteer @mermaid-js/mermaid-cli
RUN chmod -R u+rwX,g+rX,o+rX /root
ENV PUPPETEER_CACHE_DIR="/root/.cache/puppeteer"

# Install klartext_pygments
ARG KLARTEXT_PYGMENTS_VERSION=0.1.0
ADD klartext_pygments-$KLARTEXT_PYGMENTS_VERSION-py2.py3-none-any.whl /
RUN pip install klartext_pygments-$KLARTEXT_PYGMENTS_VERSION-py2.py3-none-any.whl
RUN rm /*.whl
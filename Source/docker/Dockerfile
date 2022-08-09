FROM emhaka/pypeline:latest

ARG DOSSIER_VERSION=0.1.0

ADD wheels/dossier-$DOSSIER_VERSION-py3-none-any.whl /
RUN pip install dossier-$DOSSIER_VERSION-py3-none-any.whl
RUN rm /dossier-$DOSSIER_VERSION-py3-none-any.whl

FROM emhaka/pypeline:latest

ARG KLARTEXT_VERSION=0.1.0
ARG MDX_VERSION=0.1.0
ARG DOSSIER_VERSION=0.1.0

ADD klartext/dist/*.whl dossier-mdx/dist/*.whl dossier/dist/*.whl /
RUN pip install klartext-$KLARTEXT_VERSION-py3-none-any.whl dossier-mdx-$MDX_VERSION-py3-none-any.whl dossier-$DOSSIER_VERSION-py3-none-any.whl
RUN rm /*.whl

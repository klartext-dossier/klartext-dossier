FROM emhaka/pypeline:latest

ARG KLARTEXT_VERSION=0.1.0
ARG MDX_VERSION=0.1.0
ARG DOSSIER_VERSION=0.1.0

ADD klartext/dist/*.whl mdx/dist/*.whl dossier/dist/*.whl /
RUN pip install klartext/dist/klartext-$KLARTEXT_VERSION-py3-none-any.whl mdx/dist/mdx-$MDX_VERSION-py3-none-any.whl dossier/dist/dossier-$DOSSIER_VERSION-py3-none-any.whl
RUN rm /*.whl

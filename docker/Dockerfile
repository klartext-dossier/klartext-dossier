FROM klartext/pypeline:latest

ARG KLARTEXT_VERSION=0.1.0
ARG KLARTEXT_PYGMENTS_VERSION=0.1.0
ARG MDX_VERSION=0.1.0
ARG DOSSIER_VERSION=0.1.0

ADD klartext/dist/*.whl klartext-pygments/dist/*.whl mdx/dist/*.whl dossier/dist/*.whl /
RUN pip install --force-reinstall klartext-$KLARTEXT_VERSION-py3-none-any.whl klartext_pygments-$KLARTEXT_PYGMENTS_VERSION-py3-none-any.whl dossier_mdx-$MDX_VERSION-py3-none-any.whl dossier-$DOSSIER_VERSION-py3-none-any.whl
RUN rm /*.whl

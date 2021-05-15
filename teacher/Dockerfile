FROM jupyter/base-notebook

# Install nbgrader
RUN pip3 install nbgrader nose
RUN jupyter nbextension install --sys-prefix --py nbgrader --overwrite
RUN jupyter nbextension enable --sys-prefix --py nbgrader
RUN jupyter serverextension enable --sys-prefix --py nbgrader

WORKDIR /assignments

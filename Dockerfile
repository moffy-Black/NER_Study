FROM python:3.8
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN apt-get install -y libhdf5-dev
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pymagnitude
RUN pip install magnitude
RUN pip install torch
RUN pip install sudachipy
RUN pip install sudachidict_core
RUN pip install pandas
RUN pip install numpy
# RUN pip install spacy-streamlit
# RUN pip install spacy[ja]
# RUN pip install gensim
# RUN python -m spacy download ja_core_news_md
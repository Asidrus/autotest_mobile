FROM continuumio/miniconda3
WORKDIR /app/autotest/
RUN mkdir ../allure-results ../logs ../cache
COPY req.yml ./
RUN conda env create -f req.yml
RUN echo "source activate autotest" > ~/.bashrc
ENV PATH /opt/conda/envs/autotest/bin:$PATH
COPY . .
FROM python:3.4

ADD . /src
WORKDIR /src
RUN python setup.py install
CMD ["python", "test-script.py"]

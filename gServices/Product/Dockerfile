FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/app

RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

CMD ["python", "./app/server.py"]
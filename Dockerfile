FROM python:3.11

ARG run_env=development
ENV env $run_env

WORKDIR /lesson/test

COPY ./requirements.txt /lesson/test/requirements.txt
RUN pip install -r /lesson/test/requirements.txt

COPY . /lesson/test

CMD pytest -m "$env" -s -v tests/

#docker build -t automation_tests .
#docker run automation_tests

#docker build --build-arg env=development -t automation_tests .
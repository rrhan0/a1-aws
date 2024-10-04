FROM public.ecr.aws/lambda/python:3.8

COPY stats.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "stats.lambda_handler" ]
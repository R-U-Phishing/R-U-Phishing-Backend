FROM public.ecr.aws/lambda/python:3.7

WORKDIR ${LAMBDA_TASK_ROOT}

COPY ./Total_URL/* .

RUN pip3 install -r requirements.txt

CMD [ "lambda_function.lambda_handler" ]
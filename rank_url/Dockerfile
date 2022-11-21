FROM public.ecr.aws/lambda/python:3.7

COPY Rank_URL/ ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.

RUN  pip3 install pymysql

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.lambda_handler" ] 

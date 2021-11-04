# The AWS base images provide the following environment variables:
# - LAMBDA_TASK_ROOT=/var/task
# - LAMBDA_RUNTIME_DIR=/var/runtime
ARG HANDLER="handler.py"

FROM public.ecr.aws/lambda/python:3.8

# Include global args in this stage of the build
ARG HANDLER
# Copy hanlder file
COPY ${HANDLER} ${LAMBDA_TASK_ROOT}

cmd [ "handler.handle" ]
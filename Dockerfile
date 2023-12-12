FROM python:3.10 as base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt #  To upgrade run: pip install --upgrade pip

COPY ./prisma /code/prisma

RUN prisma generate

FROM base as api

COPY ./services/trends /code/trends

WORKDIR /code/trends

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]

# CMD ["curl", "-0", "0.0.0.0:8888/openapi.json", ">>", "openapi/openapi.json"]

FROM base as tiktok-worker

COPY ./workers/tiktok /code/tiktok

WORKDIR /code/tiktok

CMD ["python", "main.py"]
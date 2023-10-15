FROM python:3.10-slim AS builder

WORKDIR /app
COPY src/ .
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

FROM python:3.10-slim AS deployer

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

WORKDIR /app
COPY src/ .

CMD [ "python", "main.py" ]


FROM python:3.11-slim
WORKDIR /app
COPY app/ .
RUN pip install flask pytz
ENTRYPOINT ["python", "main.py"]
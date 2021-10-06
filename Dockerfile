FROM python:3.7-bullseye
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . /app

CMD ["python", "app.py"]

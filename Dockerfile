FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . ./

EXPOSE 8000

CMD ["python3", "stripe_test/manage.py", "runserver", "0.0.0.0:8000"]

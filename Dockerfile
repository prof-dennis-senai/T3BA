FROM python:3.14

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app/SafeIndustry

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.9-slim

WORKDIR /django_env

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 8000
RUN python dummy_data.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

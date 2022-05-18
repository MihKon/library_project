FROM python:3.10.4-bullseye
WORKDIR /library_project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "8000"]

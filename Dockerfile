FROM python:3.8
WORKDIR /FastAPI-Sqlite3
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
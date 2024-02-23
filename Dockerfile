FROM python:3.8

EXPOSE 8080
WORKDIR /app

COPY . ./

RUN pip install -r requirements1.txt

ENTRYPOINT ["streamlit", "run", "genaidemo.py", "--server.port=8080", "--server.address=0.0.0.0"]

FROM python:3.9-alpine

#mkdir /app & cd /app
WORKDIR /app

#copy dependency files & directories:
COPY main.py .
COPY requirements.txt .
COPY utils.py .
COPY run.sh .

#copy directories :
COPY public public
COPY templates templates

RUN pip install -r requirements.txt

## ====Running

#set your env variables here :
ENV PORT=3000
ENV INSTANCE_NAME="dov bear"
ENV INSTANCE_HASH=abc123

EXPOSE ${PORT}

ENTRYPOINT ["python", "main.py"]

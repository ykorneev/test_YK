FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["putest", "/Users/yurakorneev/Documents/test_YK/tests"]



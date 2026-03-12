FROM python:3.11

WORKDIR /app

COPY . .

CMD ["python","map_port.py","192.168.1.235"]

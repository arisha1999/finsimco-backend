FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=.

# Убери эту строку, если она есть:
# ENTRYPOINT ["python", "app/main.py", "run"]

CMD [ "bash" ]
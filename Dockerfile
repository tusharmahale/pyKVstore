FROM python:3.8.5-slim

RUN mkdir -p /app/{src/templates,tests}
WORKDIR /app/src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY tests /app/tests
COPY src /app/src
COPY input.csv ./
RUN chmod 755 /app/src/*py /app/tests/*py /app/tests/*sh

CMD ["python", "app.py"]

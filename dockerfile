FROM python:3.11-slim

WORKDIR /app

COPY . .

CMD ["bash", "-c", "python -m unittest test/test_decorators.py && python main.py"]


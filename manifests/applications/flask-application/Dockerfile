FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Install additional utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client netcat-openbsd curl && \
    rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

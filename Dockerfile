FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY constraints.txt .

RUN pip install --upgrade pip \
 && pip install -r requirements.txt -c constraints.txt \
 && pip install --no-cache-dir opencv-python-headless==4.13.0.90

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

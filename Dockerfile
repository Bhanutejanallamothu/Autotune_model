FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=7860
ENV OPENCV_DISABLE_GUI=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip \
 && pip install torch fastapi uvicorn pillow python-multipart numpy pyyaml pydantic \
 && pip install --no-deps ultralytics \
 && pip install --no-cache-dir opencv-python-headless==4.13.0.90 \
 && pip uninstall -y opencv-python

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

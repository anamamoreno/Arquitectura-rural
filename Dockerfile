FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV READ_ONLY=true
ENV PYTHONUNBUFFERED=1

EXPOSE 8501

CMD ["sh", "-c", "streamlit run scripts/app_matriz_estandares.py \
    --server.port=8501 \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.baseUrlPath=/artefactos/viviendarural \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false \
    --browser.gatherUsageStats=false"]

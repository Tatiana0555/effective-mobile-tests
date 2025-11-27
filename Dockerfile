FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libgtk-3-0 \
    libgdk-pixbuf-2.0-0 \
    libx11-xcb1 \
    libxss1 \
    libdbus-1-3 \
    libgconf-2-4 \
    libatspi2.0-0 \
    libwayland-client0 \
    xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

COPY . .

CMD ["pytest", "-v"]

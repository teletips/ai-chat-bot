FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies (do this first for docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code
COPY . .

# Run your bot script
CMD ["python", "bot.py"]

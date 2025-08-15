FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    texlive \
    pandoc \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio port
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]

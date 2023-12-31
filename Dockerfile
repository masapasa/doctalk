# Using a slim version for a smaller base image
FROM python:3.11-slim-bullseye

# Install GEOS library, Rust, and other dependencies, then clean up
RUN apt-get update && apt-get install -y \
    git \
    libgeos-dev \
    pandoc \
    binutils \
    curl \
    build-essential && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

# Add Rust binaries to the PATH
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /code

# Copy just the requirements first
COPY ./requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Increase timeout to wait for the new installation
RUN pip install --no-cache-dir -r requirements.txt --timeout 200

# Copy the rest of the application cd backend && uvicorn main:app --reload --host 0.0.0.0 --port 5050 kill -9 $(lsof -ti tcp:5050)https://4218-3-253-139-8.ngrok-free.app
COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5050"]

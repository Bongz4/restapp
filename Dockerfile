# 1. Base image
FROM python:3.9

# 2. Set working directory
WORKDIR /code

# 3. Copy requirements
COPY requirements.txt /code/requirements.txt

# 4. Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 5. Copy app code
COPY ./app /code/app

# 6. Run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
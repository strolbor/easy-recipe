FROM python:3.7-slim

WORKDIR /etc/easyrecipe

COPY requirements.txt requirements.txt

##BUILD DEPENCIES
RUN apt update &&\
    apt install make automake gcc g++ subversion python3-dev ffmpeg libsm6 libxext6  -y && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt && \
    apt purge make automake gcc g++ subversion python3-dev -y && \
    rm -rf /var/cache/apk/*

# Copy App
COPY easy-recipe.py easy-recipe.py
COPY app/ app/
COPY instance/ instance/

EXPOSE 5000
CMD ["python3","easy-recipe.py"]
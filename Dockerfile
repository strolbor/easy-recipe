FROM python:alpine3.15

WORKDIR /etc/easyrecipe

COPY requirements.txt requirements.txt

##BUILD DEPENCIES
RUN apk update &&\
    apk add make automake gcc g++ subversion python3-dev && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt && \
    apk del make automake gcc g++ subversion python3-dev && \
    rm -rf /var/cache/apk/*

# Copy App
COPY easy-recipe.py easy-recipe.py
COPY app/ app/
COPY instance/ instance/

EXPOSE 5000
CMD ["python3","easy-recipe.py"]
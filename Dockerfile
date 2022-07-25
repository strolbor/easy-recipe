FROM python:alpine3.15

WORKDIR /etc/easyrecipe

##BUILD DEPENCIES
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
#RUN ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install --upgrade numpy

# PYthon Libs install
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze > req-now.txt

# Copy App
COPY easy-recipe.py easy-recipe.py
COPY app/ app/

EXPOSE 5000
CMD ["python3","easy-recipe.py"]
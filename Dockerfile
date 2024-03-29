# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

RUN apk update
RUN apk upgrade
RUN apk add --no-cache ffmpeg

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

EXPOSE 8080

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
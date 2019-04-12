FROM python:3.6.2

# set the work dir at /app
WORKDIR /app

# copy all files and put into the /app of docker container
ADD . /app

# install required packages
RUN pip install -r requirements.txt


# let port 80 accessible from outside
EXPOSE 80

# define env variable
ENV NAME World

# when docker running, do the command 'python app.py'
CMD ["python", "app.py"]
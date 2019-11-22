# BUILD
#  docker build --tag=my_flask_wsgi .
# 
# SEND TO DOCKERHUB
#  docker login
#  docker image ls
#  docker tag my_flask_wsgi nbianchi/my_flask_wsgi:latest
#  docker push nbianchi/my_flask_wsgi


FROM tiangolo/uwsgi-nginx-flask:python3.7
COPY . /app
WORKDIR /app

# RUN
#  docker run -d --name my_flask_container --env-file ./env.sh -p 80:80 my_flask_wsgi

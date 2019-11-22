## k8s ConfigMaps and Secrets
Scope of the exercise is to create a simple Python Flask app, create a container with the app inside, and then create a K8S deployment for the container using configmaps and secret for the app.


## Install
``` bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Docker image creation
Create or use the **Dockerfile** and then run the following commands
``` bash
# BUILD
docker build --tag=my_flask_wsgi

# SEND TO DOCKERHUB
docker login
docker image ls
docker tag my_flask_wsgi nbianchi/my_flask_wsgi:latest
docker push nbianchi/my_flask_wsgi
```

## Create Kubernetes configmap and secret
``` bash
kubectl apply -f configmap.yaml

# it's easier to create the secrets via cli because it takes care of the base 64 conversion automatically
kubectl create secret generic generic-secret --from-literal=mysql_password='abc*123\complex!'
```

## Run the app on Kubernetes
``` bash
kubectl apply -f app_deployment.yaml
kubectl apply -f service.yaml
kubectl get svc
```

## Checks
To verify that it work connect to the port on the node as per **kubectl get svc** output.  
On minikube the ip to address is from the command **minikube ip**

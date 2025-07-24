# Containers
Study notes on containerisation

# Docker

Docker notes

## Reference docker file
Dockerfile
```
# Use the official Node.js image as the base image
FROM node:14

# Set environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code
COPY . .

# Add additional file
ADD public/index.html /app/public/index.html

# Expose the port on which the application will run
EXPOSE $PORT

# Specify the default command to run when the container starts
CMD ["node", "app.js"]

# Labeling the image
LABEL version="1.0"
LABEL description="Node.js application Docker image"
LABEL maintainer="Your Name"

# Healthcheck to ensure the container is running correctly
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -fs http://localhost:$PORT || exit 1

# Set a non-root user for security purposes
USER node
```

## Working with Docker
Typical command to copy modify and save app
See docker version

```
docker --version
```


List images
```
docker images
```

Pull image from Docker Hub
```
docker pull hello-world
```

Run hello world image
```
docker run hello-world
```

List containers that were ran
```
docker ps -a
```

Remove container
```
docker container rm <container_id>
```

Build image
```
docker build . -t myimage:v1
```

Run image as a container
```
docker run -dp 8080:8080 myimage:v1
```

Check app responds
```
curl localhost:8080
```

Stop container
```
docker stop $(docker ps -q)
```

Check that container stopped
```
docker ps
```


# Kubernetes
# Using Kubernetes

Below provides view on Linux Arch

## Install and Config

Check
```
kubectl version
```

Install
```
sudo pacman -S kubectl
```

Config
List config
```
kubectl config view
```

Get cluster info
```
kubectl cluster-info
```


### For local development install minikube
```
sudo pacman -S minikube
```
```
minikube start
```
```
kubectl config use-context minikube
```


## Deploy


Create deployment using nginx image
```
kubectl create deployment my-deployment1 --image=nginx
```

Expose deployment as a server
```
kubectl expose deployment my-deployment1 --port=80 --type=NodePort --name=my-service1
```

## Operate
List services
```
kubectl get services
```

Get list of pods
```
kubectl get pods
```

Show labels of the pod
```
kubectl get pod <pod-name> --show-labels
```

Add label
```
kubectl label pods <pod-name> environment=deployment
```

Add pod
```
kubectl run my-test-pod --image=nginx --restart=Never
```

## Working with .yaml config
### StatefulSet
A StatefulSet manages the deployment and scaling of a set of pods, and maintains a sticky identity for each of their Pods, ensuring that each Pod has a persistent identity and storage.

```
touch statefulset.yaml
```

statefuleset.yaml
```
   apiVersion: apps/v1
   kind: StatefulSet
   metadata:
     name: my-statefulset
   spec:
     serviceName: "nginx"
     replicas: 3
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
         - name: nginx
           image: nginx
           ports:
           - containerPort: 80
             name: web
     volumeClaimTemplates:
     - metadata:
         name: www
       spec:
         accessModes: [ "ReadWriteOnce" ]
         resources:
           requests:
             storage: 1Gi
```

Create the resources defined in the YAML file
```
kubectl apply -f statefulset.yaml
```

Verify
```
kubectl get statefulsets
```

### DaemonSet
A DaemonSet ensures that a copy of a specific Pod runs on all (or some) nodes in the cluster. It is particularly useful for deploying system-level applications that provide essential services across the nodes in a cluster, such as log collection, monitoring, or networking services

```
touch daemonset.yaml
```

daemonset.yaml
```
  apiVersion: apps/v1
  kind: DaemonSet
  metadata:
    name: my-daemonset
  spec:
    selector:
      matchLabels:
        name: my-daemonset
    template:
      metadata:
        labels:
          name: my-daemonset
      spec:
        containers:
        - name: my-daemonset
          image: nginx
```

Apply
```
kubectl apply -f daemonset.yaml
```

Verify
```
kubectl get daemonsets
```
Numbers under fields DESIRED CRRENT READY UP-TO-DATE and AVAILABLE indicate number  of respective pods
NODE SELECTOR: Specifies which nodes in the cluster the DaemonSet should run on. By default, it's set to <none>, meaning the DaemonSet is not restricted to specific nodes.

# Containers
Study notes on containerisation

# Docker

Docker notes

install
```
sudo apt install docker.io -y
```

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
Bake your app into a reusable image.
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

### Docker compose
```
docker-compose up
```
Launch all the services defined in your compose file together (Node app, Mongo, etc.).

looks for ```docker-compose.yml``` file that looks like:
```
version: '3.9'

services:
  # Mongodb service
  mongo_db:
    container_name: db_container
    image: mongo:latest
    ports:
      - 27017:27017
    restart: always
    volumes:
      - mongo_data:/data/db

  # Node api service
  api:
    image: nodeapp
    ports:
      - 3030:3030
    depends_on: 
      - mongo_db

volumes:
  mongo_data: {}
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
Get more details about the pod
```
kubectl describe pod hello-world
```

Add label
```
kubectl label pods <pod-name> environment=deployment
```

Add pod
```
kubectl run my-test-pod --image=nginx --restart=Never
```

Delete pod
```
kubectl delete pod hello-world
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


## Create pod with an imperative command
Get clusters
```
kubectl config get-clusters
```

Get contexts
```
kubectl config get-contexts
```

Get pods
```
kubectl get pods
```

Export namespace as env variable
```
export MY_NAMESPACE=sn-labs-$USERNAME
```


Build and push
```
docker build -t us.icr.io/$MY_NAMESPACE/hello-world:1 . && docker push us.icr.io/$MY_NAMESPACE/hello-world:1
```

Run the "hello-world" image as a container in Kubernetes.
```
kubectl run hello-world --image us.icr.io/$MY_NAMESPACE/hello-world:1 --overrides='{"spec":{"template":{"spec":{"imagePullSecrets":[{"name":"icr"}]}}}}'
```

## Create pod with an imperative configuration file
Create file
```
touch hello-worlds-create.yaml
```

content
```
apiVersion: v1
kind: Pod
metadata:
  name: hello-world
spec:
  containers:
  - name: hello-world
    image: us.icr.io/<my_namespace>/hello-world:1
    ports:
    - containerPort: 8080
  imagePullSecrets:
  - name: icr

```

```
kubectl create -f hello-world-create.yaml
```

verify
```
kubectl get pods
```

## Create pod with an declarative command
This is better for production
```touch hello-world-apply.yaml``` with content:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  generation: 1
  labels:
    run: hello-world
  name: hello-world
spec:
  replicas: 3
  selector:
    matchLabels:
      run: hello-world
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        run: hello-world
    spec:
      containers:
      - image: us.icr.io/<my_namespace>/hello-world:1
        imagePullPolicy: Always
        name: hello-world
        ports:
        - containerPort: 8080
          protocol: TCP
        resources:
          limits:
            cpu: 2m
            memory: 30Mi
          requests:
            cpu: 1m
            memory: 10Mi   
      imagePullSecrets:
      - name: icr
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      securityContext: {}
      terminationGracePeriodSeconds: 30
```

Apply
```
kubectl apply -f hello-world-apply.yaml
```

Verify that deployment is created
```
kubectl get deployments
```

List pods
```
kubectl get pods
```

## Expose to internet
Expose
```
kubectl expose deployment/hello-world
```

Get services
```
kubectl get services
```

Start proxy (in development only)
```
kubectl proxy
```

Ping
```
curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy
```


# Working with autoscaling and secrets
## Prepare
Get files
`git clone https://github.com/raliaskarov/tutorial_docker.git`
`cd tutorial_docker`
`cd lab5_k8-scaling-and-secrets-mgmt`

Build
`export MY_NAMESPACE=sn-labs-$USERNAME`
`docker build . -t us.icr.io/$MY_NAMESPACE/myapp:v1`
`ibmcloud cr images`

Deploy
`kubectl apply -f deployment.yaml`
`kubectl get pods`
`kubectl port-forward deployment.apps/myapp 3000:3000`
`docker push us.icr.io/$MY_NAMESPACE/myapp:v1`
`kubectl expose deployment/myapp`

## VPA
Apply vertical autoscaler
`kubectl apply -f vpa.yaml`
`kubectl get vpa`
`kubectl describe vpa myvpa`

## HPA
Apply horizontal autoscaler
`kubectl apply -f hpa.yaml`
`kubectl proxy`

Test HPA in another window
```
for i in `seq 100000`; do curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/myapp/proxy; done
```

Monitor HPA in 3rd window
```
kubectl get hpa myhpa --watch
```
Ctr + C to break

```
kubectl get hpa myhpa
```

## Secrets
Apply secrets
`kubectl apply -f secret.yaml`
`kubectl get secret`
`kubectl get deployment` 


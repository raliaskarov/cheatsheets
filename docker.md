# Docker

Study notes on containerisation and Docker

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


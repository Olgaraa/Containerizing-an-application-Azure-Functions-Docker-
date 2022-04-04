Create an application (Azure Functions) that will take data from an API, connect to Azure SQL DB and perform operations (eg. Insert). Afterwards build and run an image (Dockerfile), by pushing it into Azure Container Registry and testing it with Azure Container Instances.

Trivia:

Dockerfile - a text document that contains all the necessary commands you need to call on the command line in order to create an image

docker build - command that builds an image from a Dockerfile
Syntax:
\n
docker build -t <tag:version> <dockerfile_path>
Eg:
docker build -t olgaraa/azurefunctionsimage:v1.0.0 .

Azure Container Registry - allows you to build, store, and manage container images and artifacts in a private registry.
In order to push an image to Azure Container Registry, you need to log in to ACR from your command line.
Syntax:
docker login <login_server> -u <user> -p <access_key_password>
Eg:
docker login olga.azurecr.io -u olga -p bhbhb54h5b4h54b5h4b5h4
	
Azure Container Instances (ACI) - a managed service that allows you to run containers directly on the Microsoft Azure public cloud

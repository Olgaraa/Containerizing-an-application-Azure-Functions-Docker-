Create an application (Azure Functions) that will take data from an API, connecto the Azure SQL DB and perform operations (eg. Insert). Afterwards build and run an image (Dockerfile), by pushing it into Azure Container Registry and testing it with Azure Container Instances.

Trivia:
Dockerfile - a text document that contains all the necessary commands you need to call on the command line in order to create an image

docker build - command that builds an image from a Dockerfile
Syntax:
docker build -t <tag:version> <dockerfile_path>
Eg:
docker build -t olgaraa/azurefunctionsimage:v1.0.0 .

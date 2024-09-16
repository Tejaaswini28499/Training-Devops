name: Docker Image CI push

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Log in to Docker Hub
      run: echo "${{ secrets.DOCKERHUB_PASSWORD }}" | docker login -u "${{ secrets.DOCKERHUB_USERNAME }}" --password-stdin

    - name: Build the Docker image
      run: docker build . --file Dockerfile --tag justwicks/qrtap.in

    - name: Push the Docker image to Docker Hub
      run: docker push justwicks/qrtap.in


## How to setup secrets in GitAcions
```
Step-by-Step Guide
Navigate to Your Repository:

Go to the GitHub repository where you want to set up the secrets.
Go to Settings:

On the repository page, click on the Settings tab located on the right side of the page.
Access Secrets and Variables:

In the left sidebar under "Security", click on Secrets and variables.
Then, click on Actions under "Secrets and variables".
Add a New Secret:

Click on the New repository secret button.
Enter the Secret Name and Value:

Name: Provide a name for your secret, e.g., DOCKERHUB_USERNAME.
Value: Enter the sensitive information (e.g., your Docker Hub username) in the value field.
Save the Secret:

Click the Add secret button to save it.
```
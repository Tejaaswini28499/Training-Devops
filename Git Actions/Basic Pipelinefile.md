name: Docker Image CI

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
    - name: Build the Docker image
      run: docker build . --file Dockerfile --tag my-image-name:$(date +%s)


name: Docker Image CI
This names the workflow "Docker Image CI" for easy identification in GitHub's Actions tab.
Triggering Events:

on:
push:: This part triggers the workflow when changes (commits) are pushed to the main branch of the repository.
pull_request:: This triggers the workflow when a pull request is opened, synchronized, or reopened against the main branch.
Jobs:

The workflow contains a single job named build:
runs-on: ubuntu-latest: This specifies the operating system environment on which the job will run. In this case, it's an Ubuntu environment.

Steps:
The job contains a series of steps to be executed:
- uses: actions/checkout@v4: This step checks out the repository's code, making it available for subsequent steps. It uses version 4 of the actions/checkout action.
- name: Build the Docker image: This step is named "Build the Docker image".
run: docker build . --file Dockerfile --tag my-image-name:$(date +%s):
docker build .: Builds a Docker image using the Dockerfile located in the root of the repository (. refers to the current directory).

--file Dockerfile: Specifies the Dockerfile to use for building the image.
--tag my-image-name:$(date +%s): Tags the built Docker image with a name (my-image-name) followed by a unique timestamp ($(date +%s) generates a Unix timestamp, ensuring that each build has a unique tag).

Purpose
The purpose of this workflow is to automate the Docker image building process, ensuring that every time changes are made to the main branch (either directly or through a pull request), a new Docker image is built and tagged with a unique identifier. This helps in maintaining consistent and versioned Docker images for deployment or further testing.
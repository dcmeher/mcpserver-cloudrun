# MCP Account Validator Server
 This is a Model Context Protocol (MCP) server built with Python. It provides tools for arithmetic and account validation, designed to be deployed as a high-performance microservice using streamable-http.
## FeaturesThe server exposes the following tools to MCP-compatible AI clients:
validate_account: Checks if an account number is valid (length $\ge 5$) and returns mock user data.
## Quick StartLocal DevelopmentInstall dependencies using uv:Bashuv sync
Run the server:Bashpython server.py
The server will start on the port defined by the PORT environment variable (default: 8080).
##Containerization & DeploymentDockerA Dockerfile is included to package the application using a python:3.11-slim base image and the uv package manager for fast builds.
##To build the image locally:Bashdocker build -t mcp-account-validator .
Google Cloud Run DeploymentAs a recommended GCP path, you can deploy this directly to Cloud Run:
Enable APIs: Enable Cloud Run and Artifact Registry.
Deploy: cloud run deploy account-validator \
    --source . \
    --region us-central1 \
    --allow-unauthenticated
## Security & IAMWhen deploying to GCP, ensure the following:
Service Account: The Cloud Run service uses a Service Account that requires roles/run.invoker if you disable public access.
##Project Structure
server.py:Core logic and MCP tool definitions.
test_server.py: Test suite for validating tool logic.
Dockerfile: Optimized container configuration.
pyproject.toml: Dependency management via uv.



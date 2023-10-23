
# AI Software Engineering 

## Introduction

This repository contains the code for an AI Software Engineering project. The project utilizes Docker services and Django for the admin site. It was built using AI-Augmented Software Engineering methodologies follow the following 5 principles:

- The Common SDP (software development process)
- Tool Selection
- Prompt Engineering
- Intelligent Feedback and Artifact Creation
- Experience-based vetting

The tools, prompt patterns, logic behind the decisions made and input / output of the AI tool conversations can be found in the conversations directory. Conversations are divided up into phases of the software development process:

- Kickoff 
- Planning 
- Design 
- Setup 
- Development 
- Testing 
- Deployment

## Prerequisites

To run the application you'll onlky need Docker and Docker compose installed
For more information on installing Docker and Dcoker compose visit:
https://docs.docker.com/compose/install/

## Running the Application

To run the application, follow these steps:

1. Clone the repository: `git clone https://github.com/adamhoke/ai-software-engineering.git`
2. Navigate to the project directory: `cd ai-software-engineering`
3. Run the Docker services: `docker-compose up`

## Using the Application
To use the To-Do application, navigate to http://localhost:8000. Here you'll see the Django application.
To access the admin site for any reason, navigate to /admin on the same host.

To access PGAdmin to inspect the database, navigate to localhost:8080

For the default user and passwords for both the admin section and the pgadmin UI, see the docker-compose.yaml file.

## Details about the Application and Docker Services

The application is built using Django (version 4.2.6), Black (version 23.9.1), and Flake8 (version 6.1.0). It consists of several Docker services including `todo` (likely the main application or service), `db` (probably the database service), and `pgadmin` (a popular administration and management tool for the PostgreSQL database).

## Changelog

| Version | Description            | Date       |
|---------|------------------------|------------|
| 1.0     | Initial release        | 10-23-2023     |

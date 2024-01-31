
# Async Shop with Microservices

My first project based on microservice architecture for educational purposes. 
The goal of the project is to create minimal functionality of an online store using Python, gRPC. 


## Stack

 - FastAPI - for gateway.
 - Piccolo - for operating with database.
 - PostgreSQL
 



## Installation

Clone the project

```bash
  git clone https://github.com/GilbertFranchesko/AsyncShopPython.git
  cd AsyncShopPython
```

First of all, you have to run all the microservices
```bash
 cd gServices
 docker-compose -f local.yaml up --build
```

After successfully bringing up all microservices, you can move on to bringing up the gateway api

```bash
 cd APIGateway
 docker-compose -f local.yaml up --build
```
After that, you can check if it works by going to http://localhost:5000 in your browser.


## Testing

Testing microservices has proven to be an interesting challenge for me. That's why you can see only test developments for now, because the project logic is not so complicated.

Firstly, you can a different microservice to testing.
```bash
# But for working with them the main compose file must a upped been.
cd gServices
docker-compose -f local.yaml exec [SERVICE_NAME]_service exec python tests.py
```

The names of microservices you can see in ```gServices/local.yaml``` file.
For example: ```product_service```, and more.
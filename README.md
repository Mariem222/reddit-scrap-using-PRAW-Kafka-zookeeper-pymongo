# Reddit Scraping Using PRAW, Kafka, Zookeeper, and PyMongo

## Overview

This project demonstrates a Reddit scraping system implemented in Python using PRAW for accessing Reddit API, 
Kafka for message queuing, Zookeeper for distributed coordination, and PyMongo for storing scraped data in MongoDB.


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [Results](#results)

## Prerequisites

Before you begin, ensure you have the following installed:

Python 3.8 
docker and docker-compose
pip ( python package manager )

other dependencies will be triggered with a script when running the the commands I'll give bellow in the usage section.


## Configuration

run the following command to clone the project:
git clone https://github.com/Mariem222/reddit-scrap-using-PRAW-Kafka-zookeeper-pymongo.git

access the directory containing the project 
cd reddit-scrap-using-PRAW-Kafka-zookeeper-pymongo

modify the configurations to match your need and credentials:

### in the producer/producer.py
in the producer/producer.py 
Add your own reddit credentials
client_id = 'your client_id'
client_secret = 'your client_secret'
user_agent = 'your reddit username'

edit the kafka settings to name your topis:

kafka_bootstrap_servers = 'host.docker.internal:29092' ( this port and host are defined in the docker-compose.yml if you want to modify the start by there )
kafka_topic = 'your_topic'

edit the subreddits and your keyword(s)
subreddits = ['keyword(s)','of interst']

### in the consumer/consumer.py
make sure to match topic defined in the producer 
Kafka settings
kafka_bootstrap_servers = 'host.docker.internal:29092'
kafka_topic = 'topic defined in the producer.py'
ports and hostnames must match the ones defined in the docker-compose.yml file in the root directory 


Now your scrapper is all set let's run it ! 

## Usage

For the first time you'll need to build the images before starting them: 
used the following command to start the set of Docker containers defined in the docker-compose.yml
including Zookeeper kafka mongodb and a container for the producer and another one for the consumer

docker-compose up --build

for future uses you can drop the build arguments and start directly 

this command alone will pull the images install dependencies start containers in order and you'll only sit and watch your data moving from container to
finally being stored in your mongo db:

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Any contributions are welcome!

## Results













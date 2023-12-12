from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient

# Kafka settings
kafka_bootstrap_servers = 'host.docker.internal:29092'
kafka_topic = 'topic defined in the producer.py'

# MongoDB settings
mongo_host = 'mongo'
mongo_port = 27017
mongo_db = 'reddit_data'
mongo_collection = 'posts'

# Initialize Kafka Consumer
conf = {'bootstrap.servers': kafka_bootstrap_servers, 'group.id': 'mygroup', 'auto.offset.reset': 'earliest'}
consumer = Consumer(conf)
consumer.subscribe([kafka_topic])

# Initialize MongoDB client and collection
mongo_client = MongoClient(mongo_host, mongo_port)
mongo_db_instance = mongo_client[mongo_db]
mongo_collection_instance = mongo_db_instance[mongo_collection]

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                break

        # Store message value in MongoDB
        msg=msg.value()
        message= msg.decode('utf-8')
        lines = message.split('\n')
        message_dict = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                message_dict[key.strip()] = value.strip()
        mongo_collection_instance.insert_one(message_dict)

        print(f"Message Inserted to MONGODB SUCCESSFULY !: {msg}")

except KeyboardInterrupt:
    pass
finally:
    consumer.close()

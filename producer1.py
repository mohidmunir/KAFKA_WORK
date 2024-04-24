import json
import time
from kafka import KafkaProducer

# Kafka producer settings
bootstrap_servers = ['localhost:9092']
topic_name = 'amazon_metadata'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Load the preprocessed data
with open('preprocessed_data.json') as f:
    data = json.load(f)

# Send data chunks to Kafka topic
for chunk in data:
    # Serialize the data chunk to JSON
    data_json = json.dumps(chunk)
    
    # Send the data chunk to the Kafka topic
    producer.send(topic_name, value=data_json.encode('utf-8'))
    
    # Flush the producer to ensure data is sent immediately
    producer.flush()
    
    # Sleep for 1 second to simulate real-time data streaming
    time.sleep(1)

# Close the Kafka producer
producer.close()
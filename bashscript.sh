bashscript.py(bouns)
#!/bin/bash

# Start Zookeeper
zookeeper-server-start.sh

# Start Kafka
kafka-server-start.sh

# Create Kafka topics
kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 amazon_metadata

# Start Kafka Connect
connect-distributed.sh

# Start Producer
python producer1.py

# Start Consumers
python consumer1.py &
python consumer2.py &
python consumer3.py &
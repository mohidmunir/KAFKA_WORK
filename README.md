# KAFKA_WORK
Amazon Metadata Analysis Project
Overview
This project analyzes the Amazon metadata dataset using Apache Kafka and Python. The project consists of a Kafka cluster with multiple topics, two producers that generate data, and three consumers that consume and process the data. The data is generated based on a realistic Amazon metadata use case using a Kafka client library. The consumers perform different processes on the data, such as frequent itemset analysis, association rule analysis, and product recommendation analysis. The pipeline is also integrated with an external system, such as a MongoDB database.
Data Description
Brief description of some of the most common data available in the Amazon metadata dataset:
Product Data: Historical and real-time data on product information, including product title, description, price, and sales rank.
Customer Data: Information on customer behavior, including purchase history and product ratings.
Product Relationships: Data on product relationships, including similar products and frequently bought together products.
Product Categories: Information on product categories, including category hierarchy and product classification.
Pipeline Setup
To set up and run the pipeline, follow these steps:
Install Apache Kafka and ZooKeeper.
Start ZooKeeper by running the following command in a terminal:
bin/zookeeper-server-start.sh config/zookeeper.properties
Start Kafka brokers by running the following command in a new terminal:
kafka-server-start.sh config/server1.properties
kafka-server-start.sh config/server2.properties
kafka-server-start.sh config/server3.properties
Create Kafka topics with different replication factors, retention periods, and partition counts. For example:
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 4 --topic topic1
Create Kafka producers:
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic1,topic2
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic3
Create Kafka consumers:
kafka-console-consumer.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --topic topic1
kafka-console-consumer.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --topic topic2
kafka-console-consumer.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --topic topic3
Analysis Approach
The analysis approach consists of the following steps for each consumer:
Consumer 1: Frequent Itemset Analysis
Data Ingestion: Read data from Kafka topic, which contains Amazon metadata information.
Data Preprocessing: Preprocess data by removing stop words and stemming to normalize the data.
Frequent Itemset Generation: Generate frequent itemsets using the Apriori algorithm, which identifies sets of products that are frequently purchased together.
Data Storage: Store frequent itemsets in a MongoDB database for further analysis and visualization.
Consumer 2: Association Rule Analysis
Data Ingestion: Read data from Kafka topic, which contains Amazon metadata information.
Data Preprocessing: Preprocess data by removing stop words and stemming to normalize the data.
Association Rule Generation: Generate association rules using the PCY algorithm, which identifies rules of the form "if A then B" based on frequent itemsets.
Data Storage: Store association rules in a MongoDB database for further analysis and visualization.
Consumer 3: Product Recommendation Analysis
Data Ingestion: Read data from Kafka topic, which contains Amazon metadata information.
Data Preprocessing: Preprocess data by removing stop words and stemming to normalize the data.
Product Recommendation Generation: Generate product recommendations based on similarity using a custom algorithm, which identifies products that are similar to the ones a customer has purchased or viewed.
Data Storage: Store product recommendations in a MongoDB database for further analysis and visualization.
Why this approach?
I chose this approach because it allows for real-time processing and analysis of large datasets. Kafka's distributed architecture and fault-tolerance make it ideal for handling large amounts of data, while Python's simplicity and flexibility make it easy to implement complex analysis tasks. MongoDB was chosen as the database because of its ability to handle large amounts of unstructured data and its ease of use.
How to run
To run this project, simply execute the bash script run_project.sh in the terminal. This script will start the Kafka server, create the necessary topics, and start the consumers.
Note: Make sure to install Kafka, Python, and MongoDB on your machine before running this project.
Conclusion
This project demonstrates the power of Apache Kafka and Python in analyzing large datasets. By using Kafka's distributed architecture and Python's simplicity, we can perform complex analysis tasks in real-time. The MongoDB database provides a

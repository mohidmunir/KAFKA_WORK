#Consumer.py 3:
import kafka
from kafka.consumer import KafkaConsumer
from collections import defaultdict
import json
import itertools

# Kafka consumer settings
bootstrap_servers = ['localhost:9092']
topic_name = 'amazon_metadata'
group_id = 'my_unique_group'

# Create a Kafka consumer
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, group_id=group_id)

# Product Recommendation Analysis settings
min_similarity = 0.5

# Initialize data structures
product_features = defaultdict(list)
product_recommendations = {}

# Consumer loop
for message in consumer:
	try:
		# Extract the product data from the message
		product = json.loads(message.value)
		asin = product['asin']
		features = product['feature']
		categories = product['categories']

		# Update the product features
		product_features[asin] = features + categories

		# Check if the product has enough features
		if len(product_features[asin]) >= 5:
			# Calculate the similarity with other products
			similar_products = []
			for other_asin, other_features in product_features.items():
				if asin != other_asin:
					similarity = calculate_similarity(product_features[asin], other_features)
					if similarity >= min_similarity:
						similar_products.append((other_asin, similarity))

			# Update the product recommendations
			product_recommendations[asin] = similar_products

			# Print the product recommendations
			print(f"Product Recommendations for {asin}:")
			for recommendation in product_recommendations[asin]:
				print(f"  {recommendation[0]} with similarity {recommendation[1]}")
	except Exception as e:
		print(f"Error processing message: {e}")

def calculate_similarity(features1, features2):
	# Calculate the Jaccard similarity between two sets of features
	intersection = set(features1) & set(features2)
	union = set(features1) | set(features2)
	return len(intersection) / len(union)
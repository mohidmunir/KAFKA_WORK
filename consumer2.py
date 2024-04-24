#Consumer2.py:
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

# PCY algorithm settings
min_support = 0.5
min_confidence = 0.7

# Sliding window settings
window_size = 100  # Process 100 messages at a time
window_timeout = 60  # seconds

# Initialize data structures
itemsets = defaultdict(int)
rules = []

# Consumer loop
for message in consumer:
	try:
		# Extract the product data from the message
		product = json.loads(message.value)
		features = product['feature']
		categories = product['categories']
		transaction = set(features + categories)

		# Update the itemsets
		for item in transaction:
			itemsets[item] += 1

		# Check if the window is full or timeout has reached
		if len(itemsets) >= window_size or message.timestamp >= window_timeout:
			# Process the itemsets in the window
			frequent_itemsets = {item: count for item, count in itemsets.items() if count >= min_support * window_size}
			rules = generate_association_rules(frequent_itemsets, min_confidence)

			# Print real-time insights and associations
			print("Real-time Insights:")
			print("Frequent Itemsets:")
			for item, count in frequent_itemsets.items():
				print(f"{item}: {count}")
			print("Rules:")
			for rule in rules:
				print(f"{rule[0]} => {rule[1]} with confidence {rule[2]}")

			# Reset the window
			itemsets = defaultdict(int)
			window_timeout = message.timestamp + 60
	except Exception as e:
		print(f"Error processing message: {e}")

def generate_association_rules(frequent_itemsets, min_confidence):
	rules = []
	for itemset in frequent_itemsets:
		for subset in generate_subsets(itemset):
			if len(subset) > 0 and len(itemset - subset) > 0:
				confidence = calculate_confidence(itemset, subset, frequent_itemsets)
				if confidence >= min_confidence:
					rules.append((subset, itemset - subset, confidence))
	return rules

def generate_subsets(itemset):
	subsets = []
	for i in range(1, len(itemset)):
		subsets.extend(itertools.combinations(itemset, i))
	return subsets

def calculate_confidence(itemset, subset, frequent_itemsets):
	confidence_count = frequent_itemsets[itemset]
	support_count = frequent_itemsets[subset]
	return confidence_count / support_count

# PCY algorithm implementation
def pcy_algorithm(itemsets, min_support, min_confidence):
	frequent_itemsets = {item: count for item, count in itemsets.items() if count >= min_support * window_size}
	rules = generate_association_rules(frequent_itemsets, min_confidence)
	return frequent_itemsets, rules

# Call the PCY algorithm
frequent_itemsets, rules = pcy_algorithm(itemsets, min_support, min_confidence)

# Print real-time insights and associations
print("Real-time Insights:")
print("Frequent Itemsets:")
for item, count in frequent_itemsets.items():
	print(f"{item}: {count}")
print("Rules:")
for rule in rules:
	print(f"{rule[0]} => {rule[1]} with confidence {rule[2]}")
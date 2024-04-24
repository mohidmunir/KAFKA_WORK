consumer1.py

import kafka
from kafka.consumer import KafkaConsumer
from collections import defaultdict
from apyori import apriori
import json
import itertools

# Kafka consumer settings
bootstrap_servers = ['localhost:9092']
topic_name = 'amazon_metadata'
group_id = 'my_group'

# Create a Kafka consumer
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, group_id=group_id)

# Apriori algorithm settings
min_support = 0.5
min_confidence = 0.7

# Sliding window settings
window_size = 100  # Process 100 messages at a time
window_timeout = 60  # seconds

# Initialize data structures
itemsets = set()
rules = []
transactions = set()

# Consumer loop
for message in consumer:
	try:
		# Extract the product data from the message
		product = json.loads(message.value)
		features = product['feature']
		categories = product['categories']
		transaction = set(features + categories)
		transactions.add(frozenset(transaction))  # Use a set to store transactions

		# Check if the window is full or timeout has reached
		if len(transactions) >= window_size or message.timestamp >= window_timeout:
			# Process the transactions in the window
			itemsets, rules = apriori(transactions, min_support, min_confidence)

			# Print real-time insights and associations
			print("Real-time Insights:")
			print("Itemsets:")
			for itemset in itemsets:
				print(itemset)
			print("Rules:")
			for rule in rules:
				print(rule)

			# Reset the window
			transactions = set()
			window_timeout = message.timestamp + 60
	except Exception as e:
		print(f"Error processing message: {e}")

def apriori(transactions, min_support, min_confidence):
	# Initialize the itemsets and rules
	itemsets = []
	rules = []

	# Generate the frequent itemsets
	frequent_itemsets = generate_frequent_itemsets(transactions, min_support)

	# Generate the association rules
	rules = generate_association_rules(frequent_itemsets, min_confidence)

	return itemsets, rules

def generate_frequent_itemsets(transactions, min_support):
	# Initialize the frequent itemsets
	frequent_itemsets = []

	# Generate the candidate itemsets
	candidate_itemsets = generate_candidate_itemsets(transactions)

	# Filter the candidate itemsets based on the minimum support
	for itemset in candidate_itemsets:
		if calculate_support(itemset, transactions) >= min_support:
			frequent_itemsets.append(itemset)

	return frequent_itemsets

def generate_candidate_itemsets(transactions):
	# Initialize the candidate itemsets
	candidate_itemsets = []

	# Generate the candidate itemsets
	for transaction in transactions:
		for item in transaction:
			candidate_itemsets.append({item})

	return candidate_itemsets

def calculate_support(itemset, transactions):
	# Initialize the support count
	support_count = 0

	# Calculate the support count
	for transaction in transactions:
		if itemset.issubset(set(transaction)):
			support_count += 1

	return support_count / len(transactions)

def generate_association_rules(frequent_itemsets, min_confidence):
	# Initialize the association rules
	rules = []

	# Generate the association rules
	for itemset in frequent_itemsets:
		for subset in generate_subsets(itemset):
			if len(subset) > 0 and len(itemset - subset) > 0:
				confidence = calculate_confidence(itemset, subset, transactions)
				if confidence >= min_confidence:
					rules.append((subset, itemset - subset, confidence))

	return rules

def generate_subsets(itemset):
	# Initialize the subsets
	subsets = []

	# Generate the subsets
	for i in range(1, len(itemset)):
		subsets.extend(itertools.combinations(itemset, i))

	return subsets

def calculate_confidence(itemset, subset, transactions):
	# Initialize the confidence count
	confidence_count = 0

	# Calculate the confidence count
	for transaction in transactions:
		if itemset.issubset(set(transaction)):
			confidence_count += 1

	return confidence_count / calculate_support(subset, transactions)
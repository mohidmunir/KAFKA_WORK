
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['amazon_metadata']
collection = db['frequent_itemsets']

# Store the frequent itemsets in the database
for itemset, count in frequent_itemsets.items():
	collection.insert_one({'itemset': itemset, 'count': count})
#Consumer 2:
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['amazon_metadata']
collection = db['association_rules']

# Store the association rules in the database
for rule in rules:
	collection.insert_one({'rule': rule[0], 'confidence': rule[2]})
#Consumer 3:
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['amazon_metadata']
collection = db['product_recommendations']

# Store the product recommendations in the database
for asin, recommendations in product_recommendations.items():
	collection.insert_one({'asin': asin, 'recommendations': recommendations})

import json

def preprocess_data(raw_data):
    cleaned_data = {}  # Initialize an empty dictionary to store cleaned data
    for key, value in raw_data.items():
        # Example preprocessing logic: Convert all string values to uppercase
        if isinstance(value, str):
            cleaned_data[key] = value.upper()
        else:
            cleaned_data[key] = value
    return cleaned_data

# Input and output file paths
input_file_path = '/home/moiz/Desktop/Assignment_3/Sampled_Amazon_Meta.json'
output_file_path = 'preprocessed_data.json'

# Open input and output files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Iterate over each line in the input file
    for line in input_file:
        # Load JSON data from the current line
        raw_data = json.loads(line)
        
        # Preprocess the data
        cleaned_data = preprocess_data(raw_data)
        
        # Write the preprocessed data to the output file
        json.dump(cleaned_data, output_file)
        output_file.write('\n')  # Add a newline character to separate each JSON object

print("Preprocessing completed. Preprocessed data saved to:", output_file_path)
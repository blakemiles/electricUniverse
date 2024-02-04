#!/bin/bash

# Directory containing JSON files
json_directory="/Users/blakemiles/electricUniverse/transcripts"

# Output directory for text files
output_directory="/Users/blakemiles/electricUniverse/transcripts/text"

# Create output directory if it does not exist
mkdir -p "$output_directory"

# Loop through all .json files in the directory
for json_file in "$json_directory"/*.json; do
  # Check if the JSON file exists
  if [[ -f "$json_file" ]]; then
    # Extract the base filename without extension
    base_name=$(basename "$json_file" .json)

    # Convert JSON to plain text (change this line according to your needs)
    jq -r . "$json_file" > "$output_directory"/"$base_name".txt

    echo "Converted $json_file to $base_name.txt"
  else
    echo "No JSON files found in $json_directory."
  fi
done
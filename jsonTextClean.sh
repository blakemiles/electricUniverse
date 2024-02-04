#!/bin/bash

# Directory containing text files (converted from JSON)
text_directory="/Users/blakemiles/electricUniverse/transcripts/text"

# Output directory for extracted text files
output_directory="/Users/blakemiles/electricUniverse/transcripts/text/cleaned"

# Create output directory if it does not exist
mkdir -p "$output_directory"

# Loop through all .txt files in the directory
for text_file in "$text_directory"/*.txt; do
  # Check if the text file exists
  if [[ -f "$text_file" ]]; then
    # Extract the base filename without extension
    base_name=$(basename "$text_file" .txt)

    # Use jq to extract all string values and save them to a new file
    jq -r 'recurse | strings' "$text_file" > "$output_directory"/"$base_name"_extracted.txt

    echo "Extracted text elements from $text_file to $base_name""_extracted.txt"
  else
    echo "No text files found in $text_directory."
  fi
done

echo "Extraction complete."
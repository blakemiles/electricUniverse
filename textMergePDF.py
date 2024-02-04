import os

# Directory containing text files
text_directory = "/Users/blakemiles/electricUniverse/transcripts/cleanedText"
# Output text file name
output_file = "transcriptsThunderboltsProject_Merged.txt"

# Get a list of text files
text_files = [f for f in sorted(os.listdir(text_directory)) if f.endswith(".txt")]

# Open output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Process each file and append its content to the output file
    for text_file in text_files:
        with open(os.path.join(text_directory, text_file), 'r', encoding='utf-8') as infile:
            # Read the content, strip newlines, and write to the output file
            outfile.write(infile.read().replace('\n', ' '))
            # Add a newline to separate content between files
            outfile.write('\n')

print("Text files have been combined into one.")
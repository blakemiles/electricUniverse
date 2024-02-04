import os

# Path to the large input text file
input_file_path = "/Users/blakemiles/electricUniverse/transcriptsThunderboltsProject_Merged.txt"
# Directory where the split files will be saved
output_directory = "/Users/blakemiles/electricUniverse/transcripts/"
# Maximum size of each split file in bytes (800 KB)
max_file_size = 819200

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

def write_chunk(chunk, file_index):
    # Construct the filename for the split file
    output_file_path = os.path.join(output_directory, f"transcriptsThunderboltsProject_{file_index}.txt")
    # Write the current chunk to the output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(chunk)

# Initialize variables
current_chunk = ""
file_index = 1
current_size = 0

# Open the large text file and start processing
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Check if adding the current line exceeds the max file size
        if current_size + len(line.encode('utf-8')) > max_file_size:
            # Write the current chunk to a new file
            write_chunk(current_chunk, file_index)
            # Reset the chunk and increment the file index
            current_chunk = line
            current_size = len(line.encode('utf-8'))
            file_index += 1
        else:
            # Add the current line to the chunk
            current_chunk += line
            current_size += len(line.encode('utf-8'))

        # If there's a paragraph break (two line breaks), consider it as a possible split point
        if line == '\n' and current_size >= max_file_size * 0.9:  # 90% of max size for a safe split
            # Write the current chunk to a new file
            write_chunk(current_chunk, file_index)
            # Reset the chunk and increment the file index
            current_chunk = ""
            current_size = 0
            file_index += 1

# Write any remaining content to a final file
if current_chunk:
    write_chunk(current_chunk, file_index)

print(f"Large text file has been split into {file_index} parts.")
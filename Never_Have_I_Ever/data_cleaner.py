import re

# Open the file 'database.txt' in read mode and read all lines into a list
file = open('database.txt', 'r')
content = file.readlines()
print(content)

# Initialize an empty list to store cleaned lines
clean_content = []

# Iterate through each line in the content list
for line in content:
    # Use regex to remove tabs, newlines, numbers followed by a dot, multiple spaces, and non-word boundary spaces
    clean_content.append(re.sub('(\t)+|(\n)+|(\d)+\.|(\s\s)+|(\B\s)', '', line))

# Print the cleaned content for verification
print(clean_content)

# Remove any empty strings from the cleaned content list
while True:
    try:
        clean_content.remove('')
    except ValueError:
        # Break the loop when no more empty strings are found
        break

# Open a new file 'data.txt' in write mode to store the final cleaned content
final_file = open('data.txt', 'w')

# Write each cleaned line to the final file, adding a newline character after each line
for line in clean_content:
    final_file.write(line + '\n')

# Close the final file to ensure all data is written and resources are freed
final_file.close()

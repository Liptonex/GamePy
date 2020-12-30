import re

file = open('database.txt', 'r')
content = file.readlines()
print(content)
clean_content = []
for line in content:
    clean_content.append(re.sub('(\t)+|(\n)+|(\d)+\.|(\s\s)+|(\B\s)', '', line))
print(clean_content)

while True:
    try:
        clean_content.remove('')
    except ValueError:
        break

final_file = open('data.txt', 'w')

for line in clean_content:
    final_file.write(line + '\n')

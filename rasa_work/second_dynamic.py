import re

with open("C:\\Users\\india\\OneDrive\\Documents\\SRAJAN\\rasa_work\\data\\nlu.yml", 'r') as file:
    nlu_content = file.read()
newContent = re.sub(re.escape('\\n'), '', nlu_content)
print(newContent)



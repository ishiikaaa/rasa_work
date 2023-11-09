# import yaml
# import json
# import pandas as pd
# import nltk
# from nltk.corpus import stopwords
# with open('scraped_data.json') as f:
#     data = json.load(f)
# df = pd.DataFrame(data)
# list_of_strings = df.to_numpy().tolist()
# # print(list_of_strings)
# flattened_list = [item for sublist in list_of_strings for item in sublist]
# with open('list_of_strings.txt', 'w') as f:
#     for inner_list in list_of_strings:
#         json.dump(inner_list, f)
#         f.write('\n')
# size = len(list_of_strings)
# print(size)
# for i in list_of_strings:
#     print(i)

import re
import json
import pandas as pd
import yaml
with open('scraped_data.json') as f:
    data = json.load(f)
df = pd.DataFrame(data)
list_of_strings = df.values.tolist()
nlu_data = {"version": "3.1", "nlu": []}

for string_list in list_of_strings:
    intent_name = string_list[0]
    examples = string_list[1:]
    intent_data = {
        "intent": intent_name,
        "examples": "|",
    }
    for example in examples:
        intent_data["examples"] += f"\n  - {example}"
    nlu_data["nlu"].append(intent_data)
with open("C:\\Users\\india\\OneDrive\\Documents\\SRAJAN\\rasa_work\\data\\nlu.yml", 'w') as yaml_file:
    yaml.dump(nlu_data, yaml_file, default_flow_style=False)

with open("C:\\Users\\india\\OneDrive\\Documents\\SRAJAN\\rasa_work\\data\\nlu.yml", 'r') as file:
    nlu_content = file.read()
newContent = re.sub(re.escape('\\n'), '', nlu_content)
print(newContent)




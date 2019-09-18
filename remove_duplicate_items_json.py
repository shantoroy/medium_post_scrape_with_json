import json

with open("post_data/related_all_post_data_without_ethereum.json", "r") as f:
    data = json.load(f)
unique_post = {each['title']: each for each in data}
listed_dictionary_items = list(unique_post.values())
with open("post_data/related_data_rm_duplicacy_without_ethereum.json", "w") as f:
    json.dump(listed_dictionary_items, f)
print("# of post after removing duplicacy = ", len(listed_dictionary_items))

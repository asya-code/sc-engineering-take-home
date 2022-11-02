import requests
import operator
import json

url = "https://hub.snapshot.org/graphql"
skip_entry = 0

voters_dict = {}

def get_votes(url, skip_entry):
    body = f'{{ votes(first: 1000, skip: {skip_entry} where: {{space: "aave.eth"}}, orderBy: "created", orderDirection: asc) {{voter}} }}'
    response = requests.get(url=url, json={"query": body})
    votes = response.json()["data"]["votes"]
    return votes


def add_to_dict(votes, voters_dict):
    for vote in votes:
        user = vote["voter"]
        voters_dict[user] = voters_dict.get(user, 0) + 1
    return voters_dict

while len(get_votes(url, skip_entry)) > 0:
    #print(skip_entry)
    votes = get_votes(url, skip_entry)
    add_to_dict(votes, voters_dict)
    #print(len(voters_dict))
    skip_entry += 1000

# to not go over the whole dataset again and start from the last page containing data processed
last_entry = skip_entry - 1000
sorted_voters = sorted(voters_dict.items(), key=operator.itemgetter(1), reverse=True)

most_active_20 = sorted_voters[0:20]
print(most_active_20)



import requests
import operator
import json

url = "https://hub.snapshot.org/graphql"
skip_entry = 0
voters_dict = {}

# he max size of GraphQL response for this query is 2000 objects
def get_votes(url, skip_entry):
    body = f'{{ votes(first: 20000, skip: {skip_entry} where: {{space: "aave.eth"}}, orderBy: "created", orderDirection: asc) {{voter}} }}'
    response = requests.get(url=url, json={"query": body})
    votes = response.json()["data"]["votes"]
    return votes

def add_to_dict(votes, voters_dict):
    for vote in votes:
        user = vote["voter"]
        voters_dict[user] = voters_dict.get(user, 0) + 1
    return voters_dict

# count all votes and save the number of the last object processed
votes_amount = 0

def full_voters_data(skip_entry, votes_amount):
    while len(get_votes(url, skip_entry)) > 0:
        votes = get_votes(url, skip_entry)
        votes_amount += len(votes)
        add_to_dict(votes, voters_dict)
        skip_entry += 20000
    return voters_dict

full_voters_data(skip_entry, votes_amount)

sorted_voters = sorted(voters_dict.items(), key=operator.itemgetter(1), reverse=True)

most_active_20 = sorted_voters[0:20]
print(most_active_20)



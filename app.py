import requests
import operator
import datetime


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
global votes_amount
votes_amount = 0

def full_voters_data(skip_entry):
    while len(get_votes(url, skip_entry)) > 0:
        votes = get_votes(url, skip_entry)
        global votes_amount
        votes_amount = votes_amount + len(votes)
        add_to_dict(votes, voters_dict)
        skip_entry += 20000
    return voters_dict

def m_active_part_rate(voter, votes_amount):
    participation = 100 / votes_amount * voter[1]
    return voter[0], participation

full_voters_data(skip_entry)
#print(voters_dict['0x7A3BdeE62dd34faC317Ae61cd8B3bA7c27ada145'])

sorted_voters = sorted(voters_dict.items(), key=operator.itemgetter(1), reverse=True)
raw_most_active_20 = sorted_voters[0:20]
#print(raw_most_active_20)
most_active_20 = [voter[0] for voter in raw_most_active_20]
part_rate_20 = [m_active_part_rate(voter, votes_amount) for voter in raw_most_active_20]

print(datetime.datetime.now())
print(most_active_20)
print(votes_amount)
print(part_rate_20)


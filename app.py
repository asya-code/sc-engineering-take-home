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

def participation_rate(voter, votes_amount):
    participation = 100 / votes_amount * voter[1]
    return voter[0], participation


def voter_by_adress(address):
    #since we know from the full_voters_data results that the max amount of votes by one address is less than 20000 where is no need to change this part of the query
    body = f'{{ votes(first: 20000, where: {{space: "aave.eth",  voter: "0x070341aA5Ed571f0FB2c4a5641409B1A46b4961b"}}, orderBy: "created", orderDirection: asc) {{voter}} }}'
    response = requests.get(url=url, json={"query": body})
    print(response)
    votes = response.json()["data"]["votes"]
    voter = (address, len(votes))
    return voter


full_voters_data(skip_entry)

sorted_voters = sorted(voters_dict.items(), key=operator.itemgetter(1), reverse=True)
raw_most_active_20 = sorted_voters[0:20]
most_active_20 = [voter[0] for voter in raw_most_active_20]

part_rate_20 = [participation_rate(voter, votes_amount) for voter in raw_most_active_20]

#University of Pennsylvania blockchain student organization
up_address = "0x070341aA5Ed571f0FB2c4a5641409B1A46b4961b"
up_participation = participation_rate(voter_by_adress(up_address), votes_amount)

print(datetime.datetime.now())
print(part_rate_20)
print(up_participation)


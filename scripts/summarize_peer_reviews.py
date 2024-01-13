#!/usr/bin/env python

import yaml
import argparse

parser = argparse.ArgumentParser("summarize_peer_review")
parser.add_argument("data_file", type=str, help="data file with details of peer reviews")

args = parser.parse_args()

reviews = yaml.safe_load(open(args.data_file))

years = list(set([ x["year"] for x in reviews]))

for y in reversed(sorted(years)):
    print("Year: ", y)
    year_reviews = [ x for x in reviews if x["year"] == y ]
    journals = set([ x["journal"] for x in year_reviews])
    for j in journals:
        nj = sum(1 for x in year_reviews if x["journal"] == j)
        print(f"  {j}: {nj:d}")

print()
print()
print("All Years")
journals = set([ x["journal"] for x in reviews])
for j in journals:
    nj = sum(1 for x in reviews if x["journal"] == j)
    print(f"  {j}: {nj:d}")
print("Total number of reviews: ", len(reviews))

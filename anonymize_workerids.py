#!/usr/bin/env python
# Run this from repo root to anonymize workerids in production-results directory

import os, json

if not os.path.isdir("./production-results"):
    error("Directory 'production-results' not found! Run this from the root directory of your project or check that you have data stored by cosub correctly.")

hits = os.listdir("./production-results/")

hitlist = open("./production-results/anonymized-results-key.csv", "w")
hitlist.write("WorkerId,AnonId\n")

if not os.path.isdir("./anonymized-results/"):
    os.mkdir("./anonymized-results")

for hitnum, hit in enumerate(hits):
    if hit.endswith(".json"):
        hitdata = json.load(open("./production-results/" + hit))
        workerid = hitdata["WorkerId"]
        hitdata["WorkerId"] = "anon" + str(hitnum)
        anonfile = open("./anonymized-results/anon-" + str(hitnum) + ".json","w")
        json.dump(hitdata, anonfile)
        hitlist.write(workerid + ",anon-" + str(hitnum) + "\n")

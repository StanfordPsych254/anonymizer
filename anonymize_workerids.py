#!/usr/bin/env python
# Run this from repo root to anonymize workerids in production-results directory

import os, sys, json

target_dir = sys.argv[1] if len(sys.argv) >= 2 else "."

if not os.path.isdir(target_dir + "/production-results"):
    raise ValueError("\n\nDirectory 'production-results' not found at " + target_dir + "! \n\nRun this from the root directory of your project or check that you have data stored by cosub correctly.")

hits = os.listdir(target_dir + "/production-results/")

hitlist = open(target_dir + "/production-results/anonymized-results-key.csv", "w")
hitlist.write("WorkerId,AnonId\n")

if not os.path.isdir(target_dir + "/anonymized-results/"):
    os.mkdir(target_dir + "/anonymized-results")

for hitnum, hit in enumerate(hits):
    if hit.endswith(".json"):
        hitdata = json.load(open(target_dir + "/production-results/" + hit))
        workerid = hitdata["WorkerId"]
        hitdata["WorkerId"] = "anon" + str(hitnum)
        anonfile = open(target_dir + "/anonymized-results/anon-" + str(hitnum) + ".json","w")
        json.dump(hitdata, anonfile)
        anonfile.close()
        hitlist.write(workerid + ",anon-" + str(hitnum) + "\n")

hitlist.close()


"""
#!/usr/bin/env python
anonymize.py
"""

import os, sys, json
import pdb

def anonymize_ids_in_target_dir(target_dir):
    ## Get dir contents
    hits = os.listdir(target_dir)
    ## Create new csv file as key to anonymized results
    hitlist = open(target_dir +  "-anonymized-results-key.csv", "w")
    hitlist.write("WorkerId,AnonId\n")
    
    ## Anonymized data dir
    if not os.path.isdir(target_dir + "-anonymized-results/"):
        os.mkdir(target_dir + "-anonymized-results")

    for hitnum, hit in enumerate(hits):
        if hit.endswith(".json"):
            hitdata = json.load(open(target_dir + "/" + hit))
            workerid = hitdata["WorkerId"]
            hitdata["WorkerId"] = "anon" + str(hitnum)
            anonfile = open(target_dir + "-anonymized-results/anon-" + str(hitnum) + ".json","w")
            json.dump(hitdata, anonfile)
            anonfile.close()
            hitlist.write(workerid + ",anon-" + str(hitnum) + "\n")

    hitlist.close()

def anonymize_ids_in_child_dirs(parent_dir):
    sub_dirs = os.listdir(parent_dir)
    for sub_dir in sub_dirs:
        if os.path.isdir(sub_dir):
            anonymize_ids_in_target_dir(sub_dir)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) >= 2 else "."
    if target_dir == ".":
        print("Currently looking for sub-directories to anonymize...")
        anonymize_ids_in_child_dirs(target_dir)
    else:
        print("Currently anonymizing files in " + target_dir)
        anonymize_ids_in_target_dir(target_dir)
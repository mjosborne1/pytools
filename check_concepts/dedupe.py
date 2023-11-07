import pathlib
import sys
from collections import OrderedDict

## Function to De dupe a Snap2SNOMED source map file
def dedupe_sourcefile(tsvfilepath,tsvfinalpath):
   ## Create an empty dictionary and populate with test codes and test names
   ## any duplicates are added as synonyms in a new file along with the orignal code and name
   tests = OrderedDict()
   if pathlib.Path(tsvfilepath).is_file():
        with open(tsvfilepath) as fin:
            for line in fin:
                cols = line.split("\t")
                key = cols[0].strip()
                val = cols[1].rstrip()
                if tests.get(key) == None:
                    tests[key] = val
                else:
                    tests[key] = tests[key] +"\t"+ val
        with open(tsvfinalpath,"w+") as fout:
            fout.write("Test Code\tTest Name\tSynonyms")
            for key in tests:
                fout.write(key+"\t"+tests[key]+"\n")
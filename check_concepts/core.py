import pathlib
import sys

from helpers import get_json_files,search_json_file
from dedupe import dedupe_sourcefile

## 1. Function to find deprecated concepts in an IG
def find_deprecated_concepts(srch_path):
    # Create the Pathling context
    #pc = PathlingContext.create()

    # Get O/S specific Path object using pathlib
    root_path=pathlib.Path(srch_path)
    
    # Get all json files
    file_list = get_json_files(root_path)
    for f in file_list:
        print("---Checking %s\n" % f)
        search_json_file(f)


def main():
    # Pass this in as an argument
    ##srch_path="/Users/osb074/Development/hl7au/au-fhir-base/output"
    default_path="/Users/osb074/tmp"
    print("1. Find deprecated concepts ")
    val = input("2. De-dupe a Snap2SNOMED source map: ")
    if (val == "1"): 
        srch_path="/Users/osb074/tmp"
        find_deprecated_concepts(srch_path)
        sys.exit()
    if (val == "2"):
        fpath = input("   Enter file path (default=/Users/osb074/tmp) :")
        if fpath=="":
            fpath = default_path
        fname = input("   Enter tsv file name (*.txt):")
        tsvfilepath = pathlib.PurePosixPath(fpath,fname)
        tsvfinalpath= pathlib.PurePosixPath(fpath,"deduped"+fname)
        dedupe_sourcefile(tsvfilepath,tsvfinalpath)
        sys.exit()
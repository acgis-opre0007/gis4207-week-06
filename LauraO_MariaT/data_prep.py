import arcpy
import os
from sys import argv

def main():
    if len(sys.argv) !=4:
        print(f"Usage: data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>")
        sys.exit(1)
    
    if not arcpy.Exists(file):
        print(f"File does not exist")
        sys.exit(2)

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False


        return UTMZone10

if __name__ == '__main__':
    GdbsToFds(*argv[1:])

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

    in_gdbs_base_folder = sys.argv[1] #C:\acgis\gis4207\data\Surrey
    out_gdb = sys.argv[2]
    out_feature_dataset = sys.argv[3] 

    arcpy.env.overwriteOutput = True

    file_gdb = arcpy.CreateFileGDB_management(out_gdb, out_feature_dataset)
    gdb_name = 'surrey.gdb'
    arcpy.env.workspace = in_gdbs_base_folder
    gdb_list = arcpy.ListWorkspaces(in_gdbs_base_folder)
    for gdb in gdb_list:
        desc = arcpy.Describe(gdb)
        print(f"{gdb_list}")

    arcpy.EnvManager.SetEnvironment("workspace", in_gdbs_base_folder)

    arcpy.management.CreateFeatureDataset_management(out_gdb, out_feature_dataset)

    #desc = arcpy.Describe()
    #sr = desc.spatialReference

if __name__ == '__main__':
    main(*argv[1:])   
    # GdbsToFds(*argv[1:])

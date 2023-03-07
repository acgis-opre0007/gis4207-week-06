import os
import sys
import arcpy
from arcpy import env 

def main():
    if len(sys.argv) !=4:
        print(f"Usage: data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>")
        sys.exit() 
        
    in_gdbs_folder = sys.argv[1]
    out_gdb = sys.argv[2]
    out_feature_dataset = sys.argv[3] 
    
    if not arcpy.Exists(in_gdbs_folder):
        print(in_gdbs_folder,"Does does not exist")
        sys.exit() 
        
    arcpy.env.overwriteOutput = True
    
    Geodatabase_path = arcpy.CreateFileGDB_management(in_gdbs_folder,out_gdb)[0]
    arcpy.env.workspace = in_gdbs_folder
    
    workspace_path = arcpy.ListWorkspaces()
    arcpy.env.workspace = ws
    for ws in workspace_path[:1]:
        FeatureClass_List = arcpy.ListFeatureClasses()
        desc = arcpy.Describe(FeatureClass_List) 
             
    sr = desc.SpatialReference
        
    FeatureClass_path = arcpy.CreateFeatureDataset_management(Geodatabase_path, out_feature_dataset,sr)[0]
    
    arcpy.env.workspace = ws
    for ws in workspace_path[:1]:
       featureClasses = arcpy.ListFeatureClasses
       desc = arcpy.Describe(featureClasses[0])
       arcpy.FeatureClassToFeatureClass_conversion(in_feature = featureClasses[0], out_feature = FeatureClass_path, out_name = f"{desc.baseName}")
    
    print(Geodatabase_path,"was created")   
    print(FeatureClass_path, "was created") 
               

if __name__ == '__main__':
        main( ) 
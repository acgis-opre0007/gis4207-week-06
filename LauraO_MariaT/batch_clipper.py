import sys
import os.path
import arcpy


def main():

    if len(sys.argv) !=4:
        print("Usage: batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>")
        sys.exit()
    
    arcpy.env.overwriteOutput = True
    
    In_Workspace = sys.argv[1]
    Clip_Workspace = sys.argv[2]
    Out_Workspace = sys.argv[3] 

    arcpy.env.workspace = In_Workspace
    In_Featclass = arcpy.ListFeatureClass()
        
    arcpy.env.workspace = Clip_Workspace
    for Clip_FC in arcpy.ListFeatureClass():
        for FClass in In_Featclass:
            new_name = Clip_FC.split('.') + "_" + FClass.split('.')[0]
            arcpy.analyze.Clip(os.path.join(In_Workspace, FClass), os.path.join(Clip_Workspace, Clip_FC), Out_Workspace + '\\' + new_name)
                  
    if __name__ == "__main__":
         main()
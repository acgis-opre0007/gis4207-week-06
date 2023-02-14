import sys
import arcpy
import os

arcpy.env.workspace = r'..\..\..\data'

sites = r'..\..\..\data\BatchClipData\Sites'
clip = r'..\..\..\data\BatchClipData\TargetData'
out = r'..\..\..\data\BatchClipData\output'

feature_class = arcpy.ListFeatureClasses()
for fc in feature_class:
    fc_des = arcpy.Describe(feature_class)
    print(fc_des)



for fc in feature_class:
    arcpy.CopyFeatures_management(
        fc, os.path.join(out, os.path.splitext(fc)[0]))
    os.path.join()
    print(fc)

def main():

    if len(sys.argv) !=4:
        print("Usage: batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>")
        sys.exit()
    
    if not arcpy.Exists(arcpy.env.workspace):
        print("The feature class does not exist")
        sys.exit()

    InWorkspace = sys.argv[1]
    ClipWorkspace = sys.argv[2]
    OutWorkspace = sys.argv[3] 

def clip_analysis(in_features, clip_features, out_features):
    in_features = "CaribouLower.shp"
    clip_features = "A1.shp", "A2.shp", "A3.shp"
    out_features = out

    arcpy.analysis.Clip(in_features,  clip_features, out_features)
    

if __name__ == "__main__":
    main()
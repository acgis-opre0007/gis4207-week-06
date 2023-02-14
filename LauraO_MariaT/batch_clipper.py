import sys
import os

#arcpy.env.workspace = r'..\..\..\..\data\BatchClipData'

def main():

    global arcpy, env

    if len(sys.argv) !=4:
        print("Usage: batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>")
        sys.exit()
    
    #if not arcpy.Exists(file):
        #print("The feature class does not exist")
        #sys.exit()

    import arcpy
    from arcpy import env

    In_Workspace = sys.argv[1]
    Clip_Workspace = sys.argv[2]
    Out_Workspace = sys.argv[3] 

    env.workspace = In_Workspace
    fc_list = []
    in_F_class = arcpy.ListFeatureClasses()
    for fc in in_F_class:
        fc_list.append(fc)
        print(os.path.join(os.path.abspath(In_Workspace), fc))
        
    env.workspace = Clip_Workspace
    clip_F_class = arcpy.ListFeatureClasses()
    for fc_clip in clip_F_class:
        #nested for loop
        print(fc_clip)
        print(os.path.join(os.path.abspath(Clip_Workspace), fc_clip))

    env.workspace = Out_Workspace
    out_f_class = arcpy.ListFeatureClasses()
    for fc_out in out_f_class:
        print(fc_out)
        print(os.path.join(os.path.abspath(Out_Workspace), fc_out))
    
    clip_analysis(in_features, clip_features, out_features)


def clip_analysis(in_features, clip_features, out_features):
    in_features = r'..\..\..\..\data\BatchClipData\TargetData\CaribouLower.shp'
    clip_features = r'..\..\..\..\data\BatchClipData\Sites'
    out_features = r'..\..\..\..\data\BatchClipData\output'

    arcpy.analysis.Clip(in_features, clip_features, out_features)
    for fc in clip_features:
        print(os.path.join(os.path.abspath(in_features, fc)))
    

if __name__ == "__main__":
    main()
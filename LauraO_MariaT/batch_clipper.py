import sys
import arcpy

arcpy.env.workspace = r'..\..\..\data'

sites = r'..\..\..\data\BatchClipData\Sites'
clip = r'..\..\..\data\BatchClipData\TargetData'
out = r'..\..\..\data\BatchClipData\outfeatures'

def main():

    if len(sys.argv) !=3:
        print("Usage: batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>")
        sys.exit()

    in_features = sys.argv[1]
    clip_features = sys.argv[2]
    out_features = sys.argv[3] 

def clip_analysis(InWorkspace, ClipWorkspace, OutWorkspace):
    arcpy.clip_analysis(InWorkspace=clip, ClipWorkspace=sites, OutWorkspace=out)


arcpy.analysis.Clip("A1.shp", "A2.shp", "A3.shp")
    

if __name__ == "__main__":
    main()
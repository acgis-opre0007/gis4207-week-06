import sys
import os.path
import arcpy


def main():
    #run these 4 lines in terminal with shift+enter
    base_path = os.path.abspath('../../../../data/BatchClipData')
    in_path = os.path.join(base_path, 'sites')
    out_path = os.path.join(base_path, 'output')

    command = f'python batch_clipper.py "{base_path}" "{in_path}" "{out_path}"'
    #then type "command" + hit enter. result is the command line input to run this script

    if len(sys.argv) !=4:
        print("Usage: batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>")
        sys.exit()

    In_Workspace = sys.argv[1]
    Clip_Workspace = sys.argv[2]
    Out_Workspace = sys.argv[3] 

    arcpy.env.workspace = In_Workspace
    arcpy.env.overwriteOutput = True

    Target_FCs = arcpy.ListFeatureClasses("*", "*", In_Workspace)
    if not Target_FCs:
        print("No feature classes found in the input workspace.")
        sys.exit()

    Clip_FCs = arcpy.ListFeatureClasses("*", "Polygon", Clip_Workspace)
    if not Clip_FCs:
        print("No polygon feature classes found in the clip workspace.")
        sys.exit()

    for Clip_FC in Clip_FCs:
        for Target_FC in Target_FCs:
            In_FC = os.path.join(In_Workspace, Target_FC)
            Clip_FC = os.path.join(Clip_Workspace, Clip_FC)
            Out_FC = os.path.join(Out_Workspace, f"{Clip_FC}_{os.path.splitext(In_FC)[0]}.shp")
            arcpy.Clip_analysis(In_FC, Clip_FC, Out_FC)


if __name__ == "__main__":
    main()
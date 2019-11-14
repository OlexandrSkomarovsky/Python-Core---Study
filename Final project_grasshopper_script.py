"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""
        
__author__ = "User"
__version__ = "2019.10.11"
        
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghc
import ghpythonlib.treehelpers as th
import Rhino
        
        
def main(height, thickness, length_drywall, *baseline):
    #list to fill with detailed wall geometry
    
    walldet = []
            
    #create a wall for each curve
    for line in baseline:
        #list to fill in iteration
        profile_thickness = thickness -25
        wall = []
        offsets = map(lambda x: ghc.OffsetCurve(line, x/2, rg.Plane.WorldXY, 0), [profile_thickness, -profile_thickness])
        wallbase = ghc.EdgeSurface(offsets[0], offsets[1])
        
        #list of horizontal profiles
        profile_lower = ghc.Extrude(wallbase, ghc.VectorXYZ(0,0,profile_thickness/2)[0])
        profile_upper = (ghc.Move(profile_lower, ghc.VectorXYZ(0,0,height-(profile_thickness/2))[0]))[0]
        wall += profile_lower
        wall += profile_upper
        
#        list of vertical profiles
        nums_ancer = map(lambda x: x/length_drywall, ghc.Length(line))
#        ancer_pt = (ghc.DivideCurve(line, nums_ancer, False))[0]
#        ancer_pts = map(lambda x: rg.Point3d(x),ancer_pt) 
        frame_horizontal = (ghc.HorizontalFrames(line, nums_ancer))[0]
        frame_horizontal = (ghc.Move(frame_horizontal, ghc.VectorXYZ(0,0,height/2)[0]))[0]
        vertical_profiles = map(lambda base: ghc.CenterBox(base, profile_thickness/2, profile_thickness/2, (height-profile_thickness)/2), frame_horizontal)   
        wall += vertical_profiles
        
#        list of drywall 
        drywall_base = map(lambda x,d_th: ghc.OffsetCurve(x, d_th, rg.Plane.WorldXY, 0), offsets,[12.5, -12.5])
        drywall_base = ((ghc.EdgeSurface(offsets[0], drywall_base[0])) + (ghc.EdgeSurface(offsets[1], drywall_base[1])))
        drywall = map(lambda x: ghc.Extrude(x, ghc.VectorXYZ(0,0,height)[0]), offsets)
        print drywall
        wall += drywall[0]
        
#        


        #add wall to output list
        walldet += wall
        
    return walldet
        
#run script if curve input
if wallBaseline:
    #set data if no user input
    wheight = wallHeight if wallHeight else 3000
    wthickness = wallThickness if wallThickness else 300
    w_length_drywall = max_Length_drywall if max_Length_drywall else 600
            
    #wallbaseline is set as centerline of wall
    wallDetailed = main(wheight, wthickness, w_length_drywall, wallBaseline)

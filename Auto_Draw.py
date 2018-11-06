############################################################################################
#   Script to auto Generate the Drawings.
###########################################################################################

import FreeCAD
import TechDraw

#-----------------------------------------------------------------------------------------

#The selected part in GUI is given a name

Target = Gui.Selection.getSelectionEx()[0]
#-----------------------------------------------------------------------------------------

#function to add new document(page)


def New_page():
    App.activeDocument().addObject('TechDraw::DrawPage','Drawing')
    App.activeDocument().addObject('TechDraw::DrawSVGTemplate','Template')
    App.activeDocument().Template.Template = '/usr/share/freecad/Mod/TechDraw/Templates/A2_Landscape_ISO7200TD.svg'
    App.activeDocument().Drawing.Template = App.activeDocument().Template
    #EoF

#-----------------------------------------------------------------------------------------
#Assigning value of boundary of box of Target(Object)

Length = Target.Object.Shape.BoundBox.XMax
Height = Target.Object.Shape.BoundBox.ZMax
Width = Target.Object.Shape.BoundBox.YMax

#Assigning scaling values
Sc0 = (550)/(Length)
Sc1 = (400)/(Height)
Sc2 = (400)/(Width)
    
Scale0 = Sc0

if Scale0 > Sc1 :
   Scale0 = Sc1

if Scale0 > Sc2 :
   Scale0 = Sc2

#-----------------------------------------------------------------------------------------
#Assigning Position coordinates
Scale = Scale0/4

TopX = 40+Scale*Length
TopY = 30+Scale*Width

FrontX = 40+Scale*Length
FrontY = 30+3*Scale*Width

RightX = 40+4*Scale*Length
RightY = 30+3*Scale*Width


#-----------------------------------------------------------------------------------------    

#function to add the top views of object.

def Top_view(): 
    App.activeDocument().addObject('TechDraw::DrawViewPart','topView')
    App.activeDocument().topView.Source = Target.Object
    App.activeDocument().Drawing.addView(App.activeDocument().topView)
    App.activeDocument().topView.Direction = (0,0,1)
    App.activeDocument().topView.X = TopX
    App.activeDocument().topView.Y = TopY
    App.activeDocument().topView.Scale = Scale
    #EoF
#----------------------------------------------------------------------------------------
#Create FrontView

def Front_view():
    App.activeDocument().addObject('TechDraw::DrawViewPart','FrontView')
    App.activeDocument().FrontView.Source = Target.Object
    App.activeDocument().Drawing.addView(App.activeDocument().FrontView)
    App.activeDocument().FrontView.Direction = (0,-1,0)
    App.activeDocument().FrontView.X = FrontX
    App.activeDocument().FrontView.Y = FrontY
    App.activeDocument().FrontView.Scale = Scale
    #EoF

##----------------------------------------------------------------------------------------
#Create RightView


def Side_view():
    App.activeDocument().addObject('TechDraw::DrawViewPart','SideView')
    App.activeDocument().SideView.Source = Target.Object
    App.activeDocument().Drawing.addView(App.activeDocument().SideView)
    App.activeDocument().SideView.Direction = (1,0,0)
    App.activeDocument().SideView.X = RightX
    App.activeDocument().SideView.Y = RightY
    App.activeDocument().SideView.Scale = Scale
    #EoF
   

#---------------------------------------------------------------------------------------

#Create IsotView

def Iso_view():    
    App.activeDocument().addObject('TechDraw::DrawViewPart','IsoView')
    App.activeDocument().IsoView.Source = Target.Object
    App.activeDocument().Drawing.addView(App.activeDocument().IsoView)
    App.activeDocument().IsoView.Direction = (1,1,1)
    App.activeDocument().IsoView.X = RightX
    App.activeDocument().IsoView.Y = TopY
    App.activeDocument().IsoView.Scale = Scale
    
#----------------------------------------------------------------------------------------
#Calling of functions

New_page()
Top_view()
Front_view()
Side_view()
Iso_view()


############################################################################################
#Script ends
############################################################################################


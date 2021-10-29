# NX 1969
# Journal created by Wesoly on Thu Oct  7 10:21:18 2021 W. Europe Daylight Time
#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Drafting
import NXOpen.Drawings
import NXOpen.MenuBar
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theUI = NXOpen.UI.GetUI()
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "break")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    verticalOrdinateDimension1 = theUI.SelectionManager.GetSelectedObject(0)
    #for object in verticalOrdinateDimension1:
    objects1[0] = verticalOrdinateDimension1
    editSettingsBuilder1 = workPart.SettingsManager.CreateAnnotationEditSettingsBuilder(objects1)
    
    dimensionlinearunits1 = editSettingsBuilder1.AnnotationStyle.UnitsStyle.DimensionLinearUnits
    
    editsettingsbuilders1 = [NXOpen.Drafting.BaseEditSettingsBuilder.Null] * 1 
    editsettingsbuilders1[0] = editSettingsBuilder1
    workPart.SettingsManager.ProcessForMultipleObjectsSettings(editsettingsbuilders1)
    
    editSettingsBuilder1.AnnotationStyle.BreakSettings.CreateBreaks = True
    
    editSettingsBuilder1.AnnotationStyle.BreakSettings.BreakSize = 2.5
    
    nXObject1 = editSettingsBuilder1.Commit()
    
    editSettingsBuilder1.Destroy()
    
    
if __name__ == '__main__':
    main()

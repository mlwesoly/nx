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
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "toleranz")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    number = theUI.SelectionManager.GetNumSelectedObjects()
    
    for i in range(0,number):
        Dimension1 = theUI.SelectionManager.GetSelectedObject(i)
        objects1 = Dimension1
        editSettingsBuilder1 = workPart.SettingsManager.CreateAnnotationEditSettingsBuilder([objects1])
    
        dimensionlinearunits1 = editSettingsBuilder1.AnnotationStyle.UnitsStyle.DimensionLinearUnits

        dimtolerancetype1 = editSettingsBuilder1.AnnotationStyle.DimensionStyle.ToleranceType
    
        editSettingsBuilder1.AnnotationStyle.DimensionStyle.ToleranceType = NXOpen.Annotations.ToleranceType.Basic
 
        nXObject1 = editSettingsBuilder1.Commit()
    
        editSettingsBuilder1.Destroy()
    
    
if __name__ == '__main__':
    main()

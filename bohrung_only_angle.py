import re
import NXOpen
import NXOpen.Annotations
import NXOpen.Drafting
import NXOpen.Drawings
import NXOpen.UF

def main() :
    debug = 0
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    theUI = NXOpen.UI.GetUI()
    lw = theSession.ListingWindow
    
    theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Vor_Skript")
    
    displayPart = theSession.Parts.Display
    views = workPart.DraftingViews
    draftingdrawings = workPart.DraftingDrawingSheets

    sheets = workPart.DrawingSheets
    selectedObj = theUI.SelectionManager.GetSelectedObject(0)
    numSelectedObj = theUI.SelectionManager.GetNumSelectedObjects()

    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Redefine Feature")

    lw.Open()
    notes = workPart.Notes
    symbols = workPart.Annotations.IdSymbols
    
    for i in range(numSelectedObj):
        holePackage1 = theUI.SelectionManager.GetSelectedObject(i)
        holePackageBuilder1 = workPart.Features.CreateHolePackageBuilder(holePackage1)
        holePackageBuilder1.DrillSizeTipAngle.SetFormula("118")
        nXObject1 = holePackageBuilder1.Commit()
        holePackageBuilder1.HolePosition.CleanMappingData()
        holePackageBuilder1.Destroy()
        #lw.WriteLine(str(type(theUI.SelectionManager.GetSelectedObject(i))))
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId1)
    theSession.Preferences.Modeling.UpdatePending = False
    lw.Close()
    # theSession.CleanUpFacetedFacesAndEdges()

if __name__ == '__main__':
    main()

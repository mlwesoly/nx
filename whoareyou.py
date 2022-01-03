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
    theUFSession = NXOpen.UF.UFSession.GetUFSession()
    theUI = NXOpen.UI.GetUI()
    lw = theSession.ListingWindow
    
    theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Vor_Skript")
    
    displayPart = theSession.Parts.Display
    views = workPart.DraftingViews
    draftingdrawings = workPart.DraftingDrawingSheets

    sheets = workPart.DrawingSheets
    selectedObj = theUI.SelectionManager.GetSelectedObject(0)
    numSelectedObj = theUI.SelectionManager.GetNumSelectedObjects()
    
    lw.Open()
    notes = workPart.Notes
    symbols = workPart.Annotations.IdSymbols
    
    for i in range(numSelectedObj):
        selObj = theUI.SelectionManager.GetSelectedObject(i)
        objType = type(theUI.SelectionManager.GetSelectedObject(i))
        lw.WriteLine(str(objType))
        for dir_obj in dir(i):
            lw.WriteLine(str(dir_obj))
        lw.WriteLine(str(i.Name))
        lw.WriteLine("\n")
        #lw.WriteLine(str(isinstance(objType, NXOpen.Annotations.Note)))
        #if isinstance(objType, NXOpen.Annotations.Note):
        #    lw.WriteLine("jo")
        #    if objType.GetText().find("VWLETTER_DISP")>0:
        #        lw.WriteLine(str(objType.GetText()))
        #if selObj.GetText()[0].find("VWNAME")>0:
        #    lw.WriteLine(str(selObj.GetText()))
        lw.WriteLine(selObj.SectionViewParent.Name)
    
    # ajdust this part, for make it working in general
    #for sheet in workPart.DrawingSheets:
    #sheet.Open()
    #for obj in sheet.View.AskVisibleObjects(): 
    #        for j in dir(obj):
    #            lw.WriteLine(str(j))
    #        lw.WriteLine(str(obj.Name))
    #        lw.WriteLine("\n")
  
    lw.Close()
    # theSession.CleanUpFacetedFacesAndEdges()

if __name__ == '__main__':
    main()

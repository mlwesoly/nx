import math
import NXOpen
import NXOpen.Features
import NXOpen.Layer
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    sketches = workPart.Sketches
    lw = theSession.ListingWindow
    lw.Open()
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Move Layer")
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    displayModification1.NewLayer = 20
    
    for sketch in sketches:
        displayModification1.Apply([sketch])
    
    displayModification1.Dispose()

    displayModification2 = theSession.DisplayManager.NewDisplayModification()
    displayModification2.NewLayer = 40
   
    datums = workPart.Datums
    for datum in datums:
         if (datum.Layer < 2):
             lw.WriteLine(str(datum.Layer))
             #lw.WriteLine(str(isinstance(datum,NXOpen.DatumPlane)))
             displayModification2.Apply([datum])

    displayModification2.Dispose()

    stateArray1 = [None] * 1 
    stateArray1[0] = NXOpen.Layer.StateInfo()
    stateArray1[0] = NXOpen.Layer.StateInfo(20, NXOpen.Layer.State.Hidden)
    workPart.Layers.ChangeStates(stateArray1, False)
    stateArray1[0] = NXOpen.Layer.StateInfo(40, NXOpen.Layer.State.Hidden)
    workPart.Layers.ChangeStates(stateArray1, False)

    if displayPart.WCS.Visibility:
        displayPart.WCS.Visibility = False
    
    lw.Close()
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId2, "Layer-Einstellungen-Dialogfenster")
    
    theSession.SetUndoMarkName(markId2, "Layer-Einstellungen")
    
    theSession.DeleteUndoMark(markId2, None)

    
if __name__ == '__main__':
    main()


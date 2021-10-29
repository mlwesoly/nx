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
    lw.Open()
    theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Vor_Skript")

    symbols = workPart.Annotations.IdSymbols
    
    for symbol in symbols:
        editSettingsBuilder1 = workPart.SettingsManager.CreateAnnotationEditSettingsBuilder([symbol])
        editsettingsbuilders1 = [NXOpen.Drafting.BaseEditSettingsBuilder.Null] * 1
        editsettingsbuilders1[0] = editSettingsBuilder1
        workPart.SettingsManager.ProcessForMultipleObjectsSettings(editsettingsbuilders1)
        editSettingsBuilder1.AnnotationStyle.LetteringStyle.GeneralTextSize = 5.0
        editSettingsBuilder1.AnnotationStyle.SymbolStyle.IdSymbolSize = 15.0
        editSettingsBuilder1.AnnotationStyle.SymbolStyle.IdSymbolWidth = NXOpen.Annotations.LineWidth.Four
        
        nXObject1 = editSettingsBuilder1.Commit()
        editSettingsBuilder1.Destroy()

    lw.Close()
    theSession.CleanUpFacetedFacesAndEdges()

if __name__ == '__main__':
    main()

import re
import NXOpen
import NXOpen.Annotations
import NXOpen.Drafting
import NXOpen.Drawings
import NXOpen.UF

def main() :
    debug = 2
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    theUI = NXOpen.UI.GetUI()
    lw = theSession.ListingWindow
  
    theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible,"Vor_Skript")
  
    displayPart = theSession.Parts.Display
    views = workPart.DraftingViews
    draftingdrawings = workPart.DraftingDrawingSheets

    sheets = workPart.DrawingSheets
    #for sheet in sheets:
    #    lw.WriteLine(str(sheet.Height))
  
    lw.Open()
    notes = workPart.Notes
    symbols = workPart.Annotations.IdSymbols
   
    sizemm = 3.5
    factorLabels = 1.4285714285
    factorfont = 1.0

    layerlist = [110]


    for view in views:
        #editViewSettingsBuilder1.ViewDetailLabel.LabelCharacterHeightFactor = factorLables
        #editViewSettingsBuilder1.ViewDetailLabel.ScaleCharacterHeightFactor = factorfont
        if isinstance(view,NXOpen.Drawings.BaseView):
            #lw.WriteLine("Baseview\n")
            editViewSettingsBuilder1 = workPart.SettingsManager.CreateDrawingEditViewSettingsBuilder([view])
            editViewSettingsBuilder1.ViewLabel.LabelCharacterHeightFactor = factorfont #factorLabels 
            editViewSettingsBuilder1.ViewLabel.ScaleCharacterHeightFactor = factorfont * 0.7
            nXObject1 = editViewSettingsBuilder1.Commit()
            editViewSettingsBuilder1.Destroy()
        elif isinstance(view,NXOpen.Drawings.DetailView):
            #lw.WriteLine("Detailview\n")
            editViewSettingsBuilder1 = workPart.SettingsManager.CreateDrawingEditViewSettingsBuilder([view])
            editViewSettingsBuilder1.ViewDetailLabel.LabelCharacterHeightFactor = factorLabels
            editViewSettingsBuilder1.ViewDetailLabel.ScaleCharacterHeightFactor = factorfont
            nXObject1 = editViewSettingsBuilder1.Commit()
            editViewSettingsBuilder1.Destroy()
        elif isinstance(view,NXOpen.Drawings.ProjectedView):
            #lw.WriteLine("Projected\n")
            editViewSettingsBuilder1 = workPart.SettingsManager.CreateDrawingEditViewSettingsBuilder([view])
            editViewSettingsBuilder1.ViewProjectedLabel.LabelCharacterHeightFactor = 1.5
            editViewSettingsBuilder1.ViewProjectedLabel.ScaleCharacterHeightFactor = 1.0
            editViewSettingsBuilder1.ViewStyle.ViewProjectedArrowSettings.SizeFactor = factorLabels
            #editViewSettingsBuilder1.ViewDetailLabel.ScaleCharacterHeightFactor = factorfont
            nXObject1 = editViewSettingsBuilder1.Commit()
            editViewSettingsBuilder1.Destroy()
        elif isinstance(view,NXOpen.Drawings.SectionView):
            #lw.WriteLine("Section\n")
            editViewSettingsBuilder1 = workPart.SettingsManager.CreateDrawingEditViewSettingsBuilder([view])
            editViewSettingsBuilder1.ViewSectionLabel.LabelCharacterHeightFactor = factorLabels
            nXObject1 = editViewSettingsBuilder1.Commit()
            editViewSettingsBuilder1.Destroy()


    #lw.WriteLine("\n-> notes:\n")
    a = []
    for note in notes:
        a.append(note)

    seen = {}
    dupes = []
    for x in a:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    
    for note in notes:
        if note.Layer in layerlist:
            if note.GetText()[0].find("VWNAME") > 0:
                editViewLabelSettingsBuilder1 = workPart.SettingsManager.CreateAnnotationEditSettingsBuilder([note])
                #workPart.SettingsManager.ProcessForMultipleObjectsSettings([editViewLabelSettingsBuilder1])
                editViewLabelSettingsBuilder1.AnnotationStyle.LetteringStyle.GeneralTextSize = 5.0
                nXObject1 = editViewLabelSettingsBuilder1.Commit()
                editViewLabelSettingsBuilder1.Destroy()
            else:
                editViewLabelSettingsBuilder1 = workPart.SettingsManager.CreateAnnotationEditSettingsBuilder([note])
                #workPart.SettingsManager.ProcessForMultipleObjectsSettings([editViewLabelSettingsBuilder1])
                editViewLabelSettingsBuilder1.AnnotationStyle.LetteringStyle.GeneralTextSize = 3.5
                nXObject1 = editViewLabelSettingsBuilder1.Commit()
                editViewLabelSettingsBuilder1.Destroy()


    workPartdp = theSession.Parts.Display
    labels = workPart.Labels
    # notes with a leader (arrow to object) become a leader
    #lw.WriteLine("\n-> Labels:\n")
    for label in labels:
        editSettingsBuilder1 = workPart.SettingsManager.CreateAnnotationEditSettingsBuilder([label])
        editSettingsBuilder1.AnnotationStyle.LetteringStyle.GeneralTextSize = 3.5
        editSettingsBuilder1.AnnotationStyle.LineArrowStyle.FirstArrowheadWidth = NXOpen.Annotations.LineWidth.Four
        nXObject1 = editSettingsBuilder1.Commit()
        editSettingsBuilder1.Destroy()


    #lw.WriteLine("\n-> ID Symbols:\n")
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

# NX 1969
# Journal created by Wesoly on Mon Oct  4 11:18:08 2021 W. Europe Daylight Time
#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.Drafting
import NXOpen.Drawings
import NXOpen.MenuBar
import NXOpen.PDM
import NXOpen.Positioning

# todo: check if there is already a view with the name 3D-Ansicht
# if so, give that information to the user and stop
#

def main() :
    """ ueber die ausgewaehlte ansicht 3D-Ansicht und den massstab schreiben  """
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theUI = NXOpen.UI.GetUI()
    lw = theSession.ListingWindow
    lw.Open()
    
    #views = workPart.DraftingViews
    #.SheetDraftingViews
    #Drawings.CurrentDrawingSheet
    sheet = workPart.DrawingSheets.CurrentDrawingSheet
    viewscount = 0
    views = sheet.SheetDraftingViews
    for view in views:
        viewscount += 1
    found = 0
    
    if viewscount > 0:
        baseView1 = theUI.SelectionManager.GetSelectedObject(0)
        if (not(baseView1)) :
            lw.WriteLine("bitte Grundansicht auswaehlen")
        elif isinstance(baseView1,NXOpen.Drawings.BaseView):
            for view in views:
                if view.Name == "3D-Ansicht":
                    found = 1
            if found == 0:
                objects2 = [NXOpen.NXObject.Null] * 1 
                objects2[0] = baseView1
                objectGeneralPropertiesBuilder1 = workPart.PropertiesManager.CreateObjectGeneralPropertiesBuilder(objects2)
                objectGeneralPropertiesBuilder1.Name = "3D-Ansicht"
                nXObject1 = objectGeneralPropertiesBuilder1.Commit()
                objectGeneralPropertiesBuilder1.Destroy()
        
                views1 = [NXOpen.View.Null] * 1 
                views1[0] = baseView1
                editViewSettingsBuilder1 = workPart.SettingsManager.CreateDrawingEditViewSettingsBuilder(views1)
                editsettingsbuilders1 = [NXOpen.Drafting.BaseEditSettingsBuilder.Null] * 1 
                editsettingsbuilders1[0] = editViewSettingsBuilder1
                workPart.SettingsManager.ProcessForMultipleObjectsSettings(editsettingsbuilders1)
                editViewSettingsBuilder1.ViewLabel.ShowViewScale = True
                editViewSettingsBuilder1.ViewLabel.ShowViewLabel = True
                editViewSettingsBuilder1.ViewLabel.CustomizedViewLabel = False
                editViewSettingsBuilder1.ViewLabel.ScalePosition = NXOpen.Drawings.ScalePositionTypes.Below
                nXObject2 = editViewSettingsBuilder1.Commit()
                editViewSettingsBuilder1.Destroy()
            else:
                lw.WriteLine("Der Name 3D-Ansicht schon vorhanden")
        else:
            lw.WriteLine("bitte Grundansicht auswaehlen")
    else:
        lw.WriteLine("kein view auf dem Blatt")
    lw.Close()


if __name__ == '__main__':
    main()

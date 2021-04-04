import NXOpen
from NXOpen import Drafting as ds

def main():

    theSession = NXOpen.Session.GetSession()
    theUI = NXOpen.UI.GetUI()
 
    k = NXOpen.NXMessageBox.DialogType.ValueOf(1)
    
    helper = theSession.Parts
    print(helper)
    for partObject in theSession.Parts:
        theUI.NXMessageBox.Show("was fuer ein titel",k,str(partObject))
    #with open('C://a_nx//hello.txt' , 'w') as file:
    #    file.write(str(helper))
    
    for partObject in theSession.Parts:
        theUI.NXMessageBox.Show("was fuer ein titel",k,str(helper))
    
    NXOpen.PartCollection.FileNew()


if __name__ == '__main__':
    main()






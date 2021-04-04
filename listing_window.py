import NXOpen

def main():

    theSession  = NXOpen.Session.GetSession()
    theUI = NXOpen.UI.GetUI()
    
    lw = theSession.ListingWindow
    # Insert code here 
    lw.Open()
    
    lw.WriteLine("hello")
    lw.Close()
    
if __name__ == '__main__':
    main()


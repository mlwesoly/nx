import NXOpen
from NXOpen import Features
from NXOpen import Point3d


def main():
    theUI = NXOpen.UI.GetUI()
    NXSession = NXOpen.Session.GetSession()
    workPart = NXSession.Parts.Work
    nullFeature = NXOpen.Features.Feature.Null
    origin = Point3d(0.0, 0.0, 0.0)
    #**************************************************************************
    # CREATE BLOCK
    newBlock = workPart.Features.CreateBlockFeatureBuilder(nullFeature)
    newBlock.SetOriginAndLengths(origin, "50", "80", "100")
    blockFeature = newBlock.CommitFeature()
    newBlock.Destroy()
    #**************************************************************************
    # EDIT BLOCK
    oldBlock = workPart.Features.CreateBlockFeatureBuilder(blockFeature)
    oldBlock.SetOriginAndLengths(origin, "100", "20", "50")
    oldBlock.Commit()
    oldBlock.Destroy()

if __name__ == '__main__':
    main()

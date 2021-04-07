import NXOpen

def main():
    NXSession = NXOpen.Session.GetSession()
    for partObject in NXSession.Parts:
        processPart(partObject)
    
    def processPart(partObject):
        for bodyObject in partObject.Bodies:
            processBodyFaces(bodyObject)
            processBodyEdges(bodyObject)
    
    def processBodyFaces(bodyObject):
        for faceObject in bodyObject.GetFaces():
            processFace(faceObject)
    
    def processBodyEdges(bodyObject):
        for edgeObject in bodyObject.GetEdges():
            processEdge(edgeObject)
    
    def processFace(faceObject):
        for edgeObject in faceObject.GetEdges():
            processEdge(edgeObject)
        bodyOfFace = faceObject.GetBody()
    
    def processEdge(edgeObject):
        for faceObject in edgeObject.GetFaces():
            processEdgeFace(faceObject)
        bodyOfEdge = edgeObject.GetBody()
        
if __name__ == "__main__":
    main()
from abc import ABCMeta
class BaseModule(metaclass=ABCMeta):
    def __init__(self, pName, pDescription, pRequest):
         self.name = pName
         self.description = pDescription
         self.parseRequest(pRequest)

    #Allows a custom parser of the web request.
    def parseRequest(self, request):
         pass

    #Allows a custom init for the module.
    def initMod(self):
         pass

    #Allows custom render for the module.
    def render(self):
        pass

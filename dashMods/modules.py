from abc import ABCMeta
class BaseModule(metaclass=ABCMeta):
     def __init__(self, name, description, request):
         self.name = name
         self.description = name

     def parseRequest(self, request):
         pass

     def initMod(self):
         pass

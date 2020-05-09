#!/usr/bin/env python3
from importlib import import_module
from dashMods  import *

class DashBoard:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.Modules = []

    def addModule(self, request):
         if not "ModuleType" in request.form:
             return Response("error", 400)

         type  = request.form["ModuleType"]
         type = type.lower()

         #import class
         mod = __import__('dashMods', globals(), locals(), [type])
         cls = getattr(mod, type)
         cls = getattr(cls, type.capitalize())

         # create new class
         newMod = cls("test", "test description", request)

         #append to dashboard
         self.Modules.append(newMod)

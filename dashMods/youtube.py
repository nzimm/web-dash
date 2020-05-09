from dashMods import modules
class Youtube(modules.BaseModule):
    def __init__(self, name, description, request):
        super(modules.BaseModule)
        self.name = name
        self.description = description

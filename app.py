import os
class Application:
    def __init__(self):
        try:
            ### Assert Directory Structure
            rootDirectoryStructure = [dI for dI in os.listdir('./') if os.path.isdir(os.path.join('./', dI))]
            rootIntersection = list(set(rootDirectoryStructure).intersection(['datasets','models','plotter']))
            assert (len(rootIntersection) == 3)
            
            ### Assert SubDirectory Structure
            modelsDirectory = [dI for dI in os.listdir('./models') if os.path.isdir(os.path.join('./models', dI))]
            modelIntersection = list(set(modelsDirectory).intersection(['DLModels', 'MLModels']))
            assert (len(modelIntersection) == 2)
        except AssertionError as e:
            e.args += ("Folder Integrity corrupted!", "Please download again!")
            raise
Application()
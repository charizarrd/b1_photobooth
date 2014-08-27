import os

# needed to allow windows to find the dll on the local dir
module_path = os.path.dirname(__file__)
os.environ['PATH'] = module_path + os.pathsep + os.environ['PATH']
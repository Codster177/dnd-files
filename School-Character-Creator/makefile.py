from cx_Freeze import setup, Executable

base = None    

executables = [Executable("generator.py", base=base)]

packages = ["idna", "tkinter", "random"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<School Character Generator>",
    options = options,
    version = "0.0.1",
    description = '<Generates names and cliques.>',
    executables = executables
)
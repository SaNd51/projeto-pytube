from cx_Freeze import setup, Executable
    
base = None    
    
executables = [Executable("tela.py", base=base)]

packages = ["idna"]

options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "teste",
    options = options,
    version = "1",
    description = '<any description>',
    executables = executables
)
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
    name = "Pytube-Sander",
    options = options,
    version = "1",
    description = '<any description>',
    executables = executables
)
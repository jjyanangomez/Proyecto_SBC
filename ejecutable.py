from cx_Freeze import setup, Executable

setup(name = "AppODS",
    version="0.1",
    description="Busqueda de publicaciones ODS",
    executables = [Executable("AppODS.py")])
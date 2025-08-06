# comandos
```
python --version
git --version
pip list
python.exe -m pip install ---upgrade pip
```
## crear entorno virtual
python -m venv env
## crear entorno virtual
env\scripts\activate
si no activa ejecute en el powershell
set-ExecutionPolicy Unrestricted
y escriba s


# Estructura de datos en panda
| Tipo      | contenido                                     |
| --------- | --------------------------------------------- |
| Series    | Array de una dimension                        |
| DataFrame | se correcponde con una tabla de 2 dimensiones |
| panel     | Similar aun diccionario de DatFrame           |
# craeacion  de objetos series
```
#  craeacion de obejetos serie
s=pd.series([2,4,6,8,10])
print (s)
```
# craeacion  de objetos series
```
manejo de git
git init
git add .
git commit "algo"
git commit -m "introduccion a pandas 5%"
si sale error
   git config --global user.email "you@example.com"
   git config --global user.name "Your Name"

crear archivo requirements.txt
pip freeze >requirements.txt
clonar repositorio
como desactivar el entorno virtual
desactivate
//
git clone https://github.com/MariaJose715/IA_G296.git (para clonar la carpeta)
python -m venv env (crear env)
env\scripts\activate(activar env)
powersell, ejecutar como adminitrador: set-ExecutionPolicy Unrestricted (sino funciona hacer esto)
python.exe -m pip install --upgrade pip 
pip install -r requirements.txt 
git config --global user.email "ncuadroso@unal.edu.co"
git config --global user.name "MariaJose715"
cd .\conceptosPrevios\
python .\IntPandas.py (para imprimir)
pip install matplotlib (instalar libreria)
python .\IntNumpy.py
clsy clear (borrar el terminal)

# Remover_Fondo

Remover_Fondo es un script sencillo en Python que elimina el fondo de una imagen utilizando la librería [rembg](https://github.com/danielgatis/rembg) y la biblioteca Pillow (PIL).

## ¿Cómo funciona?

El script toma una imagen llamada `input.png` ubicada en el mismo directorio, le elimina el fondo y guarda el resultado como `output.png`.

## Requisitos

- Python 3.7 o superior
- [rembg](https://pypi.org/project/rembg/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Farias1320/Remover_Fondo.git
cd Remover_Fondo
```

2. Instala las dependencias necesarias:

```bash
pip install rembg Pillow
```

## Uso

1. Coloca la imagen que deseas procesar en el mismo directorio y nómbrala `input.png`.
2. Ejecuta el script:

```bash
python init.py
```

3. El resultado se guardará como `output.png` en el mismo directorio.

## Ejemplo de código

```python
from rembg import remove
from PIL import Image

remover_fondo = remove(Image.open("input.png")) # Remueve el fondo
remover_fondo.save("output.png") # Guarda la imagen sin fondo
```

## Autor

- [Cristopher](https://github.com/Farias1320)

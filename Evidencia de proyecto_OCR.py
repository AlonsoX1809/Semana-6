# Importamos las librerías necesarias para nuestro proyecto
import cv2
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Definimos la función con la que extraeremos el texto 
def extraccion_texto(img):
    # Leemos la imagen
    img = cv2.imread(img)
    # Agregamos una condición en caso de que no se pueda leer la operación
    if img is None:
        print(f"No se pudo cargar la imagen: {img}")
        return ""
    # Usamos tesseract para detectar texto en la imagen
    texto = pytesseract.image_to_string(img, lang='eng')
    # Separa cada línea (operación)
    operaciones = [line.strip() for line in texto.splitlines() if line.strip()] 
    return operaciones

# Definimos la función con la realizaremos la operacion
def evaluar(operaciones):
    # Variable para guardar los resultados
    resultados = []
    # Ciclo for para evaluar cada operacion
    for op in operaciones:
        # Usamos la libreria re para que en la cadena de string extraiga los operadores y numeros
        extraer_elementos_operacion = re.sub(r'[^0-9]\+\-\*/\(\) ]', '', op)
        try:
            # Ejecuta el string como si fuera un código
            resultado = eval(extraer_elementos_operacion)
            # La guardamos en resultados con la operacion correspondiente
            resultados.append((extraer_elementos_operacion, resultado))
        except Exception as e:
            # Un excepcion por si da error y no puede evaluar la operacion
            resultados.append((extraer_elementos_operacion, f"Error: {e}"))
    return resultados

operacion = extraccion_texto("Operacion_Gisel.jpg")
resultado = evaluar(operacion)
print(resultado)
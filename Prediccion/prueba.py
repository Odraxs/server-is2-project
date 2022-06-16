import os
from Prediccion.Prediccion import Prediccion
import base64
import pathlib
from PIL import Image
import cv2
from io import BytesIO
import numpy as np

def readb64(base64_string):
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_BGR2GRAY)


def predecir(modelos, imagenes):
    clases = ["alicate", "destornillador", "llave", "martillo", "regla"]
    # 0=alicate, 1=destornillador, 2=llave, 3=martillo, 4=regla
    ancho = 128
    alto = 128
    dirm="modelos/"
    files = os.listdir(dirm)
    # print(files)
    miModeloCNN = []
    resultados = []
    resultados_por_modelo=[]
    content = []
    idImg = 0
    for imagen in imagenes:
        decoded = readb64(imagen.get("content"))
        cv2.imshow(str(imagen.get("id")), decoded)
        content.append(decoded)

    for modelo in modelos:
        pred = Prediccion(dirm+modelo, ancho, alto)
        miModeloCNN.append(pred)

    for prediccion in miModeloCNN:
        resultados = []
        for img in content:
            clase = prediccion.predecir(img)
            resultados.append({"class": clases[clase], "id": imagenes[idImg].get("id")})
            idImg += 1
        resultados_por_modelo.append({"morel_id":prediccion.ruta,"results":resultados})
        idImg = 0

    return resultados_por_modelo

    # files = os.listdir(dirc + "nuevas/")
    # for file in files:
    #     imagen = cv2.imread(dirc + "nuevas/" + file)
    #     imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    #     # imagen=cv2.imread(dirc+direccion)
    #     inicio = time.time()
    #     claseResultado = miModeloCNN.predecir(imagenGris)
    #     fin = time.time()
    #     print(fin-inicio,"tiempo respuesta")
    #     #print("La imagen cargada es ", clases[claseResultado - 1])
    #     msg1="prediccion "+str(clases[claseResultado - 1])

# predecir(["modelo_2.h5"])

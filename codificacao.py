import os
import shutil

origem = "C:/Users/Hericc/Desktop/PythonTarefas/102"
destino = "C:/Users/Hericc/Desktop/PythonTarefas/102/jpg"

listaArquivo = os.listdir(origem)
#print(listaArquivo)

for H in listaArquivo:

    nome, estencao = os.path.splitext(H)
    #print(nome)
    #print(estencao)

    if estencao =="":
        continue
    if estencao in [".jpg"]:
        caminho1 = origem + "/" + H
        caminho2 = destino + "/" + "terraMon"
        caminho3 = destino + "/" + "terraMon" + H

        if os.path.exists(caminho2):
            print("movendo "+ H)
            shutil.move(caminho1, caminho3)
        else:
            os.makedirs(caminho2)    
            print("movendo "+ H)
            shutil.move(caminho1, caminho3)
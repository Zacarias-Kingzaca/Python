import shutil

def center(texto):
   largura =  shutil.get_terminal_size().columns
   print(texto.center(largura))
from zipfile import ZipFile
import os

arquivo_zip = "dados_para_download.zip"
diretorio_extrair = "arquivos_extraidos"
os.mkdir(diretorio_extrair)

with ZipFile(arquivo_zip, "r") as arq_zip:
    arq_zip.extractall(diretorio_extrair)
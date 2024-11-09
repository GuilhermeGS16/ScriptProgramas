import sys
import os
import shutil
import subprocess

# Definição de funções
def main():
    ProgramasDaRede = r'C:\Users\guilh\Desktop\All\Pasta-de-programas'
    CaminhoAreaDeTrabalho = os.path.join(os.path.expanduser("~"), "Desktop")

    # Copiar a pasta inteira usando copytree
    CaminhoPastaCopiada = os.path.join(CaminhoAreaDeTrabalho, os.path.basename(ProgramasDaRede))
    if not os.path.exists(CaminhoPastaCopiada):  # Verifica se a pasta já não foi copiada
        shutil.copytree(ProgramasDaRede, CaminhoPastaCopiada)
    
    # Lista de caminhos para os executáveis a serem rodados
    programas = [
        os.path.join(CaminhoPastaCopiada, "AdobeReader.exe"),
        os.path.join(CaminhoPastaCopiada, "LightShot.exe"),
        os.path.join(CaminhoPastaCopiada, "GoogleChrome.exe"),
        os.path.join(CaminhoPastaCopiada, "WinRar.exe"),
        os.path.join(CaminhoPastaCopiada, "Bizagi.exe"),
        os.path.join(CaminhoPastaCopiada, "PowerBI.exe"),
        os.path.join(CaminhoPastaCopiada, "SAP.exe")
    ]
    
    # Loop para executar cada programa na lista
    for programa in programas:
        try:
            subprocess.run([programa], check=True)
            print(f"{os.path.basename(programa)} executado com sucesso!")
        except subprocess.CalledProcessError:
            print(f"Erro ao executar o arquivo: {os.path.basename(programa)}")
        except FileNotFoundError:
            print(f"Arquivo {os.path.basename(programa)} não encontrado.")

main()
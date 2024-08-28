import os
import socket
from flask import Flask
from main import app  # Importa o aplicativo Flask do seu arquivo main.py

def get_local_ip():
    # Tenta se conectar a um servidor DNS público para obter o IP local
    # O IP real da máquina será obtido, mesmo que sem conexão real
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Não precisa de conexão real, apenas usa um IP externo
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  # Fallback para localhost se houver algum problema
    finally:
        s.close()
    return ip

def main():
    # Obtém o IP local da máquina
    local_ip = get_local_ip()
    
    try:
        # Inicia o servidor Flask com o IP dinâmico obtido
        app.run(host=local_ip, port=8001, debug=True)
    except KeyboardInterrupt:
        print("\nServidor interrompido. Fechando...")

if __name__ == '__main__':
    main()

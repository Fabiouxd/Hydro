import os                                                       #Pesquisei essa biblioteca ppara localizar os arquivos (.json por exemplo) independentemente de onde o script é executado
import json
import time                                                     #Pra utilizar funções com o modo tempo importei essa biblioteca
from sensores import ler_umidade, status_irrigacao
from irrigacao import controlar_irrigacao
from database import salvar_dados

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')    # Caminho para config.json

def main():
    try:
        with open(CONFIG_PATH) as f:
            config = json.load(f)
        
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Monitorar áreas")
            print("2. Controlar irrigação")
            print("3. Sair")
            
            opcao = input("Escolha: ").strip()                          #.strip() remove espacos no inicio e fim de uma str, caso tenha digitado sem querer 
            
            if opcao == "1":
                for area in config["areas"]:
                    umidade = ler_umidade(area)
                    status = status_irrigacao(umidade, config["limite_umidade"])
                    dados = {
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), #O .time Pfaz com que o padrão seja o ANO-MÊS-DIA HORA:MINUTO:SEGUNDO
                        "area": area,
                        "umidade": umidade,
                        "status": status
                    }
                    salvar_dados(dados, 'monitoramento')
                    print(f"[Área {area}] Umidade: {umidade}% → {status}")
            
            elif opcao == "2":
                irrigacao = controlar_irrigacao()
                if irrigacao:
                    salvar_dados(irrigacao, 'irrigacao')
                    print(f"Irrigação registrada: Área {irrigacao['area']} com {irrigacao['litros']}L")
            
            elif opcao == "3":
                print("Saindo do sistema...")
                break
            
            else:
                print("Opção inválida! Tente novamente.")
            
            time.sleep(0.4)                                     # ainda aproveitando a biblioteca  para simular um intervalo entre verificações (como um sistema real faria)
    
    except FileNotFoundError:                                   # parte para capturar erros no .JSON, seja caminho errado, ou corrompido
        print(f"ERRO: Arquivo config.json não encontrado em {CONFIG_PATH}")
    except json.JSONDecodeError:
        print("ERRO: config.json mal formatado!")
    except Exception as e:
        print(f"ERRO inesperado: {str(e)}")

if __name__ == "__main__":
    main()
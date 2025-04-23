import random

def ler_umidade(area: str) -> float: #Aqui Gera um valor aleatório de umidade entre 15.0% e 45.0% para uma área, seria pra simular sensores"
    return round(random.uniform(15.0, 45.0), 1)

def status_irrigacao(umidade: float, limite: float) -> str: #Essa funcao vai retornar 'IRRIGAR' se umidade abaixo do limite, caso contrário 'OK'
    return "IRRIGAR" if umidade < limite else "OK"
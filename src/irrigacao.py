from datetime import datetime

def controlar_irrigacao():
    """Controla manualmente a irrigação"""
    print("\n=== CONTROLE DE IRRIGAÇÃO ===")
    
    while True:
        area = input("Área (A/B/C/D): ").upper().strip()
        if area in ["A", "B", "C", "D"]:
            break
        print("Área inválida! Digite A, B, C ou D")
    
    while True:
        try:
            litros = float(input("Litros para irrigar: "))
            if litros > 0:
                break
            print("Digite um valor positivo!")
        except ValueError:
            print("Valor inválido! Use números (ex: 15.5)")
    
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "area": area,
        "litros": litros
    }
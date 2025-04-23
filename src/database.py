import os
import csv
import oracledb

def salvar_dados(dados: dict, tipo: str):                                 # Salva dados em CSV e Oracle
    try:
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')  # Salva em CSV (backup), extremamente complicado essa parte, tive que pedir ajuda universitaria rs
        os.makedirs(data_dir, exist_ok=True)
        
        csv_path = os.path.join(data_dir, f"{tipo}.csv")
        with open(csv_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=dados.keys())
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(dados)
        
        with oracledb.connect(                                             # Salva no Oracle (Tem que colocar minhas credenciais, ou de quem usar)
            user="RM565310",
            password="260194",
            dsn="oracle.fiap.com.br:1521/ORCL"
        ) as conn:
            with conn.cursor() as cursor:
                if tipo == 'monitoramento':
                    cursor.execute("""
                        INSERT INTO monitoramento (data, area, umidade, status)
                        VALUES (TO_TIMESTAMP(:timestamp, 'YYYY-MM-DD HH24:MI:SS'), 
                                :area, :umidade, :status)
                    """, dados)
                else:
                    cursor.execute("""
                        INSERT INTO irrigacao (data, area, litros)
                        VALUES (TO_TIMESTAMP(:timestamp, 'YYYY-MM-DD HH24:MI:SS'), 
                                :area, :litros)
                    """, dados)
                conn.commit()
                
    except Exception as e:
        print(f"ERRO ao salvar dados: {str(e)}")
import os
import csv
import oracledb

def salvar_dados(dados: dict, tipo: str):                                 # Salva dados em CSV e Oracle
    try:
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')  # Salva em CSV (backup), extremamente complicado essa parte, tive que pedir ajuda universitaria rs
        os.makedirs(data_dir, exist_ok=True)
        
        csv_path = os.path.join(data_dir, f"{tipo}.csv")
        with open(csv_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=dados.keys())
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(dados)
        
        with oracledb.connect(                                             # Salva no Oracle (Tem que colocar minhas credenciais, ou de quem usar)
            user="seu_usuario",
            password="sua_senha",
            dsn="localhost:1521/XE"
        ) as conn:
            with conn.cursor() as cursor:
                if tipo == 'monitoramento':
                    cursor.execute("""
                        INSERT INTO monitoramento (data, area, umidade, status)
                        VALUES (TO_TIMESTAMP(:timestamp, 'YYYY-MM-DD HH24:MI:SS'), 
                                :area, :umidade, :status)
                    """, dados)
                else:
                    cursor.execute("""
                        INSERT INTO irrigacao (data, area, litros)
                        VALUES (TO_TIMESTAMP(:timestamp, 'YYYY-MM-DD HH24:MI:SS'), 
                                :area, :litros)
                    """, dados)
                conn.commit()
                
    except Exception as e:
        print(f"ERRO ao salvar dados: {str(e)}")
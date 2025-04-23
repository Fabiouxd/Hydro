import oracledb

try:
    # Teste de conexão com suas credenciais
    with oracledb.connect(
        user="RM565310",
        password="260194",
        dsn="oracle.fiap.com.br:1521/ORCL" 
    ) as conn:
        print("Conexão bem-sucedida!")
        
        # Verifica se as tabelas existem
        with conn.cursor() as cursor:
            cursor.execute("SELECT table_name FROM user_tables WHERE table_name IN ('MONITORAMENTO', 'IRRIGACAO')")
            tables = [row[0] for row in cursor]
            print(f"Tabelas disponíveis: {tables}")
            
            # Testa inserção na tabela monitoramento
            try:
                cursor.execute("""
                    INSERT INTO monitoramento (data, area, umidade, status)
                    VALUES (SYSTIMESTAMP, 'A', 20.5, 'IRRIGAR')
                """)
                conn.commit()
                print("Teste de inserção bem-sucedido!")
            except Exception as e:
                print(f"Erro ao inserir: {str(e)}")
                
except Exception as e:
    print(f"Erro ao conectar: {str(e)}")
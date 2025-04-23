Sistema de Monitoramento e Controle de Irrigação
Um sistema simples para monitorar níveis de umidade e controlar a irrigação em diferentes áreas de plantio.
O que esse sistema faz?
Esse projeto foi criado para facilitar o monitoramento da umidade do solo em áreas de plantio e controlar manualmente a irrigação quando necessário. O sistema salva todos os dados tanto em arquivos CSV locais quanto em um banco de dados Oracle.
Requisitos

Python 3.6+
Oracle Database 
Biblioteca python-oracledb
Bibliotecas padrão do Python (os, csv, json, time, random, datetime)


Instale as dependências:

pip install python-oracledb

Configure suas credenciais do banco de dados no arquivo database.py
Crie as tabelas necessárias no Oracle (veja o script SQL abaixo)

Uso
Para iniciar o sistema:
python "$env:USERPROFILE\Desktop\HydroAnalise\src\main.py" 
Para testar a conexaão: 
python "$env:USERPROFILE\Desktop\HydroAnalise\src\teste_conexao.py"
O sistema oferece um menu com opções para:

Monitorar áreas (verifica o nível de umidade de cada área)
Controlar irrigação (permite definir uma área e quantidade de litros para irrigar)
Sair

Estrutura do projeto

config.json - Configurações básicas do sistema
main.py - Ponto de entrada do programa com menu principal
sensores.py - Simulação de leitura de sensores de umidade
irrigacao.py - Funções para controle de irrigação
database.py - Operações de banco de dados (CSV e Oracle)

Sobre o armazenamento de dados
Os dados são armazenados em duas formas:

Arquivos CSV 
Banco de dados Oracle 

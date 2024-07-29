import sqlite3
import pandas as pd

# Conecte-se ao banco de dados SQLite
conn = sqlite3.connect('customermanager.db')

# Substitua 'nome_da_tabela' pelo nome real da tabela
query = "SELECT * FROM cliente"

# Use pandas para executar a consulta e carregar os dados em um DataFrame
df = pd.read_sql_query(query, conn)

# Salve o DataFrame em um arquivo Excel
df.to_excel('tabela.xlsx', index=False)

# Feche a conexão com o banco de dados
conn.close()

print("Dados exportados com sucesso para tabela.xlsx")

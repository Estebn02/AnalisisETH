import csv
from web3 import Web3

# Conectarse a la red Ethereum
w3 = Web3(Web3.HTTPProvider(''))

# Obtener el número del último bloque
ultimo_bloque = w3.eth.block_number

# Crear un archivo CSV para almacenar los datos
nombre_archivo = 'transacciones.csv'
encabezados = ['Bloque', 'Hash de transacción', 'Valor', 'Dirección del remitente']
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(encabezados)
    
    # Obtener los datos de las transacciones de los últimos 5 bloques
    for numero_bloque in range(ultimo_bloque, ultimo_bloque - 5, -1):
        bloque = w3.eth.get_block(numero_bloque)
        transacciones = bloque.transactions

        for hash_tx in transacciones:
            tx = w3.eth.get_transaction(hash_tx.hex())
            fila = [numero_bloque, hash_tx.hex(), tx.value, tx.get("from")]
            writer.writerow(fila)



#https://mainnet.infura.io/v3/93345e7d058042008cc597f65d36e7cc
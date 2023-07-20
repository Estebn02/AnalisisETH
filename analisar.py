import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('transacciones.csv', encoding='latin1')
print("se cargo el df")

# Mostrar las primeras filas del DataFrame
print(df.head())
print("******************************************")

# Verificar los tipos de datos de cada columna
print(df.dtypes)
print("******************************************")

# Convertir la columna 'Valor' a tipo numérico
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce').astype(float)
print("******************************************")

# Eliminar las filas con valores faltantes
df = df.dropna()
print("se eliminaron todos los valores faltantes")

# Filtrar las transacciones con un valor mayor a cierto umbral
#umbral = 1000
#transacciones_mayores = df[df['Valor'] > umbral]

# Filtrar las transacciones de una dirección específica
direccion = '0x1234567890abcdef'
transacciones_direccion = df[df['Dirección del remitente'] == direccion]

# Calcular estadísticas descriptivas de la columna 'Valor'
estadisticas_valor = df['Valor'].describe()

# Guardar el DataFrame preprocesado en un nuevo archivo CSV
nombre_archivo_preprocesado = 'transacciones_preprocesadas.csv'
df.to_csv(nombre_archivo_preprocesado, index=False)

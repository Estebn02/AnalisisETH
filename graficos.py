import matplotlib.pyplot as plt
import pandas as pd

df2 = pd.read_csv('transacciones_preprocesadas.csv', encoding='latin1')
print(df2.head())

# Contar la cantidad de transacciones por bloque
conteo_transacciones = df2['Bloque'].value_counts()

# Crear el gráfico de torta
plt.figure(figsize=(8, 6))
plt.pie(conteo_transacciones, labels=conteo_transacciones.index, autopct='%1.1f%%')
plt.title('Cantidad de transacciones por bloque')
plt.show()



# Agrupar y sumar los valores de transacción por bloque
valor_transacciones = df2.groupby('Bloque')['Valor'].sum()

# Crear el gráfico de torta
plt.figure(figsize=(8, 6))
plt.pie(valor_transacciones, labels=valor_transacciones.index, autopct='%1.1f%%')
plt.title('Valor de transacciones por bloque')
plt.show()

# Agrupar los datos por bloque y contar el número de transacciones
transacciones_por_bloque = df2.groupby('Bloque').size()

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(transacciones_por_bloque.index, transacciones_por_bloque.values)
plt.xlabel('Bloque')
plt.ylabel('Número de transacciones')
plt.title('Evolución del número de transacciones por bloque')
plt.show()



# Verificar el nombre de la columna en el DataFrame
print(df2.columns)

# Contar las transacciones por dirección del remitente
conteo_transacciones = df2['DirecciÃ³n del remitente'].value_counts()

# Imprimir el resultado
#print(conteo_transacciones)

# Filtrar remitentes con más de 2 transacciones
remitentes_frecuentes = conteo_transacciones[conteo_transacciones > 2]

# Configurar el estilo del gráfico
plt.style.use('seaborn')

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
remitentes_frecuentes.plot(kind='bar', color='steelblue')

# Configurar los ejes y el título
ax.set_xlabel('Dirección del remitente')
ax.set_ylabel('Cantidad de transacciones')
ax.set_title('Cantidad de transacciones por remitente (más de 2 transacciones)')

# Rotar las etiquetas del eje x para una mejor legibilidad
plt.xticks(rotation=45, ha='right')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
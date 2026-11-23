import pandas as pd
import matplotlib.pyplot as plt
# Emily Barraza NC 0025
# 1. Leer el archivo CSV
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV comida India 0025 ---")
print(df_food_india)
print("\n--- Mostrar Nombre comida + ingredientes 0025 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- Tiempo de cocinado mostrar 10 requisitos de con head 0025 ---")
Nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(Nombre_y_hora)
print("\n--- Grafica comida (X) texto de cocina comida (Y) india 0025 ---")
print("\n--- Grafica comida (X) texto X a 10 grados 0025 ---")
Nombre_y_hora.plot.bar(x='name',y='cook_time', rot=30)
plt.title('comida tipica de india Emily Barraza 0025')
plt.xlabel('Nombre de platillo')
plt.ylabel('Tiempo de cocina')
plt.show()
print("\n--- Grafica de barras de varias columnas Emily 0025 ---")
Nombre_y_hora = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
Nombre_y_hora.plot.bar(x='name', rot=30)
plt.title('Grafica de 2 columnas Emily Barraza 0025')
plt.xlabel('Nombre de platillo')
plt.ylabel('Tiempo de cocina prep y comida')
plt.show()
print("\n--- Grafica de barras apiladas una tras otra verticalmente Emily Barraza 0025 ---")
Nombre_y_hora.plot.bar(x='name', stacked=True)
plt.title('Grafica apiladas una tras otra Emily Barraza 0025')
plt.xlabel('Nombre de platillo')
plt.ylabel('Tiempo de cocina prep y comida')
plt.show()



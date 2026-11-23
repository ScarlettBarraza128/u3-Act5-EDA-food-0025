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

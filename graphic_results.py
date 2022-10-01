import matplotlib.pyplot as plt
import numpy




"""
Configurar parametros de visualización y desplegar grífica basada en los datos recolectados, usando "matplotlib"
"""
# Configurar color de background y tamaños de fuentes
plt.rcParams.update({'axes.facecolor': "#edf1f7", 'font.size': 16})
# Configurar tamaño de figura a desplegar
plt.figure(5, figsize=(20, 15))
# Insertar cada lista correspondiente a la clase de usuario.
for index, user in enumerate(active_users_array):
    plt.plot(global_date_string_list, user, label="Active: User_" + str(active_users["user_id"].loc[index]), linestyle="dotted")
for index, user in enumerate(inactive_users_array):
    plt.plot(global_date_string_list, user, label="Inactive: User_" + str(inactive_users["user_id"].loc[index]), linestyle="-")
# Configurar nombre de labels en el eje X, amén del resto de los labels generales
plt.xticks(global_date_string_list, [(index + 1) for index in range(len(global_date_string_list))] )
plt.legend()
plt.grid(axis='y')
plt.title("Actividades de usuarios ACTIVOS y NO-ACTIVOS durante el mes de Marzo")
plt.xlabel("Días del mes")
plt.ylabel("Cuentas de actividades")
plt.show()
plt.clf()
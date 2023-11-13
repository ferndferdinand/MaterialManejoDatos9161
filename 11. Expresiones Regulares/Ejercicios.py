# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:52:01 2023

@author: Fernando
"""

# Soluciones ejercicios

import re
# %%
# Correo
def validar_correo(correo):
    patron = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None


correo_ejemplo = "usuario@dominio.com"
if validar_correo(correo_ejemplo):
    print(f"{correo_ejemplo} es una dirección de correo electrónico válida.")
else:
    print(f"{correo_ejemplo} no es una dirección de correo electrónico válida.")


# %%
# HTML
def extraer_html(texto):
    patron = "<[^>]+>"
    coincidencias = re.findall(patron, texto)

    return coincidencias

texto_html_ejemplo = "<p>Este es un ejemplo de <a href='http://ejemplo.com'>etiquetas</a> HTML.</p>"
etiquetas_encontradas = extraer_html(texto_html_ejemplo)

for etiqueta in etiquetas_encontradas:
    print("Etiqueta HTML encontrada:", etiqueta)


# %%
# Contraseñas
def validar_password_seguro(password):
    patron = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"

    return re.match(patron, password) is not None


# Ejemplo de uso de la función
contraseña_ejemplo = "oZfdg6.lB$2"
if validar_password_seguro(contraseña_ejemplo):
    print(f"{contraseña_ejemplo} es una contraseña segura.")
else:
    print(f"{contraseña_ejemplo} no cumple con los requisitos de contraseña segura.")

# %%
# Enlaces web
def extraer_enlaces_web(texto):
    patron = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    coincidencias = re.findall(patron, texto)

    return coincidencias

texto_ejemplo = "Aquí tienes un enlace a Classroom: https://classroom.google.com/u/0/c/NjE2NDA4MTUxODE3?hl=en y otro a GitHub https://github.com/ferdferdinand/MaterialManejoDatos9161"
enlaces_encontrados = extraer_enlaces_web(texto_ejemplo)

for enlace in enlaces_encontrados:
    print("Enlace web encontrado:", enlace)

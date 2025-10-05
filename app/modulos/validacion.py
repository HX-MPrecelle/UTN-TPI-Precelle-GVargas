"""
Módulo de Validación
===================
Este módulo contiene funciones para validar entradas del usuario,
filtrar datos y manejar errores de forma robusta.
"""

import re
from typing import Optional


def validar_entrada_numero(entrada: str, min_valor: Optional[int] = None, 
                          max_valor: Optional[int] = None) -> Optional[int]:
    """
    Valida que una entrada sea un número entero válido.
    
    Args:
        entrada (str): Entrada del usuario
        min_valor (int, optional): Valor mínimo permitido
        max_valor (int, optional): Valor máximo permitido
        
    Returns:
        Optional[int]: Número validado o None si es inválido
    """
    try:
        # Limpiar entrada y convertir a entero
        entrada_limpia = entrada.strip().replace(',', '').replace('.', '')
        numero = int(entrada_limpia)
        
        # Verificar rangos si se especifican
        if min_valor is not None and numero < min_valor:
            print(f"❌ El número debe ser mayor o igual a {min_valor}")
            return None
        
        if max_valor is not None and numero > max_valor:
            print(f"❌ El número debe ser menor o igual a {max_valor}")
            return None
        
        return numero
    
    except ValueError:
        print("❌ Por favor, ingrese un número entero válido")
        return None

def normalizar_texto_busqueda(texto: str) -> str:
    """
    Normaliza texto para búsquedas (minúsculas, sin acentos).
    
    Args:
        texto (str): Texto a normalizar
        
    Returns:
        str: Texto normalizado
    """
    # Convertir a minúsculas
    texto = texto.lower().strip()
    
    # Reemplazar caracteres especiales
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ñ': 'n', 'ü': 'u', 'ç': 'c'
    }
    
    for original, reemplazo in reemplazos.items():
        texto = texto.replace(original, reemplazo)
    
    return texto

def formatear_numero(numero: int) -> str:
    """
    Formatea un número para mostrarlo de manera legible.
    
    Args:
        numero (int): Número a formatear
        
    Returns:
        str: Número formateado con separadores de miles
    """
    return f"{numero:,}".replace(",", ".")

def pausar_ejecucion():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\n⏸️  Presione Enter para continuar...")

def mostrar_separador(caracter: str = "=", longitud: int = 50):
    """
    Muestra un separador visual.
    
    Args:
        caracter (str): Caracter a usar para el separador
        longitud (int): Longitud del separador
    """
    print(caracter * longitud)


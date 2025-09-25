"""
Módulo de Validación
===================
Este módulo contiene funciones para validar entradas del usuario,
filtrar datos y manejar errores de forma robusta.
"""

import re
from typing import List, Dict, Any, Optional, Tuple


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


def validar_entrada_texto(entrada: str, longitud_minima: int = 1, 
                         permitir_vacio: bool = False) -> Optional[str]:
    """
    Valida que una entrada sea texto válido.
    
    Args:
        entrada (str): Entrada del usuario
        longitud_minima (int): Longitud mínima del texto
        permitir_vacio (bool): Si permite texto vacío
        
    Returns:
        Optional[str]: Texto validado o None si es inválido
    """
    entrada_limpia = entrada.strip()
    
    if not permitir_vacio and not entrada_limpia:
        print("❌ El campo no puede estar vacío")
        return None
    
    if len(entrada_limpia) < longitud_minima:
        print(f"❌ El texto debe tener al menos {longitud_minima} caracteres")
        return None
    
    return entrada_limpia


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


def validar_continente(continente: str, continentes_validos: List[str]) -> Optional[str]:
    """
    Valida que un continente sea válido.
    
    Args:
        continente (str): Nombre del continente
        continentes_validos (List[str]): Lista de continentes válidos
        
    Returns:
        Optional[str]: Continente validado o None si es inválido
    """
    continente_limpio = validar_entrada_texto(continente)
    if not continente_limpio:
        return None
    
    # Buscar coincidencia exacta o parcial
    continente_normalizado = normalizar_texto_busqueda(continente_limpio)
    
    for continente_valido in continentes_validos:
        if normalizar_texto_busqueda(continente_valido) == continente_normalizado:
            return continente_valido
    
    # Buscar coincidencia parcial
    coincidencias = []
    for continente_valido in continentes_validos:
        if continente_normalizado in normalizar_texto_busqueda(continente_valido):
            coincidencias.append(continente_valido)
    
    if len(coincidencias) == 1:
        return coincidencias[0]
    elif len(coincidencias) > 1:
        print("❌ Múltiples continentes coinciden. Opciones:")
        for i, opcion in enumerate(coincidencias, 1):
            print(f"  {i}. {opcion}")
        return None
    else:
        print(f"❌ Continente no encontrado. Continentes disponibles: {', '.join(continentes_validos)}")
        return None


def validar_rango_numerico(valor_min: str, valor_max: str, 
                          min_permitido: Optional[int] = None,
                          max_permitido: Optional[int] = None) -> Optional[Tuple[int, int]]:
    """
    Valida un rango numérico.
    
    Args:
        valor_min (str): Valor mínimo del rango
        valor_max (str): Valor máximo del rango
        min_permitido (int, optional): Valor mínimo permitido en el sistema
        max_permitido (int, optional): Valor máximo permitido en el sistema
        
    Returns:
        Optional[Tuple[int, int]]: Tupla (min, max) validada o None si es inválido
    """
    min_valor = validar_entrada_numero(valor_min, min_permitido, max_permitido)
    if min_valor is None:
        return None
    
    max_valor = validar_entrada_numero(valor_max, min_permitido, max_permitido)
    if max_valor is None:
        return None
    
    if min_valor > max_valor:
        print("❌ El valor mínimo no puede ser mayor que el valor máximo")
        return None
    
    return (min_valor, max_valor)


def validar_opcion_menu(entrada: str, opciones_validas: List[str]) -> Optional[str]:
    """
    Valida una opción del menú.
    
    Args:
        entrada (str): Entrada del usuario
        opciones_validas (List[str]): Lista de opciones válidas
        
    Returns:
        Optional[str]: Opción validada o None si es inválida
    """
    entrada_limpia = entrada.strip()
    
    if entrada_limpia in opciones_validas:
        return entrada_limpia
    
    print(f"❌ Opción inválida. Opciones disponibles: {', '.join(opciones_validas)}")
    return None


def validar_cantidad_resultados(entrada: str, max_posible: int) -> Optional[int]:
    """
    Valida la cantidad de resultados a mostrar.
    
    Args:
        entrada (str): Entrada del usuario
        max_posible (int): Cantidad máxima posible
        
    Returns:
        Optional[int]: Cantidad validada o None si es inválida
    """
    cantidad = validar_entrada_numero(entrada, 1, max_posible)
    if cantidad is None:
        return None
    
    return cantidad


def formatear_numero(numero: int) -> str:
    """
    Formatea un número para mostrarlo de manera legible.
    
    Args:
        numero (int): Número a formatear
        
    Returns:
        str: Número formateado con separadores de miles
    """
    return f"{numero:,}".replace(",", ".")


def confirmar_accion(mensaje: str) -> bool:
    """
    Solicita confirmación al usuario para una acción.
    
    Args:
        mensaje (str): Mensaje a mostrar
        
    Returns:
        bool: True si confirma, False si cancela
    """
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("❌ Por favor, responda 's' para sí o 'n' para no")


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


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


"""
Módulo de Consultas y Búsquedas
==============================
Este módulo contiene funciones para buscar y filtrar países
según diferentes criterios.
"""

from typing import List, Dict, Any, Optional
from .validacion import normalizar_texto_busqueda


def buscar_pais_por_nombre(paises: List[Dict[str, Any]], nombre: str, 
                          busqueda_exacta: bool = False) -> List[Dict[str, Any]]:
    """
    Busca países por nombre (coincidencia exacta o parcial).
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        nombre (str): Nombre a buscar
        busqueda_exacta (bool): Si debe ser búsqueda exacta
        
    Returns:
        List[Dict[str, Any]]: Lista de países que coinciden
    """
    if not nombre or not paises:
        return []
    
    nombre_busqueda = normalizar_texto_busqueda(nombre)
    resultados = []
    
    for pais in paises:
        nombre_pais = normalizar_texto_busqueda(pais['nombre'])
        
        if busqueda_exacta:
            if nombre_pais == nombre_busqueda:
                resultados.append(pais)
        else:
            if nombre_busqueda in nombre_pais:
                resultados.append(pais)
    
    return resultados


def filtrar_por_continente(paises: List[Dict[str, Any]], continente: str) -> List[Dict[str, Any]]:
    """
    Filtra países por continente.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        continente (str): Nombre del continente
        
    Returns:
        List[Dict[str, Any]]: Lista de países del continente
    """
    if not continente or not paises:
        return []
    
    continente_busqueda = normalizar_texto_busqueda(continente)
    resultados = []
    
    for pais in paises:
        continente_pais = normalizar_texto_busqueda(pais['continente'])
        if continente_pais == continente_busqueda:
            resultados.append(pais)
    
    return resultados


def filtrar_por_rango_poblacion(paises: List[Dict[str, Any]], 
                               poblacion_min: int, poblacion_max: int) -> List[Dict[str, Any]]:
    """
    Filtra países por rango de población.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        poblacion_min (int): Población mínima
        poblacion_max (int): Población máxima
        
    Returns:
        List[Dict[str, Any]]: Lista de países en el rango
    """
    if not paises:
        return []
    
    resultados = []
    for pais in paises:
        poblacion = pais['poblacion']
        if poblacion_min <= poblacion <= poblacion_max:
            resultados.append(pais)
    
    return resultados


def filtrar_por_rango_superficie(paises: List[Dict[str, Any]], 
                                superficie_min: int, superficie_max: int) -> List[Dict[str, Any]]:
    """
    Filtra países por rango de superficie.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        superficie_min (int): Superficie mínima
        superficie_max (int): Superficie máxima
        
    Returns:
        List[Dict[str, Any]]: Lista de países en el rango
    """
    if not paises:
        return []
    
    resultados = []
    for pais in paises:
        superficie = pais['superficie']
        if superficie_min <= superficie <= superficie_max:
            resultados.append(pais)
    
    return resultados


def buscar_paises_multiples_criterios(paises: List[Dict[str, Any]], 
                                     continente: Optional[str] = None,
                                     poblacion_min: Optional[int] = None,
                                     poblacion_max: Optional[int] = None,
                                     superficie_min: Optional[int] = None,
                                     superficie_max: Optional[int] = None,
                                     nombre_contiene: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Busca países aplicando múltiples criterios de filtrado.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        continente (str, optional): Continente a filtrar
        poblacion_min (int, optional): Población mínima
        poblacion_max (int, optional): Población máxima
        superficie_min (int, optional): Superficie mínima
        superficie_max (int, optional): Superficie máxima
        nombre_contiene (str, optional): Texto que debe contener el nombre
        
    Returns:
        List[Dict[str, Any]]: Lista de países que cumplen todos los criterios
    """
    resultados = paises.copy()
    
    # Filtrar por continente
    if continente:
        resultados = filtrar_por_continente(resultados, continente)
    
    # Filtrar por rango de población
    if poblacion_min is not None or poblacion_max is not None:
        min_pob = poblacion_min if poblacion_min is not None else 0
        max_pob = poblacion_max if poblacion_max is not None else float('inf')
        resultados = [p for p in resultados if min_pob <= p['poblacion'] <= max_pob]
    
    # Filtrar por rango de superficie
    if superficie_min is not None or superficie_max is not None:
        min_sup = superficie_min if superficie_min is not None else 0
        max_sup = superficie_max if superficie_max is not None else float('inf')
        resultados = [p for p in resultados if min_sup <= p['superficie'] <= max_sup]
    
    # Filtrar por nombre que contenga texto
    if nombre_contiene:
        resultados = buscar_pais_por_nombre(resultados, nombre_contiene, busqueda_exacta=False)
    
    return resultados



def obtener_continentes_disponibles(paises: List[Dict[str, Any]]) -> List[str]:
    """
    Obtiene la lista de continentes disponibles en los datos.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        List[str]: Lista de continentes únicos, ordenados alfabéticamente
    """
    continentes = set(pais['continente'] for pais in paises)
    return sorted(list(continentes))


def buscar_paises_top(paises: List[Dict[str, Any]], criterio: str, cantidad: int) -> List[Dict[str, Any]]:
    """
    Obtiene los países top según un criterio.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        criterio (str): Criterio de ordenamiento ('poblacion', 'superficie')
        cantidad (int): Cantidad de países a retornar
        
    Returns:
        List[Dict[str, Any]]: Lista de países top
    """
    if not paises or cantidad <= 0:
        return []
    
    # Ordenar por criterio (descendente)
    paises_ordenados = sorted(paises, key=lambda x: x[criterio], reverse=True)
    
    return paises_ordenados[:cantidad]


def buscar_paises_bottom(paises: List[Dict[str, Any]], criterio: str, cantidad: int) -> List[Dict[str, Any]]:
    """
    Obtiene los países bottom según un criterio.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        criterio (str): Criterio de ordenamiento ('poblacion', 'superficie')
        cantidad (int): Cantidad de países a retornar
        
    Returns:
        List[Dict[str, Any]]: Lista de países bottom
    """
    if not paises or cantidad <= 0:
        return []
    
    # Ordenar por criterio (ascendente)
    paises_ordenados = sorted(paises, key=lambda x: x[criterio])
    
    return paises_ordenados[:cantidad]



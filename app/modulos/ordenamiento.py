"""
Módulo de Ordenamiento
=====================
Este módulo contiene funciones para ordenar países según diferentes criterios
usando algoritmos de ordenamiento implementados desde cero.
"""

from typing import List, Dict, Any, Optional


def ordenar_por_nombre(paises: List[Dict[str, Any]], descendente: bool = False) -> List[Dict[str, Any]]:
    """
    Ordena países por nombre usando ordenamiento por selección.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        descendente (bool): Si debe ordenar de forma descendente
        
    Returns:
        List[Dict[str, Any]]: Lista de países ordenada
    """
    if not paises:
        return []
    
    # Crear copia para no modificar la lista original
    paises_ordenados = paises.copy()
    
    # Ordenamiento por selección
    n = len(paises_ordenados)
    for i in range(n):
        indice_extremo = i
        for j in range(i + 1, n):
            nombre_actual = paises_ordenados[j]['nombre'].lower()
            nombre_extremo = paises_ordenados[indice_extremo]['nombre'].lower()
            
            if descendente:
                if nombre_actual > nombre_extremo:
                    indice_extremo = j
            else:
                if nombre_actual < nombre_extremo:
                    indice_extremo = j
        
        # Intercambiar elementos
        paises_ordenados[i], paises_ordenados[indice_extremo] = \
            paises_ordenados[indice_extremo], paises_ordenados[i]
    
    return paises_ordenados


def ordenar_por_poblacion(paises: List[Dict[str, Any]], descendente: bool = False) -> List[Dict[str, Any]]:
    """
    Ordena países por población usando ordenamiento burbuja optimizado.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        descendente (bool): Si debe ordenar de forma descendente
        
    Returns:
        List[Dict[str, Any]]: Lista de países ordenada
    """
    if not paises:
        return []
    
    paises_ordenados = paises.copy()
    n = len(paises_ordenados)
    
    # Ordenamiento burbuja optimizado
    for i in range(n):
        intercambio_realizado = False
        for j in range(0, n - i - 1):
            poblacion_actual = paises_ordenados[j]['poblacion']
            poblacion_siguiente = paises_ordenados[j + 1]['poblacion']
            
            debe_intercambiar = False
            if descendente:
                debe_intercambiar = poblacion_actual < poblacion_siguiente
            else:
                debe_intercambiar = poblacion_actual > poblacion_siguiente
            
            if debe_intercambiar:
                paises_ordenados[j], paises_ordenados[j + 1] = \
                    paises_ordenados[j + 1], paises_ordenados[j]
                intercambio_realizado = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio_realizado:
            break
    
    return paises_ordenados


def ordenar_por_superficie(paises: List[Dict[str, Any]], descendente: bool = False) -> List[Dict[str, Any]]:
    """
    Ordena países por superficie usando ordenamiento por inserción.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        descendente (bool): Si debe ordenar de forma descendente
        
    Returns:
        List[Dict[str, Any]]: Lista de países ordenada
    """
    if not paises:
        return []
    
    paises_ordenados = paises.copy()
    n = len(paises_ordenados)
    
    # Ordenamiento por inserción
    for i in range(1, n):
        pais_actual = paises_ordenados[i]
        superficie_actual = pais_actual['superficie']
        j = i - 1
        
        while j >= 0:
            superficie_comparar = paises_ordenados[j]['superficie']
            
            debe_mover = False
            if descendente:
                debe_mover = superficie_actual > superficie_comparar
            else:
                debe_mover = superficie_actual < superficie_comparar
            
            if debe_mover:
                paises_ordenados[j + 1] = paises_ordenados[j]
                j -= 1
            else:
                break
        
        paises_ordenados[j + 1] = pais_actual
    
    return paises_ordenados



def ordenar_personalizado(paises: List[Dict[str, Any]], criterio: str, 
                         descendente: bool = False) -> List[Dict[str, Any]]:
    """
    Ordena países por un criterio personalizado.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        criterio (str): Criterio de ordenamiento
        descendente (bool): Si debe ordenar de forma descendente
        
    Returns:
        List[Dict[str, Any]]: Lista de países ordenada
    """
    criterios_validos = {
        'nombre': ordenar_por_nombre,
        'poblacion': ordenar_por_poblacion,
        'superficie': ordenar_por_superficie,
    }
    
    if criterio not in criterios_validos:
        print(f"❌ Criterio de ordenamiento inválido: {criterio}")
        print(f"Criterios válidos: {', '.join(criterios_validos.keys())}")
        return paises.copy()
    
    return criterios_validos[criterio](paises, descendente)


def obtener_top_paises(paises: List[Dict[str, Any]], criterio: str, 
                      cantidad: int, descendente: bool = True) -> List[Dict[str, Any]]:
    """
    Obtiene los países top según un criterio.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        criterio (str): Criterio de ordenamiento
        cantidad (int): Cantidad de países a retornar
        descendente (bool): Si debe ordenar de forma descendente
        
    Returns:
        List[Dict[str, Any]]: Lista de países top
    """
    if not paises or cantidad <= 0:
        return []
    
    paises_ordenados = ordenar_personalizado(paises, criterio, descendente)
    return paises_ordenados[:cantidad]


def obtener_bottom_paises(paises: List[Dict[str, Any]], criterio: str, 
                         cantidad: int) -> List[Dict[str, Any]]:
    """
    Obtiene los países bottom según un criterio.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        criterio (str): Criterio de ordenamiento
        cantidad (int): Cantidad de países a retornar
        
    Returns:
        List[Dict[str, Any]]: Lista de países bottom
    """
    return obtener_top_paises(paises, criterio, cantidad, descendente=False)

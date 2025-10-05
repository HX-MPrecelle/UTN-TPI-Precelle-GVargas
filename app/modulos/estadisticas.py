"""
Módulo de Estadísticas
=====================
Este módulo contiene funciones para calcular estadísticas descriptivas
y generar reportes sobre los datos de países.
"""

from typing import List, Dict, Any
from collections import defaultdict
import math


def calcular_estadisticas_generales(paises: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calcula estadísticas generales de todos los países.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        Dict[str, Any]: Diccionario con estadísticas generales
    """
    if not paises:
        return {}
    
    total_paises = len(paises)
    poblaciones = [pais['poblacion'] for pais in paises]
    superficies = [pais['superficie'] for pais in paises]
    
    # Estadísticas básicas
    poblacion_total = sum(poblaciones)
    superficie_total = sum(superficies)

    # Países extremos por población
    pais_mayor_poblacion = max(paises, key=lambda x: x['poblacion'])
    pais_menor_poblacion = min(paises, key=lambda x: x['poblacion'])
    
    # Países extremos por superficie
    pais_mayor_superficie = max(paises, key=lambda x: x['superficie'])
    pais_menor_superficie = min(paises, key=lambda x: x['superficie'])
    
    # Estadísticas de dispersión
    poblacion_promedio = poblacion_total / total_paises
    superficie_promedio = superficie_total / total_paises
    
    # Varianza y desviación estándar para población
    varianza_poblacion = sum((p - poblacion_promedio) ** 2 for p in poblaciones) / total_paises
    desviacion_poblacion = math.sqrt(varianza_poblacion)
    
    # Varianza y desviación estándar para superficie
    varianza_superficie = sum((s - superficie_promedio) ** 2 for s in superficies) / total_paises
    desviacion_superficie = math.sqrt(varianza_superficie)
    
    return {
        'total_paises': total_paises,
        'poblacion_total': poblacion_total,
        'superficie_total': superficie_total,
        'poblacion_promedio': round(poblacion_promedio, 2),
        'superficie_promedio': round(superficie_promedio, 2),
        'pais_mayor_poblacion': pais_mayor_poblacion,
        'pais_menor_poblacion': pais_menor_poblacion,
        'pais_mayor_superficie': pais_mayor_superficie,
        'pais_menor_superficie': pais_menor_superficie,
        'desviacion_poblacion': round(desviacion_poblacion, 2),
        'desviacion_superficie': round(desviacion_superficie, 2)
    }


def calcular_estadisticas_continente(paises: List[Dict[str, Any]], continente: str) -> Dict[str, Any]:
    """
    Calcula estadísticas para un continente específico.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        continente (str): Nombre del continente
        
    Returns:
        Dict[str, Any]: Estadísticas del continente especificado
    """
    if not paises or not continente:
        return {}
    
    # Filtrar países del continente
    paises_continente = [p for p in paises if p['continente'] == continente]
    if not paises_continente:
        return {}
    
    # Calcular estadísticas usando la función general
    return calcular_estadisticas_generales(paises_continente)


def calcular_estadisticas_por_continente(paises: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Calcula estadísticas agrupadas por continente.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        Dict[str, Dict[str, Any]]: Diccionario con estadísticas por continente
    """
    if not paises:
        return {}
    
    # Agrupar países por continente
    paises_por_continente = defaultdict(list)
    for pais in paises:
        paises_por_continente[pais['continente']].append(pais)
    
    estadisticas_continentes = {}
    
    for continente, paises_continente in paises_por_continente.items():
        estadisticas = calcular_estadisticas_generales(paises_continente)
        estadisticas_continentes[continente] = estadisticas
    
    return estadisticas_continentes


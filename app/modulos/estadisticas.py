"""
Módulo de Estadísticas
=====================
Este módulo contiene funciones para calcular estadísticas descriptivas
y generar reportes sobre los datos de países.
"""

from typing import List, Dict, Any, Optional, Tuple
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
    densidades = [pais['densidad'] for pais in paises]
    
    # Estadísticas básicas
    poblacion_total = sum(poblaciones)
    superficie_total = sum(superficies)
    densidad_promedio = poblacion_total / superficie_total if superficie_total > 0 else 0
    
    # Países extremos por población
    pais_mayor_poblacion = max(paises, key=lambda x: x['poblacion'])
    pais_menor_poblacion = min(paises, key=lambda x: x['poblacion'])
    
    # Países extremos por superficie
    pais_mayor_superficie = max(paises, key=lambda x: x['superficie'])
    pais_menor_superficie = min(paises, key=lambda x: x['superficie'])
    
    # Países extremos por densidad
    pais_mayor_densidad = max(paises, key=lambda x: x['densidad'])
    pais_menor_densidad = min(paises, key=lambda x: x['densidad'])
    
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
        'densidad_promedio': round(densidad_promedio, 2),
        'poblacion_promedio': round(poblacion_promedio, 2),
        'superficie_promedio': round(superficie_promedio, 2),
        'pais_mayor_poblacion': pais_mayor_poblacion,
        'pais_menor_poblacion': pais_menor_poblacion,
        'pais_mayor_superficie': pais_mayor_superficie,
        'pais_menor_superficie': pais_menor_superficie,
        'pais_mayor_densidad': pais_mayor_densidad,
        'pais_menor_densidad': pais_menor_densidad,
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


def calcular_mediana(lista_numeros: List[float]) -> float:
    """
    Calcula la mediana de una lista de números.
    
    Args:
        lista_numeros (List[float]): Lista de números
        
    Returns:
        float: Mediana de la lista
    """
    if not lista_numeros:
        return 0
    
    lista_ordenada = sorted(lista_numeros)
    n = len(lista_ordenada)
    
    if n % 2 == 0:
        # Si hay un número par de elementos, promedio de los dos del medio
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        # Si hay un número impar de elementos, el del medio
        return lista_ordenada[n // 2]


def calcular_cuartiles(lista_numeros: List[float]) -> Dict[str, float]:
    """
    Calcula los cuartiles de una lista de números.
    
    Args:
        lista_numeros (List[float]): Lista de números
        
    Returns:
        Dict[str, float]: Diccionario con Q1, Q2 (mediana) y Q3
    """
    if not lista_numeros:
        return {'Q1': 0, 'Q2': 0, 'Q3': 0}
    
    lista_ordenada = sorted(lista_numeros)
    n = len(lista_ordenada)
    
    # Q2 es la mediana
    Q2 = calcular_mediana(lista_ordenada)
    
    # Q1 es la mediana de la primera mitad
    primera_mitad = lista_ordenada[:n // 2]
    Q1 = calcular_mediana(primera_mitad)
    
    # Q3 es la mediana de la segunda mitad
    segunda_mitad = lista_ordenada[n // 2 + (n % 2):]
    Q3 = calcular_mediana(segunda_mitad)
    
    return {'Q1': Q1, 'Q2': Q2, 'Q3': Q3}


def calcular_percentiles(lista_numeros: List[float], percentil: float) -> float:
    """
    Calcula un percentil específico de una lista de números.
    
    Args:
        lista_numeros (List[float]): Lista de números
        percentil (float): Percentil a calcular (0-100)
        
    Returns:
        float: Valor del percentil
    """
    if not lista_numeros or percentil < 0 or percentil > 100:
        return 0
    
    lista_ordenada = sorted(lista_numeros)
    n = len(lista_ordenada)
    
    # Calcular posición del percentil
    posicion = (percentil / 100) * (n - 1)
    
    # Si la posición es entera, tomar ese elemento
    if posicion == int(posicion):
        return lista_ordenada[int(posicion)]
    
    # Si no, interpolar entre los dos elementos más cercanos
    pos_inf = int(posicion)
    pos_sup = pos_inf + 1
    
    valor_inf = lista_ordenada[pos_inf]
    valor_sup = lista_ordenada[pos_sup]
    
    # Interpolación lineal
    fraccion = posicion - pos_inf
    return valor_inf + fraccion * (valor_sup - valor_inf)


def analizar_distribucion_poblacion(paises: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analiza la distribución de población entre los países.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        Dict[str, Any]: Análisis de distribución de población
    """
    if not paises:
        return {}
    
    poblaciones = [pais['poblacion'] for pais in paises]
    
    # Calcular estadísticas descriptivas
    cuartiles = calcular_cuartiles(poblaciones)
    percentil_90 = calcular_percentiles(poblaciones, 90)
    percentil_95 = calcular_percentiles(poblaciones, 95)
    percentil_99 = calcular_percentiles(poblaciones, 99)
    
    # Clasificar países por tamaño poblacional
    paises_grandes = [p for p in paises if p['poblacion'] >= percentil_90]
    paises_medianos = [p for p in paises if percentil_90 > p['poblacion'] >= cuartiles['Q2']]
    paises_pequeños = [p for p in paises if p['poblacion'] < cuartiles['Q2']]
    
    return {
        'cuartiles': cuartiles,
        'percentil_90': percentil_90,
        'percentil_95': percentil_95,
        'percentil_99': percentil_99,
        'paises_grandes': len(paises_grandes),
        'paises_medianos': len(paises_medianos),
        'paises_pequeños': len(paises_pequeños),
        'lista_grandes': paises_grandes[:10],  # Top 10
        'lista_pequeños': paises_pequeños[:10]  # Bottom 10
    }


def analizar_distribucion_superficie(paises: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analiza la distribución de superficie entre los países.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        Dict[str, Any]: Análisis de distribución de superficie
    """
    if not paises:
        return {}
    
    superficies = [pais['superficie'] for pais in paises]
    
    # Calcular estadísticas descriptivas
    cuartiles = calcular_cuartiles(superficies)
    percentil_90 = calcular_percentiles(superficies, 90)
    
    # Clasificar países por superficie
    paises_extensos = [p for p in paises if p['superficie'] >= percentil_90]
    paises_medianos = [p for p in paises if percentil_90 > p['superficie'] >= cuartiles['Q2']]
    paises_pequeños = [p for p in paises if p['superficie'] < cuartiles['Q2']]
    
    return {
        'cuartiles': cuartiles,
        'percentil_90': percentil_90,
        'paises_extensos': len(paises_extensos),
        'paises_medianos': len(paises_medianos),
        'paises_pequeños': len(paises_pequeños),
        'lista_extensos': paises_extensos[:10],  # Top 10
        'lista_pequeños': paises_pequeños[:10]  # Bottom 10
    }


def calcular_correlacion_poblacion_superficie(paises: List[Dict[str, Any]]) -> float:
    """
    Calcula la correlación entre población y superficie.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        float: Coeficiente de correlación de Pearson
    """
    if len(paises) < 2:
        return 0
    
    poblaciones = [pais['poblacion'] for pais in paises]
    superficies = [pais['superficie'] for pais in paises]
    
    n = len(poblaciones)
    
    # Calcular medias
    media_poblacion = sum(poblaciones) / n
    media_superficie = sum(superficies) / n
    
    # Calcular covarianza
    covarianza = sum((p - media_poblacion) * (s - media_superficie) 
                    for p, s in zip(poblaciones, superficies)) / n
    
    # Calcular desviaciones estándar
    var_poblacion = sum((p - media_poblacion) ** 2 for p in poblaciones) / n
    var_superficie = sum((s - media_superficie) ** 2 for s in superficies) / n
    
    desv_poblacion = math.sqrt(var_poblacion)
    desv_superficie = math.sqrt(var_superficie)
    
    # Calcular correlación
    if desv_poblacion == 0 or desv_superficie == 0:
        return 0
    
    correlacion = covarianza / (desv_poblacion * desv_superficie)
    return round(correlacion, 4)


def generar_reporte_completo(paises: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Genera un reporte completo con todas las estadísticas.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        Dict[str, Any]: Reporte completo con todas las estadísticas
    """
    if not paises:
        return {}
    
    return {
        'estadisticas_generales': calcular_estadisticas_generales(paises),
        'estadisticas_continentes': calcular_estadisticas_por_continente(paises),
        'distribucion_poblacion': analizar_distribucion_poblacion(paises),
        'distribucion_superficie': analizar_distribucion_superficie(paises),
        'correlacion_poblacion_superficie': calcular_correlacion_poblacion_superficie(paises),
        'total_continentes': len(set(pais['continente'] for pais in paises))
    }


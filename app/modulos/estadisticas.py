"""
Módulo de Estadísticas
=====================
Este módulo contiene funciones para calcular estadísticas descriptivas
y generar reportes sobre los datos de países.
"""

from typing import List, Dict, Any
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
    poblaciones_ordenadas = sorted(poblaciones)
    n = len(poblaciones_ordenadas)
    
    # Calcular percentil 90 (simplificado)
    posicion_90 = int(0.9 * (n - 1))
    percentil_90 = poblaciones_ordenadas[posicion_90] if posicion_90 < n else poblaciones_ordenadas[-1]
    
    # Calcular mediana (percentil 50)
    if n % 2 == 0:
        mediana = (poblaciones_ordenadas[n // 2 - 1] + poblaciones_ordenadas[n // 2]) / 2
    else:
        mediana = poblaciones_ordenadas[n // 2]
    
    # Clasificar países por tamaño poblacional
    paises_grandes = [p for p in paises if p['poblacion'] >= percentil_90]
    paises_pequeños = [p for p in paises if p['poblacion'] < mediana]
    
    return {
        'percentil_90': percentil_90,
        'mediana': mediana,
        'paises_grandes': len(paises_grandes),
        'paises_pequeños': len(paises_pequeños),
        'lista_grandes': paises_grandes[:10]  # Top 10
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




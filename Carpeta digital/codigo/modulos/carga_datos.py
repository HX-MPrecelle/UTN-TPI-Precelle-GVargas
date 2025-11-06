"""
Módulo de Carga de Datos
========================
Este módulo se encarga de cargar y procesar los datos desde archivos CSV.
Incluye funciones para validar el formato de los datos y manejar errores.
"""
import csv
import os
from typing import List, Dict, Any

def cargar_datos_csv(ruta_archivo: str) -> List[Dict[str, Any]]:
    """
    Carga datos de países desde un archivo CSV.
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV con los datos
        
    Returns:
        List[Dict[str, Any]]: Lista de diccionarios con los datos de países
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si hay errores en el formato de los datos
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    
    paises = []
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            # Verificar que las columnas requeridas estén presentes
            columnas_requeridas = ['nombre', 'poblacion', 'superficie', 'continente']
            if not all(col in lector_csv.fieldnames for col in columnas_requeridas):
                raise ValueError("El archivo CSV no contiene todas las columnas requeridas")
            for numero_fila, fila in enumerate(lector_csv, start=2):  # Empezamos en 2 porque la fila 1 es el header
                try:
                    # Validar y convertir los datos
                    pais = validar_fila_pais(fila, numero_fila)
                    paises.append(pais)
                except ValueError as e:
                    print(f"Advertencia: Error en fila {numero_fila}: {e}")
                    continue
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV: {e}")
    
    if not paises:
        raise ValueError("No se pudieron cargar datos válidos del archivo")
    print(f"✓ Datos cargados exitosamente: {len(paises)} países")
    return paises


def validar_fila_pais(fila: Dict[str, str], numero_fila: int) -> Dict[str, Any]:
    """
    Valida y convierte una fila del CSV a un diccionario de país.
    
    Args:
        fila (Dict[str, str]): Fila del CSV como diccionario
        numero_fila (int): Número de fila para reportar errores
        
    Returns:
        Dict[str, Any]: Diccionario con los datos validados del país
        
    Raises:
        ValueError: Si los datos no son válidos
    """
    # Validar nombre
    nombre = fila['nombre'].strip()
    if not nombre:
        raise ValueError("El nombre del país no puede estar vacío")
    
    # Validar y convertir población
    try:
        poblacion = int(fila['poblacion'].replace(',', '').replace('.', ''))
        if poblacion <= 0:
            raise ValueError("La población debe ser un número positivo")
    except (ValueError, TypeError):
        raise ValueError(f"Población inválida: '{fila['poblacion']}'")
    
    # Validar y convertir superficie
    try:
        superficie = int(fila['superficie'].replace(',', '').replace('.', ''))
        if superficie <= 0:
            raise ValueError("La superficie debe ser un número positivo")
    except (ValueError, TypeError):
        raise ValueError(f"Superficie inválida: '{fila['superficie']}'")
    
    # Validar continente
    continente = fila['continente'].strip()
    if not continente:
        raise ValueError("El continente no puede estar vacío")
    
    # Crear diccionario del país
    pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente,
    }
    
    return pais


def verificar_integridad_datos(paises: List[Dict[str, Any]]) -> bool:
    """
    Verifica la integridad de los datos cargados.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        
    Returns:
        bool: True si los datos son válidos, False en caso contrario
    """
    if not paises:
        print("❌ Error: No hay países cargados")
        return False
    
    # Verificar que todos los países tengan los campos requeridos
    campos_requeridos = ['nombre', 'poblacion', 'superficie', 'continente']
    
    for i, pais in enumerate(paises):
        for campo in campos_requeridos:
            if campo not in pais:
                print(f"❌ Error: País {i+1} no tiene el campo '{campo}'")
                return False
        
        # Verificar que los valores numéricos sean válidos
        if pais['poblacion'] <= 0:
            print(f"❌ Error: País {pais['nombre']} tiene población inválida")
            return False
        
        if pais['superficie'] <= 0:
            print(f"❌ Error: País {pais['nombre']} tiene superficie inválida")
            return False
    
    print("✓ Integridad de datos verificada correctamente")
    return True




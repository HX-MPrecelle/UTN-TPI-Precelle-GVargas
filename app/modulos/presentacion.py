"""
Módulo de Presentación
=====================
Este módulo contiene funciones para mostrar información de manera clara
y formateada al usuario.
"""

from typing import List, Dict, Any, Optional
from .validacion import formatear_numero, mostrar_separador, pausar_ejecucion


def mostrar_pais(pais: Dict[str, Any], mostrar_indice: bool = False, indice: int = 0):
    """
    Muestra la información de un país de forma formateada.
    
    Args:
        pais (Dict[str, Any]): Datos del país
        mostrar_indice (bool): Si debe mostrar el índice
        indice (int): Número de índice
    """
    if not pais:
        print("❌ No hay datos del país para mostrar")
        return
    
    # Formatear números
    poblacion = formatear_numero(pais['poblacion'])
    superficie = formatear_numero(pais['superficie'])
    densidad = f"{pais['densidad']:.2f}"
    
    # Mostrar información
    if mostrar_indice:
        print(f"{indice:3d}. ", end="")
    
    print(f"🌍 {pais['nombre']}")
    print(f"   📍 Continente: {pais['continente']}")
    print(f"   👥 Población: {poblacion} habitantes")
    print(f"   📏 Superficie: {superficie} km²")
    print(f"   🏘️  Densidad: {densidad} hab/km²")
    print()


def mostrar_lista_paises(paises: List[Dict[str, Any]], titulo: str = "Países", 
                        mostrar_indices: bool = True, max_paises: Optional[int] = None):
    """
    Muestra una lista de países de forma formateada.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        titulo (str): Título de la sección
        mostrar_indices (bool): Si debe mostrar índices
        max_paises (int, optional): Máximo número de países a mostrar
    """
    if not paises:
        print(f"❌ No se encontraron países para mostrar en: {titulo}")
        return
    
    # Limitar cantidad si se especifica
    paises_a_mostrar = paises[:max_paises] if max_paises else paises
    
    print(f"\n📋 {titulo} ({len(paises_a_mostrar)} países)")
    mostrar_separador("-", 50)
    
    for i, pais in enumerate(paises_a_mostrar, 1):
        mostrar_pais(pais, mostrar_indices, i)
    
    # Mostrar información adicional si se limitó la lista
    if max_paises and len(paises) > max_paises:
        print(f"... y {len(paises) - max_paises} países más")
    
    print(f"Total: {len(paises)} países")


def mostrar_estadisticas_generales(estadisticas: Dict[str, Any]):
    """
    Muestra las estadísticas generales de forma formateada.
    
    Args:
        estadisticas (Dict[str, Any]): Estadísticas a mostrar
    """
    if not estadisticas:
        print("❌ No hay estadísticas para mostrar")
        return
    
    print("\n📊 ESTADÍSTICAS GENERALES")
    mostrar_separador("=", 60)
    
    # Estadísticas básicas
    print(f"📈 Total de países: {estadisticas['total_paises']}")
    print(f"👥 Población mundial: {formatear_numero(estadisticas['poblacion_total'])} habitantes")
    print(f"📏 Superficie mundial: {formatear_numero(estadisticas['superficie_total'])} km²")
    print(f"🏘️  Densidad promedio: {estadisticas['densidad_promedio']} hab/km²")
    
    print(f"\n📊 Población promedio: {formatear_numero(estadisticas['poblacion_promedio'])} habitantes")
    print(f"📊 Superficie promedio: {formatear_numero(estadisticas['superficie_promedio'])} km²")
    
    # Países extremos
    print(f"\n🏆 EXTREMOS:")
    print(f"   Mayor población: {estadisticas['pais_mayor_poblacion']['nombre']} "
          f"({formatear_numero(estadisticas['pais_mayor_poblacion']['poblacion'])} hab)")
    print(f"   Menor población: {estadisticas['pais_menor_poblacion']['nombre']} "
          f"({formatear_numero(estadisticas['pais_menor_poblacion']['poblacion'])} hab)")
    print(f"   Mayor superficie: {estadisticas['pais_mayor_superficie']['nombre']} "
          f"({formatear_numero(estadisticas['pais_mayor_superficie']['superficie'])} km²)")
    print(f"   Menor superficie: {estadisticas['pais_menor_superficie']['nombre']} "
          f"({formatear_numero(estadisticas['pais_menor_superficie']['superficie'])} km²)")


def mostrar_estadisticas_continente(estadisticas: Dict[str, Any], continente: str):
    """
    Muestra las estadísticas de un continente específico.
    
    Args:
        estadisticas (Dict[str, Any]): Estadísticas del continente
        continente (str): Nombre del continente
    """
    if not estadisticas:
        print(f"❌ No hay estadísticas para el continente: {continente}")
        return
    
    print(f"\n🌍 ESTADÍSTICAS DE {continente.upper()}")
    mostrar_separador("=", 50)
    
    print(f"📈 Total de países: {estadisticas['total_paises']}")
    print(f"👥 Población total: {formatear_numero(estadisticas['poblacion_total'])} habitantes")
    print(f"📏 Superficie total: {formatear_numero(estadisticas['superficie_total'])} km²")
    print(f"🏘️  Densidad promedio: {estadisticas['densidad_promedio']} hab/km²")
    
    # Países extremos del continente
    print(f"\n🏆 EXTREMOS EN {continente.upper()}:")
    print(f"   Mayor población: {estadisticas['pais_mayor_poblacion']['nombre']} "
          f"({formatear_numero(estadisticas['pais_mayor_poblacion']['poblacion'])} hab)")
    print(f"   Menor población: {estadisticas['pais_menor_poblacion']['nombre']} "
          f"({formatear_numero(estadisticas['pais_menor_poblacion']['poblacion'])} hab)")


def mostrar_menu_principal():
    """Muestra el menú principal de la aplicación."""
    print("\n" + "="*60)
    print("🌍 SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("="*60)
    print("1. 🔍 Buscar país por nombre")
    print("2. 🌎 Filtrar países por continente")
    print("3. 📊 Filtrar países por rango de población")
    print("4. 📏 Filtrar países por rango de superficie")
    print("5. 📈 Ordenar países por criterio")
    print("6. 🏆 Mostrar top países")
    print("7. 📊 Mostrar estadísticas generales")
    print("8. 🌍 Mostrar estadísticas por continente")
    print("9. 🔎 Búsqueda avanzada (múltiples criterios)")
    print("10. 📋 Mostrar todos los países")
    print("11. 💾 Exportar resultados a archivo")
    print("0. 🚪 Salir")
    print("="*60)


def mostrar_submenu_ordenamiento():
    """Muestra el submenú de ordenamiento."""
    print("\n📈 ORDENAR PAÍSES POR:")
    print("1. Nombre (A-Z)")
    print("2. Nombre (Z-A)")
    print("3. Población (Mayor a menor)")
    print("4. Población (Menor a mayor)")
    print("5. Superficie (Mayor a menor)")
    print("6. Superficie (Menor a mayor)")
    print("7. Densidad (Mayor a menor)")
    print("8. Densidad (Menor a mayor)")
    print("0. Volver al menú principal")


def mostrar_submenu_top():
    """Muestra el submenú de top países."""
    print("\n🏆 MOSTRAR TOP PAÍSES POR:")
    print("1. Población (Mayor a menor)")
    print("2. Superficie (Mayor a menor)")
    print("3. Densidad (Mayor a menor)")
    print("4. Población (Menor a mayor)")
    print("5. Superficie (Menor a mayor)")
    print("6. Densidad (Menor a mayor)")
    print("0. Volver al menú principal")


def mostrar_continentes_disponibles(continentes: List[str]):
    """
    Muestra la lista de continentes disponibles.
    
    Args:
        continentes (List[str]): Lista de continentes
    """
    print("\n🌍 CONTINENTES DISPONIBLES:")
    mostrar_separador("-", 30)
    for i, continente in enumerate(continentes, 1):
        print(f"{i:2d}. {continente}")


def mostrar_resultados_busqueda(paises: List[Dict[str, Any]], tipo_busqueda: str):
    """
    Muestra los resultados de una búsqueda.
    
    Args:
        paises (List[Dict[str, Any]]): Países encontrados
        tipo_busqueda (str): Tipo de búsqueda realizada
    """
    if not paises:
        print(f"❌ No se encontraron países con la búsqueda: {tipo_busqueda}")
        return
    
    print(f"\n✅ Búsqueda exitosa: {tipo_busqueda}")
    print(f"📊 Se encontraron {len(paises)} países")
    
    # Mostrar solo los primeros 10 países
    paises_a_mostrar = paises[:10]
    mostrar_lista_paises(paises_a_mostrar, f"Resultados de: {tipo_busqueda}")
    
    if len(paises) > 10:
        print(f"\n💡 Se encontraron {len(paises)} países. Mostrando los primeros 10.")
        print("   Use la opción 'Mostrar todos los países' para ver la lista completa.")


def mostrar_distribucion_poblacion(distribucion: Dict[str, Any]):
    """
    Muestra el análisis de distribución de población.
    
    Args:
        distribucion (Dict[str, Any]): Análisis de distribución
    """
    if not distribucion:
        print("❌ No hay datos de distribución para mostrar")
        return
    
    print("\n📊 DISTRIBUCIÓN DE POBLACIÓN")
    mostrar_separador("=", 50)
    
    print(f"📈 Distribución de población:")
    print(f"   Percentil 90: {formatear_numero(distribucion['percentil_90'])} habitantes")
    print(f"   Mediana: {formatear_numero(distribucion['mediana'])} habitantes")
    
    print(f"\n📊 Clasificación por tamaño:")
    print(f"   🌟 Países grandes (top 10%): {distribucion['paises_grandes']} países")
    print(f"   📉 Países pequeños (bottom 50%): {distribucion['paises_pequeños']} países")
    
    # Mostrar algunos ejemplos
    if distribucion['lista_grandes']:
        print(f"\n🏆 Top 5 países más poblados:")
        for i, pais in enumerate(distribucion['lista_grandes'][:5], 1):
            print(f"   {i}. {pais['nombre']}: {formatear_numero(pais['poblacion'])} habitantes")


def mostrar_correlacion(correlacion: float):
    """
    Muestra la correlación entre población y superficie.
    
    Args:
        correlacion (float): Coeficiente de correlación
    """
    print(f"\n📊 CORRELACIÓN POBLACIÓN-SUPERFICIE")
    mostrar_separador("-", 40)
    
    print(f"🔗 Coeficiente de correlación: {correlacion}")
    
    if correlacion > 0.7:
        interpretacion = "Correlación fuerte positiva"
    elif correlacion > 0.3:
        interpretacion = "Correlación moderada positiva"
    elif correlacion > -0.3:
        interpretacion = "Correlación débil o nula"
    elif correlacion > -0.7:
        interpretacion = "Correlación moderada negativa"
    else:
        interpretacion = "Correlación fuerte negativa"
    
    print(f"📝 Interpretación: {interpretacion}")



def exportar_a_archivo(paises: List[Dict[str, Any]], nombre_archivo: str, 
                      formato: str = 'txt') -> bool:
    """
    Exporta una lista de países a un archivo.
    
    Args:
        paises (List[Dict[str, Any]]): Lista de países
        nombre_archivo (str): Nombre del archivo
        formato (str): Formato de exportación ('txt' o 'csv')
        
    Returns:
        bool: True si la exportación fue exitosa
    """
    try:
        if formato == 'txt':
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write("LISTA DE PAÍSES\n")
                archivo.write("=" * 50 + "\n\n")
                
                for i, pais in enumerate(paises, 1):
                    archivo.write(f"{i}. {pais['nombre']}\n")
                    archivo.write(f"   Continente: {pais['continente']}\n")
                    archivo.write(f"   Población: {formatear_numero(pais['poblacion'])} habitantes\n")
                    archivo.write(f"   Superficie: {formatear_numero(pais['superficie'])} km²\n")
                    archivo.write(f"   Densidad: {pais['densidad']:.2f} hab/km²\n\n")
        
        elif formato == 'csv':
            import csv
            with open(nombre_archivo, 'w', encoding='utf-8', newline='') as archivo:
                if paises:
                    campos = paises[0].keys()
                    escritor = csv.DictWriter(archivo, fieldnames=campos)
                    escritor.writeheader()
                    escritor.writerows(paises)
        
        print(f"✅ Archivo exportado exitosamente: {nombre_archivo}")
        return True
        
    except Exception as e:
        print(f"❌ Error al exportar archivo: {e}")
        return False


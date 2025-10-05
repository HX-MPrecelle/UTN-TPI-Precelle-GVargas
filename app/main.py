#!/usr/bin/env python3
"""
Sistema de Gestión de Datos de Países - Aplicación Principal
============================================================
Trabajo Práctico Integrador (TPI) - Programación I
Universidad Tecnológica Nacional (UTN)

Integrantes:
- Precelle, Martín Nicolás
- García Vargas, Marcos

Este archivo contiene la aplicación principal que coordina todos los módulos
del sistema de gestión de datos de países.
"""

import sys
import os

# Agregar el directorio de módulos al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modulos'))

# Importar todos los módulos
from modulos.carga_datos import cargar_datos_csv, verificar_integridad_datos
from modulos.validacion import (
    validar_entrada_numero, 
    pausar_ejecucion, mostrar_separador
)
from modulos.consultas import (
    buscar_pais_por_nombre, filtrar_por_continente,
    filtrar_por_rango_poblacion, filtrar_por_rango_superficie,
    buscar_paises_multiples_criterios, obtener_continentes_disponibles,
    buscar_paises_top, buscar_paises_bottom
)
from modulos.ordenamiento import ordenar_personalizado
from modulos.estadisticas import (
    calcular_estadisticas_generales, calcular_estadisticas_continente,
    analizar_distribucion_poblacion, calcular_correlacion_poblacion_superficie
)
from modulos.presentacion import (
    mostrar_menu_principal, mostrar_submenu_ordenamiento, mostrar_submenu_top,
    mostrar_continentes_disponibles, mostrar_resultados_busqueda,
    mostrar_lista_paises, mostrar_estadisticas_generales,
    mostrar_estadisticas_continente, exportar_a_archivo
)

# Variables globales
paises = []
resultados_actuales = []


def inicializar_datos() -> bool:
    """
    Carga e inicializa los datos de países desde el archivo CSV.
    
    Returns:
        bool: True si la carga fue exitosa, False en caso contrario
    """
    global paises
    
    print("🔄 Iniciando sistema...")
    mostrar_separador("-", 50)
    
    try:
        # Cargar datos
        ruta_datos = 'data/paises.csv'
        print(f"📂 Cargando datos desde: {ruta_datos}")
        paises = cargar_datos_csv(ruta_datos)
        
        if not paises:
            print("❌ No se pudieron cargar los datos del archivo CSV")
            return False
        
        # Verificar integridad
        print("🔍 Verificando integridad de datos...")
        if not verificar_integridad_datos(paises):
            print("❌ Los datos no pasaron la verificación de integridad")
            return False
        
        print(f"✅ Sistema inicializado correctamente")
        print(f"📊 {len(paises)} países cargados exitosamente")
        mostrar_separador("-", 50)
        return True
        
    except Exception as e:
        print(f"❌ Error al inicializar el sistema: {e}")
        return False


def ejecutar_busqueda_por_nombre():
    """Ejecuta la búsqueda de países por nombre."""
    global resultados_actuales
    
    print("\n🔍 BÚSQUEDA POR NOMBRE")
    mostrar_separador("-", 30)
    
    nombre = input("Ingrese el nombre del país a buscar: ").strip()
    if not nombre:
        print("❌ Debe ingresar un nombre válido")
        return
    
    # Buscar países
    resultados = buscar_pais_por_nombre(paises, nombre)
    resultados_actuales = resultados
    
    # Mostrar resultados
    mostrar_resultados_busqueda(resultados, f"Países que contienen '{nombre}'")
    
    pausar_ejecucion()


def ejecutar_filtro_por_continente():
    """Ejecuta el filtrado de países por continente."""
    global resultados_actuales
    
    print("\n🌍 FILTRADO POR CONTINENTE")
    mostrar_separador("-", 35)
    
    # Mostrar continentes disponibles
    continentes = obtener_continentes_disponibles(paises)
    mostrar_continentes_disponibles(continentes)
    
    # Solicitar selección
    try:
        opcion = int(input(f"\nSeleccione un continente (1-{len(continentes)}): "))
        if 1 <= opcion <= len(continentes):
            continente_seleccionado = continentes[opcion - 1]
            resultados = filtrar_por_continente(paises, continente_seleccionado)
            resultados_actuales = resultados
            
            mostrar_resultados_busqueda(resultados, f"Países de {continente_seleccionado}")
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Debe ingresar un número válido")
    
    pausar_ejecucion()


def ejecutar_filtro_por_poblacion():
    """Ejecuta el filtrado de países por rango de población."""
    global resultados_actuales
    
    print("\n📊 FILTRADO POR POBLACIÓN")
    mostrar_separador("-", 35)
    
    try:
        poblacion_min = validar_entrada_numero(
            input("Ingrese población mínima: "), 0, 2000000000
        )
        poblacion_max = validar_entrada_numero(
            input("Ingrese población máxima: "), poblacion_min, 2000000000
        )
        
        if poblacion_min is not None and poblacion_max is not None:
            resultados = filtrar_por_rango_poblacion(
                paises, poblacion_min, poblacion_max
            )
            resultados_actuales = resultados
            
            mostrar_resultados_busqueda(
                resultados, 
                f"Países con población entre {poblacion_min:,} y {poblacion_max:,} habitantes"
            )
    except Exception as e:
        print(f"❌ Error en el filtrado: {e}")
    
    pausar_ejecucion()


def ejecutar_filtro_por_superficie():
    """Ejecuta el filtrado de países por rango de superficie."""
    global resultados_actuales
    
    print("\n📏 FILTRADO POR SUPERFICIE")
    mostrar_separador("-", 35)
    
    try:
        superficie_min = validar_entrada_numero(
            input("Ingrese superficie mínima (km²): "), 0, 20000000
        )
        superficie_max = validar_entrada_numero(
            input("Ingrese superficie máxima (km²): "), superficie_min, 20000000
        )
        
        if superficie_min is not None and superficie_max is not None:
            resultados = filtrar_por_rango_superficie(
                paises, superficie_min, superficie_max
            )
            resultados_actuales = resultados
            
            mostrar_resultados_busqueda(
                resultados, 
                f"Países con superficie entre {superficie_min:,} y {superficie_max:,} km²"
            )
    except Exception as e:
        print(f"❌ Error en el filtrado: {e}")
    
    pausar_ejecucion()


def ejecutar_ordenamiento():
    """Ejecuta el ordenamiento de países."""
    global resultados_actuales
    
    print("\n📈 ORDENAMIENTO DE PAÍSES")
    mostrar_separador("-", 35)
    
    # Mostrar submenú de ordenamiento
    mostrar_submenu_ordenamiento()
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        
        # Mapeo de opciones a criterios y direcciones
        opciones_ordenamiento = {
            1: ('nombre', False),      # A-Z
            2: ('nombre', True),       # Z-A
            3: ('poblacion', True),    # Mayor a menor
            4: ('poblacion', False),   # Menor a mayor
            5: ('superficie', True),   # Mayor a menor
            6: ('superficie', False),  # Menor a mayor
            7: ('densidad', True),     # Mayor a menor
            8: ('densidad', False)     # Menor a mayor
        }
        
        if opcion in opciones_ordenamiento:
            criterio, descendente = opciones_ordenamiento[opcion]
            
            # Determinar qué datos ordenar
            datos_a_ordenar = resultados_actuales if resultados_actuales else paises
            
            resultados = ordenar_personalizado(datos_a_ordenar, criterio, descendente)
            resultados_actuales = resultados
            
            # Mostrar resultados
            direccion = "mayor a menor" if descendente else "menor a mayor"
            titulo = f"Países ordenados por {criterio} ({direccion})"
            mostrar_lista_paises(resultados, titulo, max_paises=20)
            
        elif opcion == 0:
            return  # Volver al menú principal
        else:
            print("❌ Opción inválida")
            
    except ValueError:
        print("❌ Debe ingresar un número válido")
    
    pausar_ejecucion()


def ejecutar_top_paises():
    """Ejecuta la visualización de países top."""
    global resultados_actuales
    
    print("\n🏆 TOP PAÍSES")
    mostrar_separador("-", 25)
    
    # Mostrar submenú de top países
    mostrar_submenu_top()
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        
        # Solicitar cantidad
        cantidad = validar_entrada_numero(
            input("¿Cuántos países desea mostrar? (1-50): "), 1, 50
        )
        
        if cantidad is None:
            return
        
        opciones_top = {
            1: ('poblacion', True),    # Mayor población
            2: ('superficie', True),   # Mayor superficie
            3: ('densidad', True),     # Mayor densidad
            4: ('poblacion', False),   # Menor población
            5: ('superficie', False),  # Menor superficie
            6: ('densidad', False)     # Menor densidad
        }
        
        if opcion in opciones_top:
            criterio, descendente = opciones_top[opcion]
            
            if descendente:
                resultados = buscar_paises_top(paises, criterio, cantidad)
            else:
                resultados = buscar_paises_bottom(paises, criterio, cantidad)
            
            resultados_actuales = resultados
            
            # Mostrar resultados
            direccion = "mayor" if descendente else "menor"
            titulo = f"Top {cantidad} países con {direccion} {criterio}"
            mostrar_lista_paises(resultados, titulo)
            
        elif opcion == 0:
            return  # Volver al menú principal
        else:
            print("❌ Opción inválida")
            
    except ValueError:
        print("❌ Debe ingresar un número válido")
    
    pausar_ejecucion()


def ejecutar_estadisticas_generales():
    """Ejecuta el cálculo y visualización de estadísticas generales."""
    print("\n📊 ESTADÍSTICAS GENERALES")
    mostrar_separador("-", 40)
    
    try:
        estadisticas = calcular_estadisticas_generales(paises)
        if estadisticas:
            mostrar_estadisticas_generales(estadisticas)
            
            # Mostrar análisis adicional
            print("\n📈 ANÁLISIS ADICIONAL")
            mostrar_separador("-", 25)
            
            distribucion = analizar_distribucion_poblacion(paises)
            if distribucion:
                from modulos.presentacion import mostrar_distribucion_poblacion
                mostrar_distribucion_poblacion(distribucion)
            
            correlacion = calcular_correlacion_poblacion_superficie(paises)
            if correlacion is not None:
                from modulos.presentacion import mostrar_correlacion
                mostrar_correlacion(correlacion)
        else:
            print("❌ No se pudieron calcular las estadísticas")
            
    except Exception as e:
        print(f"❌ Error al calcular estadísticas: {e}")
    
    pausar_ejecucion()


def ejecutar_estadisticas_continente():
    """Ejecuta el cálculo y visualización de estadísticas por continente."""
    print("\n🌍 ESTADÍSTICAS POR CONTINENTE")
    mostrar_separador("-", 45)
    
    # Mostrar continentes disponibles
    continentes = obtener_continentes_disponibles(paises)
    mostrar_continentes_disponibles(continentes)
    
    try:
        opcion = int(input(f"\nSeleccione un continente (1-{len(continentes)}): "))
        if 1 <= opcion <= len(continentes):
            continente_seleccionado = continentes[opcion - 1]
            
            estadisticas = calcular_estadisticas_continente(paises, continente_seleccionado)
            if estadisticas:
                mostrar_estadisticas_continente(estadisticas, continente_seleccionado)
            else:
                print(f"❌ No se pudieron calcular las estadísticas para {continente_seleccionado}")
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Debe ingresar un número válido")
    
    pausar_ejecucion()


def ejecutar_busqueda_avanzada():
    """Ejecuta la búsqueda avanzada con múltiples criterios."""
    global resultados_actuales
    
    print("\n🔎 BÚSQUEDA AVANZADA")
    mostrar_separador("-", 30)
    
    print("Complete los criterios que desee aplicar (deje en blanco para omitir):")
    
    # Continente
    continentes = obtener_continentes_disponibles(paises)
    mostrar_continentes_disponibles(continentes)
    
    continente = None
    try:
        opcion_continente = input(f"\nSeleccione continente (1-{len(continentes)}) o Enter para omitir: ").strip()
        if opcion_continente:
            opcion = int(opcion_continente)
            if 1 <= opcion <= len(continentes):
                continente = continentes[opcion - 1]
    except ValueError:
        pass
    
    # Rango de población
    poblacion_min = None
    poblacion_max = None
    try:
        poblacion_min_input = input("Población mínima (Enter para omitir): ").strip()
        if poblacion_min_input:
            poblacion_min = int(poblacion_min_input)
        
        poblacion_max_input = input("Población máxima (Enter para omitir): ").strip()
        if poblacion_max_input:
            poblacion_max = int(poblacion_max_input)
    except ValueError:
        print("⚠️ Valores de población inválidos, se omitirán")
    
    # Rango de superficie
    superficie_min = None
    superficie_max = None
    try:
        superficie_min_input = input("Superficie mínima (km², Enter para omitir): ").strip()
        if superficie_min_input:
            superficie_min = int(superficie_min_input)
        
        superficie_max_input = input("Superficie máxima (km², Enter para omitir): ").strip()
        if superficie_max_input:
            superficie_max = int(superficie_max_input)
    except ValueError:
        print("⚠️ Valores de superficie inválidos, se omitirán")
    
    # Nombre que contenga
    nombre_contiene = input("Nombre debe contener (Enter para omitir): ").strip()
    if not nombre_contiene:
        nombre_contiene = None
    
    # Ejecutar búsqueda
    try:
        resultados = buscar_paises_multiples_criterios(
            paises,
            continente=continente,
            poblacion_min=poblacion_min,
            poblacion_max=poblacion_max,
            superficie_min=superficie_min,
            superficie_max=superficie_max,
            nombre_contiene=nombre_contiene
        )
        
        resultados_actuales = resultados
        
        # Crear descripción de la búsqueda
        criterios = []
        if continente:
            criterios.append(f"continente: {continente}")
        if poblacion_min or poblacion_max:
            criterios.append(f"población: {poblacion_min or 0}-{poblacion_max or '∞'}")
        if superficie_min or superficie_max:
            criterios.append(f"superficie: {superficie_min or 0}-{superficie_max or '∞'}")
        if nombre_contiene:
            criterios.append(f"nombre contiene: '{nombre_contiene}'")
        
        descripcion = "Búsqueda avanzada con criterios: " + ", ".join(criterios)
        mostrar_resultados_busqueda(resultados, descripcion)
        
    except Exception as e:
        print(f"❌ Error en la búsqueda avanzada: {e}")
    
    pausar_ejecucion()


def ejecutar_mostrar_todos():
    """Ejecuta la visualización de todos los países."""
    global resultados_actuales
    
    print("\n📋 TODOS LOS PAÍSES")
    mostrar_separador("-", 25)
    
    # Preguntar si mostrar todos o una cantidad limitada
    try:
        cantidad = input("¿Cuántos países mostrar? (Enter para mostrar todos): ").strip()
        max_paises = None
        
        if cantidad:
            max_paises = validar_entrada_numero(cantidad, 1, len(paises))
            if max_paises is None:
                print("❌ Cantidad inválida, mostrando todos")
                max_paises = None
        
        mostrar_lista_paises(paises, "Todos los países", max_paises=max_paises)
        resultados_actuales = paises
        
    except Exception as e:
        print(f"❌ Error al mostrar países: {e}")
    
    pausar_ejecucion()


def ejecutar_exportar_resultados():
    """Ejecuta la exportación de resultados a archivo."""
    print("\n💾 EXPORTAR RESULTADOS")
    mostrar_separador("-", 30)
    
    if not resultados_actuales:
        print("❌ No hay resultados para exportar")
        print("💡 Realice una búsqueda, filtro u ordenamiento primero")
        pausar_ejecucion()
        return
    
    try:
        # Solicitar nombre de archivo
        nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ").strip()
        if not nombre_archivo:
            nombre_archivo = "resultados_paises"
        
        # Solicitar formato
        print("\nFormatos disponibles:")
        print("1. Texto (.txt)")
        print("2. CSV (.csv)")
        
        formato_opcion = input("Seleccione formato (1-2): ").strip()
        
        if formato_opcion == "1":
            nombre_archivo += ".txt"
            formato = "txt"
        elif formato_opcion == "2":
            nombre_archivo += ".csv"
            formato = "csv"
        else:
            print("❌ Formato inválido, usando texto por defecto")
            nombre_archivo += ".txt"
            formato = "txt"
        
        # Exportar
        if exportar_a_archivo(resultados_actuales, nombre_archivo, formato):
            print(f"✅ {len(resultados_actuales)} países exportados exitosamente")
        
    except Exception as e:
        print(f"❌ Error al exportar: {e}")
    
    pausar_ejecucion()


def ejecutar_menu_principal():
    """Ejecuta el menú principal de la aplicación."""
    while True:
        try:
            mostrar_menu_principal()
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 0:
                print("\n👋 ¡Gracias por usar el Sistema de Gestión de Datos de Países!")
                print("🌍 Desarrollado por: Precelle, Martín Nicolás y García Vargas, Marcos")
                print("🏫 Universidad Tecnológica Nacional - Programación I")
                break
            
            elif opcion == 1:
                ejecutar_busqueda_por_nombre()
            elif opcion == 2:
                ejecutar_filtro_por_continente()
            elif opcion == 3:
                ejecutar_filtro_por_poblacion()
            elif opcion == 4:
                ejecutar_filtro_por_superficie()
            elif opcion == 5:
                ejecutar_ordenamiento()
            elif opcion == 6:
                ejecutar_top_paises()
            elif opcion == 7:
                ejecutar_estadisticas_generales()
            elif opcion == 8:
                ejecutar_estadisticas_continente()
            elif opcion == 9:
                ejecutar_busqueda_avanzada()
            elif opcion == 10:
                ejecutar_mostrar_todos()
            elif opcion == 11:
                ejecutar_exportar_resultados()
            else:
                print("❌ Opción inválida. Por favor, seleccione una opción del menú.")
                pausar_ejecucion()
                
        except ValueError:
            print("❌ Debe ingresar un número válido.")
            pausar_ejecucion()
        except KeyboardInterrupt:
            print("\n\n👋 Aplicación interrumpida por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            pausar_ejecucion()


def main():
    """Función principal del programa."""
    try:
        print("🌍 SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
        print("=" * 60)
        print("Trabajo Práctico Integrador (TPI) - Programación I")
        print("Universidad Tecnológica Nacional (UTN)")
        print("Integrantes: Precelle, Martín Nicolás y García Vargas, Marcos")
        print("=" * 60)
        
        # Inicializar datos
        if not inicializar_datos():
            print("❌ No se pudo inicializar el sistema. Verifique que el archivo de datos existe.")
            return
        
        # Ejecutar menú principal
        ejecutar_menu_principal()
        
    except Exception as e:
        print(f"❌ Error crítico en la aplicación: {e}")
        print("🔧 Por favor, contacte a los desarrolladores o revise la configuración del sistema.")
    finally:
        print("\n🏁 Aplicación finalizada.")


if __name__ == "__main__":
    main()
# 🌍 Sistema de Gestión de Datos de Países

**Trabajo Práctico Integrador (TPI) - Programación I**  
**Universidad Tecnológica Nacional (UTN)**

## 👥 Integrantes, Profesores y Tutores

### Integrantes
- **Precelle, Martín Nicolás**
- **García Vargas, Marcos**

### Profesores
- **Cintia Torres**
- **Ariel Enferrel**

### Tutores
- **Matias Torres**
- **Luciano Chiroli**

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema completo de gestión de datos de países desarrollado en Python 3.11.9. El sistema permite cargar información desde archivos CSV, realizar consultas avanzadas, aplicar filtros, ordenamientos y generar estadísticas descriptivas sobre datos demográficos y geográficos de países.

## 🎯 Objetivos

- Afianzar el uso de estructuras de datos (listas y diccionarios)
- Implementar modularización con funciones
- Aplicar técnicas de filtrado y ordenamiento
- Desarrollar validaciones robustas y manejo de errores
- Crear una interfaz de usuario intuitiva en consola

## 🏗️ Arquitectura del Sistema

### Módulos Principales

1. **`main.py`** - Aplicación principal con funciones
2. **`carga_datos.py`** - Carga y validación de datos CSV
3. **`validacion.py`** - Validación de entradas del usuario
4. **`consultas.py`** - Búsquedas y filtros de países
5. **`ordenamiento.py`** - Algoritmos de ordenamiento implementados
6. **`estadisticas.py`** - Cálculo de estadísticas descriptivas
7. **`presentacion.py`** - Formateo y visualización de datos

### Estructura de Datos

Cada país se representa como un diccionario con los siguientes campos:
```python
{
    'nombre': 'Argentina',
    'poblacion': 45376763,
    'superficie': 2780400,
    'continente': 'América',
    'densidad': 16.32  # Calculada automáticamente
}
```

## 🚀 Instalación y Uso

### Requisitos
- Python 3.6 o superior
- No se requieren librerías externas

### Instalación
1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd tpi-precelle-vargas/app
```

2. Ejecutar la aplicación:
```bash
python main.py
```

### Estructura de Archivos
```
app/
├── main.py                 # Aplicación principal
├── data/
│   └── paises.csv          # Dataset de países (175 países)
└── modulos/
    ├── __init__.py
    ├── carga_datos.py      # Carga de datos CSV
    ├── validacion.py       # Validaciones de entrada
    ├── consultas.py        # Búsquedas y filtros
    ├── ordenamiento.py     # Algoritmos de ordenamiento
    ├── estadisticas.py     # Cálculos estadísticos
    └── presentacion.py     # Formateo y visualización
```

## 🔧 Funcionalidades

### 1. Búsqueda y Filtrado
- ✅ Búsqueda de países por nombre (coincidencia parcial)
- ✅ Filtrado por continente
- ✅ Filtrado por rango de población
- ✅ Filtrado por rango de superficie
- ✅ Búsqueda avanzada con múltiples criterios

### 2. Ordenamiento
- ✅ Ordenamiento por nombre (A-Z, Z-A)
- ✅ Ordenamiento por población (ascendente/descendente)
- ✅ Ordenamiento por superficie (ascendente/descendente)
- ✅ Ordenamiento por densidad poblacional (ascendente/descendente)

### 3. Estadísticas
- ✅ Estadísticas generales (totales, promedios, extremos)
- ✅ Estadísticas por continente
- ✅ Correlación entre población y superficie

### 4. Visualización
- ✅ Lista formateada de países
- ✅ Top países por diferentes criterios
- ✅ Reportes estadísticos detallados
- ✅ Exportación a archivos (TXT, CSV)

## 📊 Dataset

El archivo `data/paises.csv` contiene información de **175 países** con los siguientes campos:
- **nombre**: Nombre del país
- **poblacion**: Población total en habitantes
- **superficie**: Superficie en km²
- **continente**: Continente al que pertenece

### Ejemplo de datos:
```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
```

## 🎮 Uso del Sistema

### Menú Principal
```
🌍 SISTEMA DE GESTIÓN DE DATOS DE PAÍSES
============================================================
1. 🔍 Buscar país por nombre
2. 🌎 Filtrar países por continente
3. 📊 Filtrar países por rango de población
4. 📏 Filtrar países por rango de superficie
5. 📈 Ordenar países por criterio
6. 🏆 Mostrar top países
7. 📊 Mostrar estadísticas generales
8. 🌍 Mostrar estadísticas por continente
9. 🔎 Búsqueda avanzada (múltiples criterios)
10. 📋 Mostrar todos los países
11. 💾 Exportar resultados a archivo
0. 🚪 Salir
```

### Ejemplos de Uso

#### Búsqueda por Nombre
```
Ingrese el nombre del país: argentina
✅ Búsqueda exitosa: Países que contienen 'argentina'
📊 Se encontraron 1 países
```

#### Filtrado por Continente
```
🌍 CONTINENTES DISPONIBLES:
 1. África
 2. América
 3. Asia
 4. Europa
 5. Oceanía

Seleccione un continente (1-5): 2
✅ Búsqueda exitosa: Países de América
```

#### Estadísticas Generales
```
📊 ESTADÍSTICAS GENERALES
============================================================
📈 Total de países: 175
👥 Población mundial: 7,794,798,739 habitantes
📏 Superficie mundial: 149,430,000 km²
🏘️  Densidad promedio: 52.15 hab/km²
```

## 📝 Ejemplos de Salida

### Lista de Países
```
📋 Países ordenados por población (descendente) (10 países)
--------------------------------------------------
 1. 🌍 China
    📍 Continente: Asia
    👥 Población: 1,439,323,776 habitantes
    📏 Superficie: 9,596,961 km²
    🏘️  Densidad: 149.97 hab/km²
```

### Estadísticas por Continente
```
🌍 ESTADÍSTICAS DE ASIA
==================================================
📈 Total de países: 48
👥 Población total: 4,641,054,775 habitantes
📏 Superficie total: 44,579,000 km²
🏘️  Densidad promedio: 104.11 hab/km²
```

## 🎯 Cumplimiento de Consignas TPI

### ✅ Requerimientos Mínimos Cumplidos
1. **Búsqueda por nombre** - Implementada con coincidencia parcial
2. **Filtrado por continente** - Lista interactiva de continentes
3. **Filtrado por rango de población** - Validación de rangos
4. **Filtrado por rango de superficie** - Validación de rangos
5. **Ordenamiento** - Por nombre, población, superficie (ascendente/descendente)
6. **Estadísticas básicas** - Países extremos, promedios, totales
7. **Validaciones** - Manejo robusto de errores
8. **Archivos CSV** - Carga y procesamiento correcto

### ✅ Estructuras de Datos Utilizadas
- **Listas**: Para almacenar países y resultados
- **Diccionarios**: Para representar cada país
- **Funciones**: Modularización completa del código
- **Condicionales**: Validaciones y flujo de control
- **Bucles**: Procesamiento de datos y algoritmos de ordenamiento

---
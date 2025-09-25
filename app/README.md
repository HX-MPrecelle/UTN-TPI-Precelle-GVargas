# 🌍 Sistema de Gestión de Datos de Países

**Trabajo Práctico Integrador (TPI) - Programación I**  
**Universidad Tecnológica Nacional (UTN)**

## 👥 Integrantes
- **Precelle, Martín Nicolás**
- **García Vargas, Marcos**

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

1. **`carga_datos.py`** - Carga y validación de datos CSV
2. **`validacion.py`** - Validación de entradas del usuario
3. **`consultas.py`** - Búsquedas y filtros de países
4. **`ordenamiento.py`** - Algoritmos de ordenamiento implementados
5. **`estadisticas.py`** - Cálculo de estadísticas descriptivas
6. **`presentacion.py`** - Formateo y visualización de datos
7. **`main.py`** - Aplicación principal y menú de usuario

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
cd tpi-precelle-vargas
```

2. Ejecutar la aplicación:
```bash
python app/main.py
```

### Estructura de Archivos
```
tpi-precelle-vargas/
├── app/
│   ├── main.py                 # Aplicación principal
│   ├── modulos/
│   │   ├── __init__.py
│   │   ├── carga_datos.py      # Carga de datos CSV
│   │   ├── validacion.py       # Validaciones
│   │   ├── consultas.py        # Búsquedas y filtros
│   │   ├── ordenamiento.py     # Algoritmos de ordenamiento
│   │   ├── estadisticas.py     # Cálculos estadísticos
│   │   └── presentacion.py     # Formateo y visualización
├── data/
│   └── paises.csv              # Dataset de países
├── README.md
└── flujo_operaciones.md
```

## 🔧 Funcionalidades

### 1. Búsqueda y Filtrado
- ✅ Búsqueda de países por nombre (coincidencia exacta o parcial)
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
- ✅ Análisis de distribución poblacional
- ✅ Correlación entre población y superficie

### 4. Visualización
- ✅ Lista formateada de países
- ✅ Top países por diferentes criterios
- ✅ Reportes estadísticos detallados
- ✅ Exportación a archivos (TXT, CSV)

## 📊 Dataset

El archivo `data/paises.csv` contiene información de más de 180 países con los siguientes campos:
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
✅ Búsqueda exitosa: países que contienen 'argentina'
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

Ingrese el nombre del continente: america
✅ Búsqueda exitosa: países de América
```

#### Estadísticas Generales
```
📊 ESTADÍSTICAS GENERALES
============================================================
📈 Total de países: 185
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

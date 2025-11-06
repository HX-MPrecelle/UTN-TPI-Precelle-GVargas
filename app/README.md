# 🌍 Sistema de Gestión de Datos de Países

**Trabajo Práctico Integrador (TPI) - Programación I**  
**Tecnicatura Universitaria en Programación a Distancia**  
**Universidad Tecnológica Nacional (UTN)**

## 👥 Participación de los Integrantes

### Integrantes del Proyecto
- **Precelle, Martín Nicolás**
- **García Vargas, Marcos**

### Profesores
- **Cintia Torres**
- **Ariel Enferrel**

### Tutores
- **Matias Torres**
- **Luciano Chiroli**

---

## 📋 Descripción del Programa

Este proyecto implementa un sistema completo de gestión de datos de países desarrollado en Python 3.11.9 El sistema permite:

- **Cargar datos** desde archivos CSV con información de países
- **Agregar nuevos países** a la base de datos
- **Actualizar datos** de países existentes (población y superficie)
- **Buscar países** por nombre (coincidencia parcial o exacta)
- **Filtrar países** por continente, rango de población o rango de superficie
- **Ordenar países** por diferentes criterios (nombre, población, superficie)
- **Calcular estadísticas** generales y por continente
- **Validar entradas** del usuario y manejar errores de forma robusta

El sistema está completamente modularizado, utilizando listas y diccionarios como estructuras de datos principales, y aplica algoritmos de ordenamiento implementados desde cero.

---

## 🚀 Instrucciones de Uso

### Requisitos del Sistema
- **Python 3.6 o superior**
- **No se requieren librerías externas** (solo módulos estándar de Python)

### Instalación

1. **Clonar o descargar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd tpi-precelle-vargas/app
   ```

2. **Verificar que el archivo CSV existe:**
   ```
   app/data/paises.csv
   ```

### Ejecución del Programa

1. **Abrir una terminal** en la carpeta `app`

2. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

3. **El programa mostrará:**
   - Mensaje de bienvenida
   - Carga de datos desde el CSV
   - Menú principal con opciones disponibles

### Estructura de Archivos

```
app/
├── main.py                 # Aplicación principal
├── data/
│   └── paises.csv          # Dataset de países (175 países)
└── modulos/
    ├── __init__.py         # Inicialización del paquete
    ├── carga_datos.py      # Carga y validación de datos CSV
    ├── validacion.py       # Validaciones de entrada del usuario
    ├── consultas.py        # Búsquedas y filtros de países
    ├── ordenamiento.py     # Algoritmos de ordenamiento
    ├── estadisticas.py     # Cálculos estadísticos
    └── presentacion.py     # Formateo y visualización
```

---

## 🎮 Menú Principal

Al ejecutar el programa, se mostrará el siguiente menú:

```
🌍 SISTEMA DE GESTIÓN DE DATOS DE PAÍSES
============================================================
1. ➕ Agregar un país
2. ✏️  Actualizar datos de un país
3. 🔍 Buscar país por nombre
4. 🌎 Filtrar países por continente
5. 📊 Filtrar países por rango de población
6. 📏 Filtrar países por rango de superficie
7. 📈 Ordenar países por criterio
8. 📊 Mostrar estadísticas generales
9. 🌍 Mostrar estadísticas por continente
0. 🚪 Salir
============================================================
```

---

## 📝 Ejemplos de Entradas y Salidas

### Ejemplo 1: Agregar un País

**Entrada:**
```
Seleccione una opción: 1

Ingrese el nombre del país: Mónaco
Ingrese la población: 39244
Ingrese la superficie (km²): 2

🌍 CONTINENTES DISPONIBLES:
 1. África
 2. América
 3. Asia
 4. Europa
 5. Oceanía
 6. Ingresar nuevo continente

Seleccione un continente (1-6): 4
```

**Salida:**
```
✅ País 'Mónaco' agregado exitosamente

🌍 Mónaco
   📍 Continente: Europa
   👥 Población: 39.244 habitantes
   📏 Superficie: 2 km²
```

---

### Ejemplo 2: Actualizar Datos de un País

**Entrada:**
```
Seleccione una opción: 2

Ingrese el nombre del país a actualizar: Argentina

📋 Datos actuales del país:
🌍 Argentina
   📍 Continente: América
   👥 Población: 45.376.763 habitantes
   📏 Superficie: 2.780.400 km²

Ingrese los nuevos valores (presione Enter para mantener el valor actual):
Población actual: 45376763 → Nueva población: 46000000
Superficie actual: 2780400 → Nueva superficie (km²): [Enter]
```

**Salida:**
```
✅ País 'Argentina' actualizado exitosamente

📋 Datos actualizados:
🌍 Argentina
   📍 Continente: América
   👥 Población: 46.000.000 habitantes
   📏 Superficie: 2.780.400 km²
```

---

### Ejemplo 3: Buscar País por Nombre

**Entrada:**
```
Seleccione una opción: 3

Ingrese el nombre del país a buscar: arg
```

**Salida:**
```
🔍 BÚSQUEDA POR NOMBRE
------------------------------

✅ Búsqueda exitosa: Países que contienen 'arg'
📊 Se encontraron 1 países

📋 Resultados de: Países que contienen 'arg' (1 países)
--------------------------------------------------

 1. 🌍 Argentina
    📍 Continente: América
    👥 Población: 45.376.763 habitantes
    📏 Superficie: 2.780.400 km²
```

---

### Ejemplo 4: Filtrar por Continente

**Entrada:**
```
Seleccione una opción: 4

🌍 CONTINENTES DISPONIBLES:
------------------------------
 1. África
 2. América
 3. Asia
 4. Europa
 5. Oceanía

Seleccione un continente (1-5): 2
```

**Salida:**
```
✅ Búsqueda exitosa: Países de América
📊 Se encontraron 35 países

📋 Resultados de: Países de América (10 países)
--------------------------------------------------

 1. 🌍 Argentina
    📍 Continente: América
    👥 Población: 45.376.763 habitantes
    📏 Superficie: 2.780.400 km²

 2. 🌍 Brasil
    📍 Continente: América
    👥 Población: 213.993.437 habitantes
    📏 Superficie: 8.515.767 km²

... (mostrando primeros 10 de 35)
```

---

### Ejemplo 5: Filtrar por Rango de Población

**Entrada:**
```
Seleccione una opción: 5

Ingrese población mínima: 100000000
Ingrese población máxima: 200000000
```

**Salida:**
```
✅ Búsqueda exitosa: Países con población entre 100,000,000 y 200,000,000 habitantes
📊 Se encontraron 3 países

📋 Resultados de: Países con población entre 100,000,000 y 200,000,000 habitantes (3 países)
--------------------------------------------------

 1. 🌍 Bangladesh
    📍 Continente: Asia
    👥 Población: 164.689.383 habitantes
    📏 Superficie: 147.570 km²

 2. 🌍 Rusia
    📍 Continente: Europa
    👥 Población: 145.934.462 habitantes
    📏 Superficie: 17.098.242 km²

 3. 🌍 México
    📍 Continente: América
    👥 Población: 128.932.753 habitantes
    📏 Superficie: 1.964.375 km²
```

---

### Ejemplo 6: Ordenar Países

**Entrada:**
```
Seleccione una opción: 7

📈 ORDENAR PAÍSES POR:
1. Nombre (A-Z)
2. Nombre (Z-A)
3. Población (Mayor a menor)
4. Población (Menor a mayor)
5. Superficie (Mayor a menor)
6. Superficie (Menor a mayor)
0. Volver al menú principal

Seleccione una opción: 3
```

**Salida:**
```
📋 Países ordenados por poblacion (mayor a menor) (20 países)
--------------------------------------------------

 1. 🌍 China
    📍 Continente: Asia
    👥 Población: 1.439.323.776 habitantes
    📏 Superficie: 9.596.961 km²

 2. 🌍 India
    📍 Continente: Asia
    👥 Población: 1.380.004.385 habitantes
    📏 Superficie: 3.287.263 km²

... (mostrando primeros 20)
```

---

### Ejemplo 7: Estadísticas Generales

**Entrada:**
```
Seleccione una opción: 8
```

**Salida:**
```
📊 ESTADÍSTICAS GENERALES
============================================================
📈 Total de países: 175
👥 Población mundial: 7.794.798.739 habitantes
📏 Superficie mundial: 149.430.000 km²

📊 Población promedio: 44.541.707 habitantes
📊 Superficie promedio: 854.457 km²

🏆 EXTREMOS:
   Mayor población: China (1.439.323.776 hab)
   Menor población: Vaticano (825 hab)
   Mayor superficie: Rusia (17.098.242 km²)
   Menor superficie: Vaticano (0 km²)
```

---

### Ejemplo 8: Estadísticas por Continente

**Entrada:**
```
Seleccione una opción: 9

🌍 CONTINENTES DISPONIBLES:
------------------------------
 1. África
 2. América
 3. Asia
 4. Europa
 5. Oceanía

Seleccione un continente (1-5): 3
```

**Salida:**
```
🌍 ESTADÍSTICAS DE ASIA
==================================================
📈 Total de países: 48
👥 Población total: 4.641.054.775 habitantes
📏 Superficie total: 44.579.000 km²

🏆 EXTREMOS EN ASIA:
   Mayor población: China (1.439.323.776 hab)
   Menor población: Maldivas (540.544 hab)
```

---

### Ejemplo 9: Error - País No Encontrado

**Entrada:**
```
Seleccione una opción: 2

Ingrese el nombre del país a actualizar: PaísInexistente
```

**Salida:**
```
❌ No se encontró el país 'PaísInexistente'
```

---

### Ejemplo 10: Error - País Ya Existe

**Entrada:**
```
Seleccione una opción: 1

Ingrese el nombre del país: Argentina
```

**Salida:**
```
❌ El país 'Argentina' ya existe en la base de datos
```

---

## 📊 Dataset

El archivo `data/paises.csv` contiene información de **175 países** con los siguientes campos:

- **nombre**: Nombre del país (string)
- **poblacion**: Población total en habitantes (entero)
- **superficie**: Superficie en km² (entero)
- **continente**: Continente al que pertenece (string)

### Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

---

## 🏗️ Arquitectura del Sistema

### Módulos Principales

1. **`main.py`** - Aplicación principal que coordina todos los módulos
2. **`carga_datos.py`** - Carga y validación de datos desde CSV
3. **`validacion.py`** - Validación de entradas del usuario
4. **`consultas.py`** - Búsquedas y filtros de países
5. **`ordenamiento.py`** - Algoritmos de ordenamiento implementados
6. **`estadisticas.py`** - Cálculo de estadísticas descriptivas
7. **`presentacion.py`** - Formateo y visualización de datos

### Estructura de Datos

Cada país se representa como un diccionario:

```python
{
    'nombre': 'Argentina',
    'poblacion': 45376763,
    'superficie': 2780400,
    'continente': 'América'
}
```

Los países se almacenan en una **lista de diccionarios**:

```python
paises = [
    {'nombre': 'Argentina', 'poblacion': 45376763, ...},
    {'nombre': 'Brasil', 'poblacion': 213993437, ...},
    # ... más países
]
```

---

## 🔧 Funcionalidades Implementadas

### 1. Gestión de Países
- ✅ **Agregar un país** - Con validación de campos obligatorios
- ✅ **Actualizar datos de un país** - Población y superficie

### 2. Búsqueda y Filtrado
- ✅ **Búsqueda por nombre** - Coincidencia parcial o exacta
- ✅ **Filtrado por continente** - Lista interactiva
- ✅ **Filtrado por rango de población** - Con validación de rangos
- ✅ **Filtrado por rango de superficie** - Con validación de rangos

### 3. Ordenamiento
- ✅ **Ordenamiento por nombre** (A-Z, Z-A) - Algoritmo de selección
- ✅ **Ordenamiento por población** (ascendente/descendente) - Burbuja optimizado
- ✅ **Ordenamiento por superficie** (ascendente/descendente) - Por inserción

### 4. Estadísticas
- ✅ **Estadísticas generales** - Totales, promedios, extremos
- ✅ **Estadísticas por continente** - Análisis por región

### 5. Validaciones
- ✅ **Validación de entradas** - Números, rangos, campos obligatorios
- ✅ **Manejo de errores** - Mensajes claros y descriptivos
- ✅ **Validación de CSV** - Formato y campos requeridos

---

**Desarrollado por:** Precelle, Martín Nicolás y García Vargas, Marcos  
**Universidad Tecnológica Nacional (UTN)**  
**Programación I - Trabajo Práctico Integrador**

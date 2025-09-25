# 📚 Documentación Técnica - Sistema de Gestión de Datos de Países

## 🎯 Marco Teórico

### Conceptos Aplicados

#### 1. Listas
Las **listas** son estructuras de datos secuenciales que permiten almacenar colecciones ordenadas de elementos. En este proyecto se utilizan para:

- **Almacenamiento de países**: `paises = []` contiene todos los países cargados desde el CSV
- **Resultados de búsqueda**: Las funciones de consulta retornan listas de países que cumplen criterios
- **Ordenamiento**: Los algoritmos trabajan sobre listas y retornan nuevas listas ordenadas
- **Iteración**: Uso de `for` para recorrer países y realizar operaciones

```python
# Ejemplo de uso de listas
paises = cargar_datos_csv('data/paises.csv')
for pais in paises:
    print(f"País: {pais['nombre']}")
```

#### 2. Diccionarios
Los **diccionarios** son estructuras de datos que almacenan pares clave-valor. Cada país se representa como un diccionario:

```python
pais = {
    'nombre': 'Argentina',
    'poblacion': 45376763,
    'superficie': 2780400,
    'continente': 'América',
    'densidad': 16.32
}
```

**Ventajas de los diccionarios:**
- Acceso eficiente por clave: `pais['nombre']`
- Estructura semántica clara
- Facilita la manipulación de datos complejos

#### 3. Funciones
El código está **modularizado** en funciones que cumplen el principio de responsabilidad única:

```python
def buscar_pais_por_nombre(paises, nombre, busqueda_exacta=False):
    """
    Busca países por nombre (coincidencia exacta o parcial).
    
    Args:
        paises: Lista de países
        nombre: Nombre a buscar
        busqueda_exacta: Si debe ser búsqueda exacta
    
    Returns:
        Lista de países que coinciden
    """
    # Implementación...
```

**Beneficios:**
- **Reutilización**: Una función puede ser llamada múltiples veces
- **Mantenimiento**: Cambios en una función no afectan otras
- **Legibilidad**: Código más fácil de entender
- **Testing**: Cada función puede probarse independientemente

#### 4. Estructuras Condicionales
Se utilizan **if-elif-else** para controlar el flujo del programa:

```python
if opcion == '1':
    self.buscar_pais_por_nombre()
elif opcion == '2':
    self.filtrar_por_continente()
else:
    print("Opción inválida")
```

#### 5. Estructuras Repetitivas
**Bucles for y while** para iterar sobre datos:

```python
# For para iterar sobre listas
for pais in paises:
    if pais['continente'] == continente:
        resultados.append(pais)

# While para menús interactivos
while True:
    mostrar_menu()
    opcion = input("Seleccione opción: ")
    if opcion == '0':
        break
```

#### 6. Algoritmos de Ordenamiento

##### Ordenamiento por Selección
```python
def ordenar_por_nombre(paises, descendente=False):
    n = len(paises_ordenados)
    for i in range(n):
        indice_extremo = i
        for j in range(i + 1, n):
            if condicion_ordenamiento:
                indice_extremo = j
        paises_ordenados[i], paises_ordenados[indice_extremo] = \
            paises_ordenados[indice_extremo], paises_ordenados[i]
```

**Complejidad**: O(n²) - Eficiente para listas pequeñas

##### Ordenamiento Burbuja Optimizado
```python
def ordenar_por_poblacion(paises, descendente=False):
    for i in range(n):
        intercambio_realizado = False
        for j in range(0, n - i - 1):
            if debe_intercambiar:
                paises_ordenados[j], paises_ordenados[j + 1] = \
                    paises_ordenados[j + 1], paises_ordenados[j]
                intercambio_realizado = True
        if not intercambio_realizado:
            break  # Optimización: salir si no hubo intercambios
```

**Complejidad**: O(n²) en el peor caso, O(n) en el mejor caso

##### Ordenamiento por Inserción
```python
def ordenar_por_superficie(paises, descendente=False):
    for i in range(1, n):
        pais_actual = paises_ordenados[i]
        j = i - 1
        while j >= 0 and debe_mover:
            paises_ordenados[j + 1] = paises_ordenados[j]
            j -= 1
        paises_ordenados[j + 1] = pais_actual
```

**Complejidad**: O(n²) - Eficiente para listas parcialmente ordenadas

##### Quicksort
```python
def _quicksort_densidad(paises, inicio, fin, descendente):
    if inicio < fin:
        indice_pivote = _particionar_densidad(paises, inicio, fin, descendente)
        _quicksort_densidad(paises, inicio, indice_pivote - 1, descendente)
        _quicksort_densidad(paises, indice_pivote + 1, fin, descendente)
```

**Complejidad**: O(n log n) promedio, O(n²) peor caso

#### 7. Estadísticas Básicas

##### Medidas de Tendencia Central
- **Media**: `suma_datos / cantidad_datos`
- **Mediana**: Valor central en una lista ordenada

```python
def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    n = len(lista_ordenada)
    if n % 2 == 0:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        return lista_ordenada[n // 2]
```

##### Medidas de Dispersión
- **Varianza**: `sum((valor - media)²) / n`
- **Desviación Estándar**: `√varianza`

```python
varianza = sum((p - poblacion_promedio) ** 2 for p in poblaciones) / total_paises
desviacion_poblacion = math.sqrt(varianza)
```

##### Correlación de Person
```python
correlacion = covarianza / (desv_poblacion * desv_superficie)
```

#### 8. Archivos CSV
**CSV (Comma-Separated Values)** es un formato de texto plano para almacenar datos tabulares:

```python
import csv

with open('data/paises.csv', 'r', encoding='utf-8') as archivo:
    lector_csv = csv.DictReader(archivo)
    for fila in lector_csv:
        pais = {
            'nombre': fila['nombre'],
            'poblacion': int(fila['poblacion']),
            'superficie': int(fila['superficie']),
            'continente': fila['continente']
        }
```

**Ventajas del CSV:**
- Formato estándar y universal
- Fácil de leer y escribir
- Compatible con Excel y otras herramientas
- Ligero y eficiente

## 🏗️ Arquitectura del Sistema

### Patrón de Diseño: Separación de Responsabilidades

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PRESENTACIÓN  │    │    LÓGICA DE    │    │   PERSISTENCIA  │
│                 │    │   NEGOCIO       │    │                 │
│ • Menú          │◄──►│ • Consultas     │◄──►│ • CSV           │
│ • Formateo      │    │ • Ordenamiento  │    │ • Validación    │
│ • Validación    │    │ • Estadísticas  │    │ • Carga         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Flujo de Datos

1. **Carga**: `main.py` → `carga_datos.py` → `paises.csv`
2. **Procesamiento**: `consultas.py`, `ordenamiento.py`, `estadisticas.py`
3. **Validación**: `validacion.py` (entradas del usuario)
4. **Presentación**: `presentacion.py` (formateo de salida)

## 📚 Bibliografía y Referencias

1. **"Python Documentation"** - https://docs.python.org/3/
2. **Real Python** - https://realpython.com/

### Conceptos de Programación
1. **Estructuras de Datos**: Listas, diccionarios, sets
2. **Algoritmos**: Ordenamiento, búsqueda, estadísticas
3. **Programación Estructurada**: Funciones, módulos, validación
4. **Manejo de Archivos**: CSV, encoding, excepciones

---




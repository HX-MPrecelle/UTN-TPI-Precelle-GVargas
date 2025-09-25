# Flujo de Operaciones Principales - Sistema de Gestión de Países

## **DIAGRAMA DE FLUJO PRINCIPAL**

```
INICIO
    ↓
[CARGAR DATOS DESDE CSV]
    ↓
[VALIDAR Y PROCESAR DATOS]
    ↓
[MENÚ PRINCIPAL]
    ↓
┌─────────────────────────────────────────────────┐
│ 1. CONSULTAR PAÍS POR NOMBRE                    │
│ 2. MOSTRAR PAÍSES POR CONTINENTE                │
│ 3. ORDENAR PAÍSES (POBLACIÓN/SUPERFICIE)       │
│ 4. CALCULAR ESTADÍSTICAS                        │
│ 5. MOSTRAR TOP N PAÍSES                         │
│ 6. BUSCAR PAÍSES POR RANGO                      │
│ 7. EXPORTAR RESULTADOS                          │
│ 0. SALIR                                        │
└─────────────────────────────────────────────────┘
    ↓
[SELECCIÓN DE OPCIÓN]
    ↓
[EJECUTAR OPERACIÓN SELECCIONADA]
    ↓
[MOSTRAR RESULTADOS]
    ↓
[VOLVER AL MENÚ PRINCIPAL]
    ↓
FIN
```

## **MÓDULOS PRINCIPALES**

### **1. MÓDULO DE CARGA DE DATOS**
```
FUNCIÓN: cargar_datos_csv()
ENTRADA: archivo CSV
PROCESO: 
- Leer archivo CSV
- Validar formato de datos
- Convertir a lista de diccionarios
SALIDA: lista de países
```

### **2. MÓDULO DE VALIDACIÓN**
```
FUNCIÓN: validar_datos()
ENTRADA: datos crudos
PROCESO:
- Verificar campos obligatorios
- Validar tipos de datos
- Manejar errores de formato
SALIDA: datos validados o mensaje de error
```

### **3. MÓDULO DE CONSULTAS**
```
FUNCIÓN: buscar_pais_por_nombre()
FUNCIÓN: filtrar_por_continente()
FUNCIÓN: buscar_por_rango_poblacion()
PROCESO: Implementar algoritmos de búsqueda
```

### **4. MÓDULO DE ORDENAMIENTO**
```
FUNCIÓN: ordenar_por_poblacion()
FUNCIÓN: ordenar_por_superficie()
FUNCIÓN: ordenar_por_densidad()
PROCESO: Implementar algoritmos de ordenamiento
```

### **5. MÓDULO DE ESTADÍSTICAS**
```
FUNCIÓN: calcular_estadisticas_continente()
FUNCIÓN: calcular_estadisticas_generales()
FUNCIÓN: mostrar_top_paises()
PROCESO: Calcular indicadores estadísticos
```

### **6. MÓDULO DE PRESENTACIÓN**
```
FUNCIÓN: mostrar_menu()
FUNCIÓN: formatear_resultados()
FUNCIÓN: exportar_a_archivo()
PROCESO: Presentar información de manera clara
```

## **ESTRUCTURA DE DATOS PRINCIPAL**

```python
# Lista de diccionarios
paises = [
    {
        'nombre': 'Argentina',
        'poblacion': 45376763,
        'superficie': 2780400,
        'continente': 'América',
        'densidad': 16.32  # Calculada
    },
    # ... más países
]
```

## **FLUJO DETALLADO DE OPERACIONES**

### **OPERACIÓN 1: Consultar País por Nombre**
```
ENTRADA: nombre del país
PROCESO:
1. Normalizar entrada (minúsculas, sin acentos)
2. Buscar coincidencia exacta o parcial
3. Mostrar información completa del país
SALIDA: Datos del país o mensaje "No encontrado"
```

### **OPERACIÓN 2: Mostrar Países por Continente**
```
ENTRADA: nombre del continente
PROCESO:
1. Filtrar países por continente
2. Mostrar lista ordenada alfabéticamente
3. Mostrar contador de países
SALIDA: Lista de países del continente
```

### **OPERACIÓN 3: Ordenar Países**
```
ENTRADA: criterio (población/superficie/densidad)
PROCESO:
1. Aplicar algoritmo de ordenamiento
2. Mostrar ranking completo o top N
SALIDA: Lista ordenada
```

### **OPERACIÓN 4: Calcular Estadísticas**
```
PROCESO:
1. Estadísticas generales:
   - Total de países
   - Población mundial total
   - Superficie mundial total
2. Estadísticas por continente:
   - País más/menos poblado
   - País más/menos extenso
   - Densidad promedio
SALIDA: Reporte estadístico
```

### **OPERACIÓN 5: Mostrar Top N Países**
```
ENTRADA: número N y criterio
PROCESO:
1. Ordenar según criterio
2. Tomar los primeros N elementos
3. Formatear presentación
SALIDA: Top N países
```

### **OPERACIÓN 6: Buscar por Rango**
```
ENTRADA: rango de población/superficie
PROCESO:
1. Filtrar países en el rango
2. Ordenar resultados
3. Mostrar con indicadores
SALIDA: Países que cumplen criterio
```

## **MANEJO DE ERRORES**

```
ERRORES COMUNES:
- Archivo CSV no encontrado
- Formato de datos incorrecto
- Entrada de usuario inválida
- Países no encontrados

MANEJO:
- Validación de entrada
- Mensajes de error descriptivos
- Opciones de reintento
- Valores por defecto
```

## **FUNCIONES AUXILIARES**

```
- limpiar_texto(): Normalizar strings
- calcular_densidad(): Población/Superficie
- formatear_numero(): Formato legible
- confirmar_salida(): Confirmación de salida
- validar_entrada(): Validación de entrada
```

## **FLUJO DE VALIDACIÓN**

```
CADA OPERACIÓN:
1. Validar entrada del usuario
2. Verificar datos disponibles
3. Ejecutar operación
4. Validar resultados
5. Presentar o mostrar error
```

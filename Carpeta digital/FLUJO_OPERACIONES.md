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
│ 1. AGREGAR UN PAÍS                              │
│ 2. ACTUALIZAR DATOS DE UN PAÍS                  │
│ 3. BUSCAR PAÍS POR NOMBRE                       │
│ 4. FILTRAR PAÍSES POR CONTINENTE                │
│ 5. FILTRAR PAÍSES POR RANGO DE POBLACIÓN        │
│ 6. FILTRAR PAÍSES POR RANGO DE SUPERFICIE       │
│ 7. ORDENAR PAÍSES POR CRITERIO                  │
│ 8. MOSTRAR ESTADÍSTICAS GENERALES               │
│ 9. MOSTRAR ESTADÍSTICAS POR CONTINENTE          │
│ 0. SALIR                                        │
└─────────────────────────────────────────────────┘
    ↓
[SELECCIÓN DE OPCIÓN]
    ↓
[EJECUTAR OPERACIÓN SELECCIONADA]
    ↓
[VALIDAR ENTRADA DEL USUARIO]
    ↓
[PROCESAR OPERACIÓN]
    ↓
[MOSTRAR RESULTADOS]
    ↓
[PAUSAR EJECUCIÓN]
    ↓
[VOLVER AL MENÚ PRINCIPAL]
    ↓
FIN
```

## **MÓDULOS PRINCIPALES**

### **1. MÓDULO DE CARGA DE DATOS**
```
FUNCIÓN: cargar_datos_csv()
ENTRADA: archivo CSV (ruta)
PROCESO: 
- Leer archivo CSV
- Validar formato de datos
- Validar campos obligatorios (nombre, población, superficie, continente)
- Convertir a lista de diccionarios
- Verificar integridad de datos
SALIDA: lista de países (diccionarios)
```

### **2. MÓDULO DE VALIDACIÓN**
```
FUNCIÓN: validar_entrada_numero()
FUNCIÓN: normalizar_texto_busqueda()
FUNCIÓN: formatear_numero()
FUNCIÓN: pausar_ejecucion()
FUNCIÓN: mostrar_separador()
ENTRADA: datos del usuario
PROCESO:
- Verificar campos obligatorios
- Validar tipos de datos
- Validar rangos numéricos
- Normalizar texto para búsquedas
- Manejar errores de formato
SALIDA: datos validados o mensaje de error
```

### **3. MÓDULO DE CONSULTAS**
```
FUNCIÓN: buscar_pais_por_nombre()
FUNCIÓN: filtrar_por_continente()
FUNCIÓN: filtrar_por_rango_poblacion()
FUNCIÓN: filtrar_por_rango_superficie()
FUNCIÓN: obtener_continentes_disponibles()
PROCESO: Implementar algoritmos de búsqueda y filtrado
```

### **4. MÓDULO DE ORDENAMIENTO**
```
FUNCIÓN: ordenar_personalizado()
FUNCIÓN: ordenar_por_nombre() (ordenamiento por selección)
FUNCIÓN: ordenar_por_poblacion() (ordenamiento burbuja optimizado)
FUNCIÓN: ordenar_por_superficie() (ordenamiento por inserción)
PROCESO: Implementar algoritmos de ordenamiento
```

### **5. MÓDULO DE ESTADÍSTICAS**
```
FUNCIÓN: calcular_estadisticas_generales()
FUNCIÓN: calcular_estadisticas_continente()
PROCESO: Calcular indicadores estadísticos
- Total de países
- Población total y promedio
- Superficie total y promedio
- País con mayor/menor población
- País con mayor/menor superficie
```

### **6. MÓDULO DE PRESENTACIÓN**
```
FUNCIÓN: mostrar_menu_principal()
FUNCIÓN: mostrar_submenu_ordenamiento()
FUNCIÓN: mostrar_continentes_disponibles()
FUNCIÓN: mostrar_resultados_busqueda()
FUNCIÓN: mostrar_lista_paises()
FUNCIÓN: mostrar_estadisticas_generales()
FUNCIÓN: mostrar_estadisticas_continente()
FUNCIÓN: mostrar_pais()
PROCESO: Presentar información de manera clara y formateada
```

## **ESTRUCTURA DE DATOS PRINCIPAL**

```python
# Lista de diccionarios
paises = [
    {
        'nombre': 'Argentina',
        'poblacion': 45376763,
        'superficie': 2780400,
        'continente': 'América'
    },
    # ... más países
]
```

## **FLUJO DETALLADO DE OPERACIONES**

### **OPERACIÓN 1: Agregar un País**
```
ENTRADA: 
- Nombre del país (obligatorio, no vacío)
- Población (obligatorio, número entero > 0)
- Superficie (obligatorio, número entero > 0)
- Continente (obligatorio, no vacío)

PROCESO:
1. Solicitar nombre del país
2. Validar que el nombre no esté vacío
3. Verificar que el país no exista ya (búsqueda exacta)
4. Solicitar población y validar (número > 0)
5. Solicitar superficie y validar (número > 0)
6. Mostrar continentes disponibles o permitir ingresar nuevo
7. Validar que el continente no esté vacío
8. Crear diccionario con los datos del país
9. Agregar país a la lista global
10. Mostrar confirmación y datos del país agregado

SALIDA: País agregado exitosamente o mensaje de error
```

### **OPERACIÓN 2: Actualizar Datos de un País**
```
ENTRADA: 
- Nombre del país a actualizar
- Nueva población (opcional, Enter para mantener)
- Nueva superficie (opcional, Enter para mantener)

PROCESO:
1. Solicitar nombre del país a actualizar
2. Buscar país (búsqueda exacta)
3. Si no se encuentra, mostrar error
4. Mostrar datos actuales del país
5. Solicitar nueva población (opcional)
6. Si se ingresa, validar y actualizar
7. Solicitar nueva superficie (opcional)
8. Si se ingresa, validar y actualizar
9. Mostrar confirmación y datos actualizados

SALIDA: País actualizado exitosamente o mensaje de error
```

### **OPERACIÓN 3: Buscar País por Nombre**
```
ENTRADA: nombre del país (coincidencia parcial o exacta)

PROCESO:
1. Solicitar nombre del país
2. Validar que el nombre no esté vacío
3. Normalizar texto (minúsculas, sin acentos)
4. Buscar coincidencias parciales en la lista
5. Mostrar resultados encontrados
6. Si no hay resultados, mostrar mensaje

SALIDA: Lista de países encontrados o mensaje "No encontrado"
```

### **OPERACIÓN 4: Filtrar Países por Continente**
```
ENTRADA: continente seleccionado (número de opción)

PROCESO:
1. Obtener lista de continentes disponibles
2. Mostrar lista numerada de continentes
3. Solicitar selección (número)
4. Validar que la opción sea válida
5. Filtrar países por continente seleccionado
6. Mostrar resultados formateados

SALIDA: Lista de países del continente seleccionado
```

### **OPERACIÓN 5: Filtrar Países por Rango de Población**
```
ENTRADA: 
- Población mínima (número entero)
- Población máxima (número entero)

PROCESO:
1. Solicitar población mínima
2. Validar que sea un número válido (0 a 2,000,000,000)
3. Solicitar población máxima
4. Validar que sea un número válido (mínima a 2,000,000,000)
5. Validar que mínimo <= máximo
6. Filtrar países en el rango
7. Mostrar resultados formateados

SALIDA: Lista de países en el rango de población
```

### **OPERACIÓN 6: Filtrar Países por Rango de Superficie**
```
ENTRADA: 
- Superficie mínima (número entero, km²)
- Superficie máxima (número entero, km²)

PROCESO:
1. Solicitar superficie mínima
2. Validar que sea un número válido (0 a 20,000,000)
3. Solicitar superficie máxima
4. Validar que sea un número válido (mínima a 20,000,000)
5. Validar que mínimo <= máximo
6. Filtrar países en el rango
7. Mostrar resultados formateados

SALIDA: Lista de países en el rango de superficie
```

### **OPERACIÓN 7: Ordenar Países por Criterio**
```
ENTRADA: 
- Criterio de ordenamiento (opción del submenú)
- Dirección (ascendente/descendente)

PROCESO:
1. Mostrar submenú de ordenamiento:
   - Nombre (A-Z)
   - Nombre (Z-A)
   - Población (Mayor a menor)
   - Población (Menor a mayor)
   - Superficie (Mayor a menor)
   - Superficie (Menor a mayor)
2. Solicitar opción
3. Determinar qué datos ordenar (resultados actuales o todos)
4. Aplicar algoritmo de ordenamiento según criterio:
   - Nombre: Ordenamiento por selección
   - Población: Ordenamiento burbuja optimizado
   - Superficie: Ordenamiento por inserción
5. Mostrar resultados ordenados (máximo 20 países)

SALIDA: Lista ordenada de países
```

### **OPERACIÓN 8: Mostrar Estadísticas Generales**
```
ENTRADA: ninguna (usa todos los países)

PROCESO:
1. Calcular estadísticas generales:
   - Total de países
   - Población mundial total
   - Superficie mundial total
   - Población promedio
   - Superficie promedio
   - País con mayor población
   - País con menor población
   - País con mayor superficie
   - País con menor superficie
2. Mostrar estadísticas formateadas

SALIDA: Reporte estadístico general
```

### **OPERACIÓN 9: Mostrar Estadísticas por Continente**
```
ENTRADA: continente seleccionado (número de opción)

PROCESO:
1. Obtener lista de continentes disponibles
2. Mostrar lista numerada de continentes
3. Solicitar selección (número)
4. Validar que la opción sea válida
5. Filtrar países del continente
6. Calcular estadísticas del continente:
   - Total de países del continente
   - Población total del continente
   - Superficie total del continente
   - País con mayor población del continente
   - País con menor población del continente
7. Mostrar estadísticas formateadas

SALIDA: Reporte estadístico del continente
```

## **MANEJO DE ERRORES**

```
ERRORES COMUNES:
- Archivo CSV no encontrado
- Formato de datos incorrecto en CSV
- Campos vacíos en CSV
- Entrada de usuario inválida
- Países no encontrados
- País ya existe al agregar
- País no existe al actualizar
- Rangos inválidos (mínimo > máximo)
- Opciones de menú inválidas

MANEJO:
- Validación de entrada en cada operación
- Mensajes de error descriptivos y claros
- Validación de rangos numéricos
- Verificación de existencia de países
- Manejo de excepciones con try-except
- Valores por defecto cuando es apropiado
- Confirmaciones antes de operaciones críticas
```

## **FUNCIONES AUXILIARES**

```
- normalizar_texto_busqueda(): Normalizar strings para búsquedas
- formatear_numero(): Formatear números con separadores de miles
- validar_entrada_numero(): Validar y convertir entrada numérica
- pausar_ejecucion(): Pausar hasta que el usuario presione Enter
- mostrar_separador(): Mostrar separador visual
- obtener_continentes_disponibles(): Obtener lista única de continentes
```

## **FLUJO DE VALIDACIÓN**

```
CADA OPERACIÓN:
1. Validar entrada del usuario
   - Verificar que no esté vacía
   - Verificar tipo de dato correcto
   - Verificar rangos válidos
2. Verificar datos disponibles
   - Verificar que haya países cargados
   - Verificar que exista el país (si aplica)
3. Ejecutar operación
   - Aplicar algoritmo correspondiente
   - Procesar datos
4. Validar resultados
   - Verificar que haya resultados
   - Verificar integridad de datos
5. Presentar resultados o mostrar error
   - Formatear salida
   - Mostrar mensajes claros
   - Pausar ejecución
```

## **FLUJO DE INICIALIZACIÓN**

```
1. Ejecutar main()
2. Mostrar mensaje de bienvenida
3. Llamar a inicializar_datos()
4. Cargar datos desde CSV:
   - Verificar que el archivo existe
   - Leer archivo con encoding UTF-8
   - Validar columnas requeridas
   - Procesar cada fila
   - Validar cada país
   - Agregar a lista si es válido
5. Verificar integridad de datos:
   - Verificar que haya países cargados
   - Verificar campos requeridos en cada país
   - Verificar valores numéricos válidos
6. Mostrar confirmación de carga
7. Ejecutar menú principal
```

## **CASOS ESPECIALES**

### **Agregar País - País Ya Existe**
```
1. Usuario ingresa nombre
2. Sistema busca coincidencia exacta
3. Si existe, mostrar error: "El país 'X' ya existe"
4. No agregar país
5. Volver al menú
```

### **Actualizar País - País No Existe**
```
1. Usuario ingresa nombre
2. Sistema busca coincidencia exacta
3. Si no existe, mostrar error: "No se encontró el país 'X'"
4. No actualizar
5. Volver al menú
```

### **Filtro por Rango - Rango Inválido**
```
1. Usuario ingresa mínimo y máximo
2. Sistema valida que mínimo <= máximo
3. Si mínimo > máximo, mostrar error
4. No filtrar
5. Volver al menú
```

### **Ordenamiento - Sin Datos**
```
1. Usuario selecciona ordenamiento
2. Sistema verifica si hay datos (resultados o todos)
3. Si no hay datos, mostrar error: "No hay datos para ordenar"
4. No ordenar
5. Volver al menú
```

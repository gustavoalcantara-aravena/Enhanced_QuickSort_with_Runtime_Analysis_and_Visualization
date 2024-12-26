# 📊 QuickSort Analysis and Visualization

Este repositorio contiene un script en Python que implementa y analiza el rendimiento del algoritmo **QuickSort**. Además, genera visualizaciones que te permiten entender mejor el comportamiento de este algoritmo de ordenamiento. 🚀

---

## 📋 **Características**
- ✅ **Ordenamiento Rápido (QuickSort):** Implementación optimizada con manejo de errores y tipos.
- 📈 **Análisis de Rendimiento:** Medición de tiempos de ejecución, promedio, mediana y desviación estándar.
- 🎨 **Visualización:** Gráficos interactivos para analizar el rendimiento y distribución de datos.
- 🔍 **Casos de Prueba:** Soporte para diversos tipos de datos y escenarios (listas ordenadas, aleatorias, vacías, etc.).

---

## 🛠️ **Requisitos**
Asegúrate de tener instalado:
- Python 3.8 o superior 🐍
- Las siguientes bibliotecas de Python:
  - `matplotlib`
  - `numpy`
  - `statistics`

Puedes instalarlas ejecutando:
```bash
pip install matplotlib numpy
```

---

## 🚀 **Cómo Usar**
1. Clona este repositorio en tu máquina:
   ```bash
   git clone https://github.com/gustavoalcantara-aravena/quicksort.git
   cd quicksort
   ```
2. Ejecuta el script principal:
   ```bash
   python quicksort.py
   ```
3. Observa los resultados en la terminal y las visualizaciones generadas. Los gráficos también se guardan como `quicksort_analisis.png`.

---

## 🧪 **Casos de Prueba Incluidos**
El script incluye varios escenarios para probar el algoritmo:
- 🔢 **Listas de enteros pequeños:** `[64, 34, 25, 12, 22, 11, 90]`
- 🎯 **Números decimales:** `[3.14, 2.71, 1.41, 9.81]`
- ✏️ **Cadenas de texto:** `['banana', 'manzana', 'cereza', 'durazno']`
- ⚪ **Lista vacía:** `[]`
- 🟢 **Un único elemento:** `[1]`
- 🔁 **Elementos duplicados:** `[1, 1, 1, 1]`
- 📊 **Grandes muestras aleatorias:** `random.sample(range(1000), 100)`
- 🔀 **Listas ya ordenadas o invertidas.**

---

## 📈 **Visualizaciones Generadas**
El script crea varios gráficos que te ayudan a entender el rendimiento de QuickSort:
1. **Tiempo de ejecución por caso.**
2. **Distribución de datos antes y después de ordenar.**
3. **Relación entre tamaño de datos y tiempo de ejecución.**
4. **Comparación de datos originales vs ordenados.**

---

## 🛡️ **Manejo de Errores**
- El script lanza una excepción si los elementos en la lista son de tipos mezclados.
- Otros errores se manejan de forma genérica para evitar interrupciones.

---

## 🧑‍💻 **Contribuciones**
¡Las contribuciones son bienvenidas! Si deseas mejorar el script o agregar nuevas funcionalidades:
1. Haz un fork de este repositorio.
2. Crea una rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Envía un pull request con una descripción detallada.

---

## 📜 **Licencia**
Este proyecto está licenciado bajo la [MIT License](LICENSE). Puedes usarlo y modificarlo libremente.

---

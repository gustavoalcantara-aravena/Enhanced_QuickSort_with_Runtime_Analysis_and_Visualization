# ⚡ Enhanced QuickSort with Runtime Analysis & Visualization

A refined implementation of the **QuickSort algorithm**, featuring improved partition logic, type checking, performance analysis, and detailed visualizations of runtime behavior.

---

## 🚀 Features

- ✅ Robust `QuickSort` with midpoint pivot and in-place sorting
- 🔎 **Custom exception** handling for mixed-type arrays
- 📊 **Performance profiling** (mean, median, standard deviation)
- 📈 **4-panel runtime visualization** (execution time, distribution, size vs. time, data ordering)
- 🧪 Predefined **test cases**: integers, floats, strings, empty, duplicates, sorted, reversed, large random arrays

---

## 🧠 Partition Logic

- Pivot is chosen as the middle element: `pivot = arr[(low + high) // 2]`
- Comparison is only valid between elements of the same type
- Raises `ErrorQuickSort` if heterogeneous types are detected

---

## 📉 Visualization Panels

- **Bar chart**: execution time per test case
- **Histogram**: before/after data distribution
- **Scatter plot**: input size vs. runtime
- **Line plot**: original vs. sorted data for visual comparison

Output is saved as:  
`quicksort_analisis.png`

---

## ▶️ Quick Start

```bash
python3 enhanced_quicksort.py

```
The script runs automatically and generates a visual analysis.

---

##🧪 Test Cases

Includes diverse scenarios for robustness:

- enteros_pequeños: integers

- decimales: float numbers

- textos: string sorting

- vacío: empty input

- único: single-element array

- duplicados: identical elements

- grande: large random array

- ordenado: already sorted

- invertido: reverse sorted

---

## 📦 Dependencies

Python 3.6+

matplotlib, numpy

Install with:
```bash
pip install matplotlib numpy


```

---

📄 License

MIT License

---

Author: Gustavo Alcántara, PhD Student


from typing import List, Union, Any
import time
import random
from datetime import datetime
import statistics
import matplotlib.pyplot as plt
import numpy as np

class ErrorQuickSort(Exception):
    """Excepción personalizada para errores de QuickSort"""
    pass

def particion(arr: List[Any], bajo: int, alto: int) -> int:
    """Función de partición mejorada"""
    indice_pivote = (bajo + alto) // 2
    arr[indice_pivote], arr[alto] = arr[alto], arr[indice_pivote]
    pivote = arr[alto]
    i = bajo - 1
    
    for j in range(bajo, alto):
        if type(arr[j]) == type(pivote) and arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def ordenamiento_rapido(arr: List[Any], inicio: int = 0, fin: int = None, mostrar_pasos: bool = False) -> List[Any]:
    """Implementación mejorada de QuickSort"""
    if not arr:
        return []
    
    if fin is None:
        fin = len(arr) - 1
        tipos = set(type(x) for x in arr)
        if len(tipos) > 1:
            raise ErrorQuickSort("No se permiten tipos mezclados")
    
    if inicio < fin:
        if mostrar_pasos:
            print(f"Estado actual: {arr}")
        pivote = particion(arr, inicio, fin)
        ordenamiento_rapido(arr, inicio, pivote - 1, mostrar_pasos)
        ordenamiento_rapido(arr, pivote + 1, fin, mostrar_pasos)
    
    return arr

def analisis_rendimiento(arr: List[Any], nombre: str = "Prueba", repeticiones: int = 5) -> None:
    """Análisis detallado de rendimiento"""
    print(f"\nAnálisis de {nombre}:")
    tiempos = []
    
    try:
        for _ in range(repeticiones):
            datos = arr.copy()
            inicio = time.perf_counter()
            resultado = ordenamiento_rapido(datos)
            tiempo = (time.perf_counter() - inicio) * 1000
            tiempos.append(tiempo)
        
        print(f"Entrada:    {arr}")
        print(f"Salida:     {resultado}")
        print(f"Promedio:   {statistics.mean(tiempos):.2f}ms")
        print(f"Mediana:    {statistics.median(tiempos):.2f}ms")
        print(f"Desv. Est.: {statistics.stdev(tiempos):.2f}ms")
        
    except ErrorQuickSort as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

def visualizar_resultados(casos_prueba: dict) -> None:
    """Genera visualizaciones del rendimiento de QuickSort"""
    plt.style.use('default')  # Cambiamos seaborn por default
    fig = plt.figure(figsize=(15, 10))
    
    # Gráfico 1: Tiempos de ejecución
    plt.subplot(2, 2, 1)
    nombres = []
    tiempos = []
    
    for nombre, datos in casos_prueba.items():
        if len(datos) > 0:
            inicio = time.perf_counter()
            ordenamiento_rapido(datos.copy())
            tiempo = (time.perf_counter() - inicio) * 1000
            nombres.append(nombre)
            tiempos.append(tiempo)
    
    plt.bar(range(len(nombres)), tiempos, color='skyblue')
    plt.xticks(range(len(nombres)), nombres, rotation=45)
    plt.title('Tiempo de Ejecución por Caso')
    plt.ylabel('Tiempo (ms)')
    
    # Gráfico 2: Distribución de datos
    plt.subplot(2, 2, 2)
    datos_grandes = casos_prueba['grande']
    plt.hist(datos_grandes, bins=30, color='lightgreen', alpha=0.7, label='Original')
    plt.hist(sorted(datos_grandes), bins=30, color='salmon', alpha=0.7, label='Ordenado')
    plt.title('Distribución de Datos')
    plt.legend()
    
    # Gráfico 3: Rendimiento
    plt.subplot(2, 2, 3)
    tamaños = [len(datos) for nombre, datos in casos_prueba.items() if len(datos) > 0]
    plt.scatter(tamaños, tiempos, color='purple', alpha=0.6)
    plt.title('Tamaño vs Tiempo')
    plt.xlabel('Tamaño del Array')
    plt.ylabel('Tiempo (ms)')
    
    # Gráfico 4: Comparación
    plt.subplot(2, 2, 4)
    datos_ejemplo = np.array(casos_prueba['enteros_pequeños'])
    plt.plot(datos_ejemplo, 'r-', label='Original')
    plt.plot(sorted(datos_ejemplo), 'b--', label='Ordenado')
    plt.title('Comparación Original vs Ordenado')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('quicksort_analisis.png')
    plt.show()

def ejecutar_pruebas():
    """Ejecuta las pruebas con diferentes casos"""
    casos_prueba = {
        'enteros_pequeños': [64, 34, 25, 12, 22, 11, 90],
        'decimales': [3.14, 2.71, 1.41, 9.81],
        'textos': ['banana', 'manzana', 'cereza', 'durazno'],
        'vacío': [],
        'único': [1],
        'duplicados': [1, 1, 1, 1],
        'grande': random.sample(range(1000), 100),
        'ordenado': list(range(20)),
        'invertido': list(range(20, 0, -1))
    }
    
    visualizar_resultados(casos_prueba)

if __name__ == "__main__":
    ejecutar_pruebas()
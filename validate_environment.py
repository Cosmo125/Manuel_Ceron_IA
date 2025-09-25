#!/usr/bin/env python3
"""
Script de validación del entorno para el Curso de IA de Manuel Cerón
Ejecuta este script después de instalar los requirements para verificar que todo funciona correctamente.
"""

import sys
import importlib
from typing import Dict, List, Tuple

def check_python_version() -> bool:
    """Verifica que la versión de Python sea compatible."""
    major, minor = sys.version_info[:2]
    if major == 3 and minor >= 8:
        print(f"✅ Python {major}.{minor} - Compatible")
        return True
    else:
        print(f"❌ Python {major}.{minor} - Se requiere Python 3.8 o superior")
        return False

def check_required_packages() -> Dict[str, bool]:
    """Verifica que los paquetes requeridos estén instalados."""
    required_packages = [
        # Básicos
        'numpy', 'pandas', 'matplotlib', 'seaborn', 'scipy',
        # Machine Learning
        'sklearn', 'xgboost', 'lightgbm',
        # Deep Learning
        'tensorflow', 'torch', 'torchvision',
        # NLP
        'nltk', 'spacy', 'transformers',
        # Computer Vision
        'cv2', 'PIL',
        # Visualización
        'plotly', 'jupyter',
        # Utilidades
        'tqdm', 'requests', 'bs4'
    ]
    
    results = {}
    
    for package in required_packages:
        try:
            # Casos especiales de nombres de módulos
            module_name = package
            if package == 'sklearn':
                module_name = 'sklearn'
            elif package == 'cv2':
                module_name = 'cv2'
            elif package == 'PIL':
                module_name = 'PIL'
            elif package == 'bs4':
                module_name = 'bs4'
                
            importlib.import_module(module_name)
            print(f"✅ {package}")
            results[package] = True
        except ImportError:
            print(f"❌ {package} - No instalado")
            results[package] = False
        except Exception as e:
            print(f"⚠️  {package} - Error: {str(e)}")
            results[package] = False
    
    return results

def check_optional_packages() -> Dict[str, bool]:
    """Verifica paquetes opcionales pero recomendados."""
    optional_packages = [
        'pytest', 'black', 'flake8', 'ipywidgets'
    ]
    
    results = {}
    print("\n📦 Paquetes opcionales:")
    
    for package in optional_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
            results[package] = True
        except ImportError:
            print(f"⚠️  {package} - No instalado (opcional)")
            results[package] = False
    
    return results

def test_basic_functionality():
    """Prueba funcionalidad básica de las librerías principales."""
    print("\n🧪 Probando funcionalidad básica:")
    
    try:
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        assert arr.sum() == 15
        print("✅ NumPy - Operaciones básicas funcionan")
    except Exception as e:
        print(f"❌ NumPy - Error: {e}")
    
    try:
        import pandas as pd
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        assert len(df) == 3
        print("✅ Pandas - DataFrames funcionan")
    except Exception as e:
        print(f"❌ Pandas - Error: {e}")
    
    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 2])
        plt.close(fig)
        print("✅ Matplotlib - Gráficos funcionan")
    except Exception as e:
        print(f"❌ Matplotlib - Error: {e}")
    
    try:
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        print("✅ Scikit-learn - Modelos disponibles")
    except Exception as e:
        print(f"❌ Scikit-learn - Error: {e}")

def main():
    """Función principal de validación."""
    print("🔍 Validando entorno para el Curso de IA de Manuel Cerón")
    print("=" * 60)
    
    # Verificar versión de Python
    python_ok = check_python_version()
    
    if not python_ok:
        print("\n❌ Por favor actualiza Python antes de continuar.")
        return False
    
    print("\n📚 Verificando paquetes requeridos:")
    required_results = check_required_packages()
    
    # Verificar paquetes opcionales
    optional_results = check_optional_packages()
    
    # Probar funcionalidad básica
    test_basic_functionality()
    
    # Resumen
    print("\n📊 Resumen de validación:")
    total_required = len(required_results)
    installed_required = sum(required_results.values())
    
    print(f"Paquetes requeridos: {installed_required}/{total_required}")
    
    if installed_required == total_required:
        print("🎉 ¡Perfecto! Tu entorno está listo para el curso.")
        print("\n🚀 Siguiente paso: Ve a modulos/modulo_1_introduccion_ia/ y comienza con el primer notebook.")
        return True
    else:
        missing = [pkg for pkg, installed in required_results.items() if not installed]
        print(f"\n⚠️  Faltan algunos paquetes: {', '.join(missing)}")
        print("💡 Ejecuta: pip install -r requirements.txt")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
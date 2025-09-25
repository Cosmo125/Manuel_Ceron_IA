# 🚀 Guía de Inicio - Curso de IA Manuel Cerón

## Bienvenido al Curso

¡Felicidades por unirte al curso de Inteligencia Artificial! Esta guía te ayudará a configurar tu entorno y comenzar tu viaje en el mundo de la IA.

## 📋 Lista de Verificación Pre-Curso

Antes de comenzar, asegúrate de tener:

- [ ] **Python 3.8+** instalado en tu sistema
- [ ] **Git** configurado para control de versiones
- [ ] **Jupyter Notebook** o **JupyterLab** para ejecutar notebooks
- [ ] Al menos **8GB de RAM** (recomendado 16GB)
- [ ] **10GB de espacio libre** en disco
- [ ] Conexión estable a internet

## 🛠️ Configuración del Entorno

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/Cosmo125/Manuel_Ceron_IA.git
cd Manuel_Ceron_IA
```

### Paso 2: Crear Entorno Virtual (Recomendado)

```bash
# Con venv (Python 3.8+)
python -m venv venv_ia
source venv_ia/bin/activate  # En Windows: venv_ia\Scripts\activate

# O con conda
conda create -n ia_course python=3.9
conda activate ia_course
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Verificar Instalación

```bash
python -c "import numpy, pandas, sklearn, tensorflow; print('✅ Todas las librerías instaladas correctamente')"
```

## 📚 Estructura de Aprendizaje

### Progresión Sugerida

1. **Semanas 1-3**: Módulo 1 - Introducción a la IA
2. **Semanas 4-8**: Módulo 2 - Machine Learning
3. **Semanas 9-14**: Módulo 3 - Deep Learning
4. **Semanas 15-19**: Módulo 4 - NLP
5. **Semanas 20-25**: Módulo 5 - Computer Vision
6. **Semanas 26-33**: Módulo 6 - Proyectos Prácticos

### Metodología de Estudio

1. **📖 Estudia la teoría**: Lee los notebooks de teoría
2. **💻 Practica con ejercicios**: Completa todos los ejercicios
3. **🔬 Desarrolla proyectos**: Implementa los proyectos propuestos
4. **🤝 Participa en la comunidad**: Comparte tus avances y dudas

## 📊 Sistema de Evaluación

| Componente | Peso | Descripción |
|------------|------|-------------|
| Ejercicios | 40% | Actividades prácticas por módulo |
| Proyectos | 45% | Proyectos integradores |
| Participación | 15% | Contribuciones y discusiones |

## 🔧 Herramientas Recomendadas

### Editores de Código
- **Visual Studio Code** con extensiones de Python
- **PyCharm Community Edition**
- **Jupyter Lab** para notebooks interactivos

### Plataformas en la Nube (Opcional)
- **Google Colab** - Gratis con GPUs limitadas
- **Kaggle Notebooks** - Gratis con datasets integrados
- **Azure Notebooks** - Para usuarios de Microsoft

### Herramientas de Visualización
- **Matplotlib** y **Seaborn** para gráficos estáticos
- **Plotly** para visualizaciones interactivas
- **TensorBoard** para monitoreo de modelos

## 🤝 Comunidad y Soporte

### Canales de Comunicación
- **Issues de GitHub**: Para reportar problemas o sugerencias
- **Discussions**: Para preguntas generales y discusiones
- **Email**: manuel.ceron@ejemplo.com para consultas directas

### Reglas de la Comunidad
1. **Respeto mutuo**: Mantén un ambiente inclusivo y respetuoso
2. **Ayuda activa**: Comparte conocimiento y ayuda a otros estudiantes
3. **Código limpio**: Sigue buenas prácticas de programación
4. **Cita fuentes**: Siempre da crédito a referencias externas

## 🎯 Objetivos de Aprendizaje

Al completar este curso, serás capaz de:

- ✅ Comprender los fundamentos teóricos de la IA
- ✅ Implementar algoritmos de Machine Learning desde cero
- ✅ Desarrollar redes neuronales con frameworks modernos
- ✅ Procesar y analizar texto con técnicas de NLP
- ✅ Crear sistemas de visión por computadora
- ✅ Desplegar modelos en producción
- ✅ Construir un portafolio profesional de proyectos de IA

## 📅 Cronograma Semanal Sugerido

### Tiempo de Estudio: 10-15 horas por semana

- **Lunes-Miércoles** (4-6 horas): Teoría y conceptos
- **Jueves-Viernes** (3-4 horas): Ejercicios prácticos
- **Sábado-Domingo** (3-5 horas): Proyectos y revisión

## 🆘 Resolución de Problemas Comunes

### Error: Módulo no encontrado
```bash
pip install [nombre_del_modulo]
# O si usas conda:
conda install [nombre_del_modulo]
```

### Problemas con TensorFlow/PyTorch
- Verifica compatibilidad con tu versión de Python
- Considera usar versiones CPU si no tienes GPU
- Consulta la documentación oficial para tu sistema operativo

### Jupyter Notebook no inicia
```bash
pip install jupyter
jupyter notebook --generate-config
jupyter notebook
```

## 🎉 ¡Comienza tu Viaje!

Ahora que tienes todo configurado:

1. Ve al **Módulo 1** → `modulos/modulo_1_introduccion_ia/`
2. Abre el notebook **`teoria/01_historia_ia.ipynb`**
3. ¡Comienza tu aventura en la Inteligencia Artificial!

---

**¡Éxito en tu aprendizaje!** 🚀🤖

*¿Tienes preguntas? Abre un issue en GitHub o contacta al instructor.*
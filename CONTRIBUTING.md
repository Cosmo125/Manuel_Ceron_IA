# 🤝 Guía de Contribución - Curso IA Manuel Cerón

¡Gracias por tu interés en contribuir al curso! Tu participación ayuda a mejorar la experiencia de aprendizaje para todos.

## 🎯 Formas de Contribuir

### 1. 🐛 Reportar Problemas
- Errores en el código o notebooks
- Errores tipográficos o de contenido
- Problemas de instalación o configuración
- Sugerencias de mejora

### 2. 💡 Proponer Mejoras
- Nuevos ejercicios o proyectos
- Mejores explicaciones de conceptos
- Recursos adicionales útiles
- Optimizaciones de código

### 3. 📚 Agregar Contenido
- Ejemplos adicionales
- Casos de estudio interesantes
- Datasets relevantes
- Notebooks complementarios

### 4. 🔧 Correcciones Técnicas
- Optimización de código
- Mejoras en la estructura
- Actualizaciones de dependencias
- Corrección de bugs

## 📋 Proceso de Contribución

### Paso 1: Fork y Clone
```bash
# 1. Haz fork del repositorio en GitHub
# 2. Clona tu fork
git clone https://github.com/TU_USUARIO/Manuel_Ceron_IA.git
cd Manuel_Ceron_IA

# 3. Configura el repositorio original como upstream
git remote add upstream https://github.com/Cosmo125/Manuel_Ceron_IA.git
```

### Paso 2: Crear Rama de Trabajo
```bash
# Crea una rama descriptiva para tu contribución
git checkout -b mejora/descripcion-breve
# Ejemplos:
# git checkout -b bugfix/error-modulo-2
# git checkout -b feature/nuevo-ejercicio-nlp
# git checkout -b docs/mejorar-readme-modulo-1
```

### Paso 3: Realizar Cambios
- Mantén los cambios enfocados y relacionados
- Sigue las convenciones de código del proyecto
- Añade comentarios claros cuando sea necesario
- Prueba tu código antes de hacer commit

### Paso 4: Commit y Push
```bash
# Añade tus cambios
git add .

# Commit con mensaje descriptivo
git commit -m "tipo: descripción breve

- Detalle del cambio 1
- Detalle del cambio 2
- Resolves #numero_issue (si aplica)"

# Push a tu fork
git push origin nombre-de-tu-rama
```

### Paso 5: Crear Pull Request
1. Ve a GitHub y crea un Pull Request
2. Usa la plantilla proporcionada
3. Describe claramente qué cambios realizaste
4. Menciona cualquier issue relacionado

## 📝 Plantilla de Pull Request

```markdown
## 📋 Descripción
[Describe brevemente los cambios realizados]

## 🎯 Tipo de Cambio
- [ ] 🐛 Corrección de bug
- [ ] ✨ Nueva funcionalidad
- [ ] 📚 Actualización de documentación
- [ ] 🎨 Mejora de formato/estilo
- [ ] ♻️ Refactorización de código
- [ ] 🧪 Añadir tests

## 🔍 ¿Cómo se puede probar?
[Describe los pasos para probar los cambios]

## 📸 Screenshots (si aplica)
[Añade screenshots si hay cambios visuales]

## ✅ Checklist
- [ ] Mi código sigue las convenciones del proyecto
- [ ] He realizado una auto-revisión de mi código
- [ ] He añadido comentarios en partes complejas
- [ ] Mis cambios no generan nuevos warnings
- [ ] He probado que mi contribución funciona
- [ ] He actualizado la documentación si es necesario
```

## 🎨 Convenciones de Código

### Python
```python
# Usa nombres descriptivos
def calcular_precision_modelo(y_true, y_pred):
    """
    Calcula la precisión de un modelo de clasificación.
    
    Args:
        y_true (array): Etiquetas verdaderas
        y_pred (array): Predicciones del modelo
    
    Returns:
        float: Precisión del modelo
    """
    return accuracy_score(y_true, y_pred)

# Usa type hints cuando sea posible
from typing import List, Tuple

def procesar_datos(datos: List[dict]) -> Tuple[np.ndarray, np.ndarray]:
    # Tu código aquí
    pass
```

### Notebooks
- Una celda por concepto principal
- Markdown explicativo antes del código
- Outputs visibles para facilitar revisión
- Usar `# %%` para separar secciones en scripts

### Documentación
- Usa markdown para documentos
- Incluye ejemplos prácticos
- Estructura jerárquica clara con headers
- Enlaces a recursos externos

## 📁 Estructura de Archivos

### Para nuevos ejercicios:
```
modulos/modulo_X_nombre/
├── ejercicios/
│   ├── ejercicio_N_nombre_descriptivo.ipynb
│   └── soluciones/
│       └── ejercicio_N_solucion.ipynb
```

### Para nuevos proyectos:
```
modulos/modulo_X_nombre/
├── proyectos/
│   ├── proyecto_nombre/
│   │   ├── proyecto_nombre.ipynb
│   │   ├── README.md
│   │   ├── datos/
│   │   └── utils/
```

### Para datasets:
```
modulos/modulo_X_nombre/
├── datasets/
│   ├── dataset_nombre/
│   │   ├── README.md
│   │   ├── datos.csv
│   │   └── descripcion_columnas.md
```

## 🏷️ Convenciones de Commits

Usa commits semánticos:

```
tipo(alcance): descripción breve

Descripción más detallada si es necesaria.

- Cambio específico 1
- Cambio específico 2

Closes #123, Fixes #456
```

### Tipos de commit:
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Cambios de formato (espacios, comas, etc.)
- `refactor`: Refactorización de código
- `test`: Añadir o modificar tests
- `chore`: Cambios en build, dependencias, etc.

### Ejemplos:
```bash
git commit -m "feat(modulo-1): añadir ejercicio sobre redes neuronales

- Nuevo notebook con ejercicios prácticos
- Incluye dataset de ejemplo
- Añade solución paso a paso"

git commit -m "fix(modulo-2): corregir error en función de validación cruzada

El parámetro cv estaba mal configurado causando resultados incorrectos.

Fixes #42"

git commit -m "docs(readme): actualizar instrucciones de instalación

- Clarificar requisitos de Python
- Añadir troubleshooting común
- Mejorar formato de código"
```

## 🧪 Testing

Antes de enviar tu contribución:

```bash
# Valida el entorno
python validate_environment.py

# Ejecuta notebooks principales para verificar que funcionan
jupyter nbconvert --execute --to notebook modulos/modulo_1_introduccion_ia/teoria/01_historia_ia.ipynb

# Si añades código Python, considera añadir tests
pytest tests/ -v
```

## 📖 Recursos para Contribuidores

### Documentación Técnica
- [Jupyter Notebook Best Practices](https://jupyter.org)
- [Python PEP 8 Style Guide](https://pep8.org)
- [Markdown Guide](https://www.markdownguide.org)

### Herramientas Útiles
- **Black**: Formateador automático de código Python
- **Flake8**: Linter para Python
- **nbstripout**: Limpia outputs de notebooks para Git

```bash
# Instalar herramientas de desarrollo
pip install black flake8 nbstripout

# Configurar git hooks
nbstripout --install

# Formatear código
black modulos/
```

## 🎓 Reconocimiento de Contribuidores

Las contribuciones significativas serán reconocidas:

- Mención en el README principal
- Créditos en notebooks específicos
- Badge de contributor en el perfil
- Certificado especial de reconocimiento

## ❓ ¿Necesitas Ayuda?

- 📧 **Email**: manuel.ceron@ejemplo.com
- 💬 **Discussions**: Usa GitHub Discussions para preguntas
- 🐛 **Issues**: Reporta problemas específicos
- 📚 **Wiki**: Consulta la documentación extendida

## 📄 Código de Conducta

Este proyecto adhiere al [Contributor Covenant](https://www.contributor-covenant.org/). Al participar, se espera que mantengas un ambiente respetuoso e inclusivo.

### Nuestro Compromiso
- Ser respetuoso con todos los participantes
- Aceptar críticas constructivas
- Enfocarse en lo mejor para la comunidad
- Mostrar empatía hacia otros miembros

---

¡Gracias por contribuir al curso de IA! 🚀🤖

*Tu contribución hace que este curso sea mejor para todos los estudiantes.*
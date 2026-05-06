# Cómo correr la app en local — mini-tutorial

> **Para qué:** instrucciones paso a paso para que otra persona pueda clonar el repositorio, instalar lo necesario y abrir la app de las matrices M1 y M2 en su navegador.

**Tiempo estimado:** 10 minutos en una máquina con Python ya instalado · 20 min si hay que instalar Python.

---

## 0. Requisitos previos

| Necesitas | Cómo verificar | Si no lo tienes |
|---|---|---|
| **Python 3.12** (no 3.14: tiene un bug con watchdog/streamlit) | `python --version` en terminal | Instalar desde https://www.python.org/downloads/ — marca "Add to PATH" durante el instalador en Windows |
| **Git** | `git --version` | Windows: https://git-scm.com/download/win · Mac: `brew install git` · Linux: `sudo apt install git` |
| **Conexión a internet** | — | Para clonar el repo y descargar dependencias |
| **Cuenta GitHub con acceso al repo privado** | Pedir invitación a Ana (anamamoreno@github) | Sin acceso al repo no puedes clonar |

---

## 1. Clonar el repositorio

Abre una terminal (PowerShell en Windows, Terminal en Mac/Linux) y elige una carpeta donde alojar el proyecto:

```bash
cd C:/Users/tu-usuario/   # Windows
# o
cd ~/proyectos             # Mac/Linux

git clone https://github.com/anamamoreno/Arquitectura-rural.git
cd Arquitectura-rural
```

Te pedirá usuario + token de GitHub la primera vez. Si no tienes, generar PAT en https://github.com/settings/tokens (scope `repo`).

---

## 2. Crear entorno virtual (recomendado)

Aísla las dependencias del resto de tu Python:

```bash
# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

Si Windows bloquea el script con error de "execution policy":
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Verás `(.venv)` al inicio del prompt cuando esté activo.

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto instala: `streamlit`, `pandas`, `portalocker`, `openpyxl`. Tarda ~1-2 minutos.

---

## 4. Lanzar la app

```bash
python -m streamlit run scripts/app_matriz_estandares.py --server.port 8504
```

Verás algo así:

```
You can now view your Streamlit app in your browser.
Local URL:   http://localhost:8504
Network URL: http://192.168.X.X:8504
```

El navegador se abre solo. Si no, copia `http://localhost:8504` en la barra de direcciones.

---

## 5. Navegación

En el sidebar izquierdo verás 2 páginas:

| Página | URL | Qué hace |
|---|---|---|
| **M1 · Estándares de sostenibilidad** | `/m1` | Tabla con los 191 criterios normativos. Filtros por referencia, eje, clima, subsistema, etc. Botón "abrir" para consultar la fuente original |
| **M2 · Casos de éxito** | `/m2` | 31 casos vernáculos y contemporáneos. Tarjetas con badges (tipo + clima + sistema). Sidebar con filtros propios. Validación inline (ver §6) |

---

## 6. Validar casos M2 (modo lectura+escritura)

En local, la app está en modo escritura por defecto. Para validar casos:

1. Ir a página **M2 · Casos de éxito**
2. En el sidebar, escribe tus iniciales o nombre en "¿Quién valida hoy?"
3. Filtros sidebar:
   - **Estado:** Pendientes (default)
   - **Archivo fuente:** marca/desmarca PDFs si quieres ocultar dominantes
   - **Clima/Tipo/Sistema:** opcionales para filtrar
4. Por cada caso pendiente:
   - Edita los campos: Subsistemas, Estándares M1, Cumplimiento, Género/inclusión, Fuente, URL
   - Click en `Validar` (acepta el caso) o `Descartar` (con motivo)
   - El caso queda marcado con tu nombre + fecha automáticamente

**Importante:**
- Los cambios escriben directamente al CSV (`docs/F0-Matriz_casos_exito.csv`)
- Hay un file lock (`portalocker`) para proteger contra escrituras simultáneas
- Si trabajas con otras personas en paralelo, **coordínense** (mejor un validador a la vez)

---

## 7. Detener la app

En la terminal donde corre Streamlit: **Ctrl+C**.

Para desactivar el venv:
```bash
deactivate
```

---

## 8. Volver a abrir más tarde

```bash
cd Arquitectura-rural

# Activar venv
.venv\Scripts\Activate.ps1   # Windows
# source .venv/bin/activate   # Mac/Linux

# Si hubo cambios en GitHub, actualizar:
git pull

# Lanzar
python -m streamlit run scripts/app_matriz_estandares.py --server.port 8504
```

---

## 9. Limitaciones conocidas en local

- **Botón "Abrir PDF local"** funciona solo si tienes la carpeta `FUENTES/` con los PDFs. **Esos PDFs NO están en el repo** (son ~140 MB). Si necesitas consultar el PDF, pídelo a Ana o usa el botón "abrir" en M1 que apunta a la URL pública del documento
- **Botones "abrir" en M1**: abren los documentos oficiales en una pestaña nueva del navegador. Funcionan siempre (no necesitan PDF local)
- **Python 3.14**: hay un bug conocido (`_PySemaphore_Wakeup`) que tira la app al cerrar pestañas. Usa Python **3.12** si es posible

---

## 10. Si algo falla

| Problema | Solución |
|---|---|
| `streamlit: command not found` | Usa `python -m streamlit run ...` en lugar de `streamlit run ...` |
| `ModuleNotFoundError: No module named 'streamlit'` | Activa el venv: `.venv\Scripts\Activate.ps1` y reinstala con `pip install -r requirements.txt` |
| Puerto 8504 ocupado | Usa otro puerto: `--server.port 8505` |
| Páginas en blanco / loading infinito | Cierra la pestaña, vuelve a abrir `http://localhost:8504/`. Si persiste: Ctrl+C en terminal y relanzar |
| Cambios al CSV no se ven | Espera 30 seg (cache TTL) o refresca la página |
| Error de codificación al editar CSV en Excel | Cierra Excel, edita en VSCode o relanza la app |

Para problemas no listados, revisar la consola donde corre Streamlit — mostrará el traceback completo.

---

## 11. Acceso a la versión web (sin instalar nada)

Si solo necesitas **consultar** las matrices (no validar casos), puedes usar la versión desplegada en el VPS:

🌐 **https://app.uxtic.co/artefactos/viviendarural/m1**

Esta versión es **solo lectura**: oculta los botones de validación y los inputs editables. Útil para arquitectos consultores y supervisor del contrato.

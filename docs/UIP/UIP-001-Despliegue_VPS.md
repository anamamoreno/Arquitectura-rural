# UIP — Despliegue de la app Matriz de Estándares en VPS

**Estado:** ✅ Decisiones tomadas 2026-05-02 — listo para ejecución
**Fecha:** 2026-04-30 (creado), 2026-05-02 (decidido)
**Autor:** Ana (con asistencia de Claude)

## Decisiones finales

| # | Decisión | Resolución |
|---|---|---|
| D1 | Arquitectura | **B** — ruta `/artefactos/viviendarural/` dentro de `app.uxtic.co` (estilo enjambres) |
| D2 | Subdominio | n/a (usa app.uxtic.co) |
| D3 | Puerto interno | a asignar en VPS según puertos libres en red `uxtic-git_uxtic-network` |
| D4/D9 | Acceso | **Basic auth en nginx** (audiencia: arquitectos del proyecto) |
| D5 | Repo Git | ✅ `github.com/anamamoreno/Arquitectura-rural` |
| D6 | Datos del CSV | versionados en repo |
| D7 | Logo / branding | default Streamlit por ahora |
| D8 | Validación en VPS | **A — solo lectura.** La validación se hace siempre en local; después `git push` (Ana) + `git pull` (VPS) + rebuild |
| D10 | Sincronización del CSV en producción | **git pull + docker compose up -d --build** (manual o vía script) |

---

## 1. Objetivo

Publicar la app Streamlit `scripts/app_matriz_estandares.py` en el VPS para que los arquitectos consultores y el equipo del Producto 1 puedan filtrar y consultar la matriz de estándares de sostenibilidad sin instalar nada localmente.

---

## 2. Alcance

**Incluye:**
- Dockerización de la app
- Publicación en subdominio bajo `*.uxtic.co`
- SSL gestionado por certbot
- Datos versionados en repo Git (CSV dentro del repo)
- Documentación de comandos de despliegue y actualización

**No incluye (fuera de esta UIP):**
- Edición online del CSV (sigue siendo edición manual + git)
- Integración con `auth_service` (se decide en sección 3)
- Migración a base de datos (la app sigue leyendo CSV)
- Otros productos del proyecto (F1, F2, etc.)

---

## 3. Decisiones a confirmar antes de implementar

| # | Decisión | Opciones | Recomendación |
|---|---|---|---|
| D1 | Arquitectura | A) subdominio independiente / B) ruta en `app.uxtic.co/artefactos/` / C) sin Docker | **A** — patrón portafolios, desacoplado |
| D2 | Subdominio | `matriz.uxtic.co`, `arqrural.uxtic.co`, `estandares.uxtic.co`, otro | a definir |
| D3 | Puerto interno Docker | Próximo libre (¿8084?) — verificar en VPS | a verificar |
| D4 | Acceso | Público / HTTP Basic / JWT vía auth_service | a definir según audiencia |
| D5 | Repo Git | GitHub privado bajo cuenta UxTIC / GitLab / otro | GitHub (consistente con ecosistema) |
| D6 | Datos del CSV | Versionados en repo / volumen montado / panel de edición | **versionados** (más simple, edición manual + redeploy) |
| D7 | Logo / branding | Default Streamlit / branding UxTIC | a definir |

**Bloqueadores:** D1, D2, D4, D5 deben resolverse antes de empezar implementación.

---

## 4. Arquitectura propuesta (asumiendo D1=A)

```
Internet → Nginx host VPS (80/443)
              └── matriz.uxtic.co → arqrural-matriz Docker (8084) [directo]
```

- Contenedor independiente, no entra a la red `uxtic-git_uxtic-network`
- Mismo patrón que portafolios (habitattropical, habitattierra, letiboland)
- 0 cambios en uxtic-git ni en uxtic-nginx Docker

---

## 5. Componentes a crear

### 5.1 En el repo `Proyecto-Arq_Rural`

- `Dockerfile` — Python 3.12-slim + streamlit + pandas + openpyxl + COPY del proyecto
- `docker-compose.yml` — servicio `arqrural-matriz`, puerto 8084:8501, restart unless-stopped
- `.dockerignore` — excluir `resultados/`, `*.xlsx` no usados, `.git`, etc.
- `.gitignore` — excluir resultados intermedios, archivos temporales de Excel
- `README.md` (raíz) — descripción del proyecto y cómo correrlo local/VPS
- `docs/DEPLOY_COMANDOS.md` — comandos exactos de deploy y actualización

### 5.2 En GitHub

- Repo nuevo (privado): `uxtic/arq-rural-matriz` (o nombre acordado)
- Push del estado actual del proyecto

### 5.3 En el VPS

- DNS: registro A `matriz.uxtic.co` → IP del VPS (o CNAME a `app.uxtic.co`)
- `/etc/nginx/sites-available/matriz-uxtic.conf` — proxy a `localhost:8084`
- Symlink en `sites-enabled/`
- Certbot: `certbot --nginx -d matriz.uxtic.co`
- Carpeta `/docker/arq-rural-matriz/` con clone del repo
- Backup de la nueva config nginx en `/docker/nginx-host-backup/`

---

## 6. Pasos de implementación (en orden)

### Fase 1 — Local
1. Crear `Dockerfile`, `docker-compose.yml`, `.dockerignore`, `.gitignore`
2. Probar build local: `docker compose up --build` y verificar en `localhost:8084`
3. Validar que el CSV se lee correctamente desde dentro del contenedor

### Fase 2 — Repositorio
4. `git init` (si aplica) + commit inicial
5. Crear repo en GitHub
6. Push de `main`

### Fase 3 — DNS
7. Configurar registro DNS para el subdominio elegido (D2)
8. Esperar propagación (`dig matriz.uxtic.co`)

### Fase 4 — VPS
9. SSH al VPS
10. `cd /docker && git clone <repo>`
11. `docker compose up -d --build` en la carpeta del proyecto
12. Verificar contenedor corriendo: `docker ps | grep matriz`
13. Verificar respuesta interna: `curl localhost:8084`

### Fase 5 — Nginx + SSL
14. Crear `/etc/nginx/sites-available/matriz-uxtic.conf` (con WebSocket headers para Streamlit)
15. Symlink + `nginx -t` + `systemctl reload nginx`
16. `certbot --nginx -d matriz.uxtic.co`
17. Backup de la config a `/docker/nginx-host-backup/`

### Fase 6 — Validación
18. Acceder a `https://matriz.uxtic.co` desde fuera del VPS
19. Probar todos los filtros de la app
20. Probar en móvil
21. Verificar que el CSV se ve completo

### Fase 7 — Documentación
22. Documentar comandos de actualización (git pull + docker compose up -d --build)
23. Anotar el puerto asignado en CLAUDE.md global del ecosistema UxTIC

---

## 7. Criterios de aceptación

- [ ] `https://matriz.uxtic.co` responde con HTTPS válido
- [ ] La app carga el CSV completo y todos los filtros funcionan
- [ ] El contenedor reinicia solo si el VPS se reinicia (`restart: unless-stopped`)
- [ ] Actualizar el CSV es: editar en local → commit → push → en VPS `git pull && docker compose up -d --build`
- [ ] No se rompió nada de uxtic-git, portafolios, ni otros servicios
- [ ] La nueva config nginx está respaldada en `/docker/nginx-host-backup/`

---

## 8. Plan de rollback

Si algo falla en producción:
- **App con error:** `cd /docker/arq-rural-matriz && git checkout <commit-anterior> && docker compose up -d --build`
- **Nginx mal:** `rm /etc/nginx/sites-enabled/matriz-uxtic.conf && systemctl reload nginx` (subdominio queda sin servir, el resto del VPS intacto)
- **Apagar todo el servicio:** `cd /docker/arq-rural-matriz && docker compose down`

Como es un servicio aislado en su propio subdominio, el blast radius es mínimo: nada más en el ecosistema depende de él.

---

## 9. Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Conflicto de puerto 8084 con otro servicio | Baja | Medio | Verificar puertos libres en VPS antes de fijar (`docker ps`, `ss -tlnp`) |
| WebSockets de Streamlit no funcionan tras nginx | Media | Alto | Incluir headers `Upgrade`/`Connection` en nginx — config probada en uxtic-enjambres |
| CSV crece y la imagen se infla | Baja | Bajo | Si supera 50MB, mover CSV a volumen montado |
| Acceso no controlado si D4=Público | Media | Depende del contenido | Decidir D4 conscientemente; HTTP Basic es 5 min de trabajo extra |

---

## 10. Estimación

- **Trabajo del desarrollador (Claude):** 2–3 horas si todas las decisiones están tomadas
- **Trabajo de la usuaria:** ~30 min (DNS, decisiones, validación)
- **Tiempo calendario:** medio día asumiendo propagación DNS rápida

---

## 11. Próximo paso

Resolver decisiones D1–D5 (mínimo D1, D2, D4, D5). Cuando estén, esta UIP se vuelve plan ejecutable.

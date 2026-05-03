# DEPLOY — Comandos exactos para VPS

App: `uxtic-artefacto-viviendarural` · URL: `https://app.uxtic.co/artefactos/viviendarural/`
Patrón: estilo `uxtic-enjambres` (ruta dentro de `app.uxtic.co` vía `uxtic-nginx` Docker)

---

## Pre-requisitos en el VPS

- Red Docker `uxtic-git_uxtic-network` activa (verificar con `docker network ls`)
- Stack `uxtic-git` corriendo (incluye `uxtic-nginx`)
- `git` y `docker compose` instalados
- Acceso SSH al VPS

---

## 1. Clonar el repo en el VPS

```bash
ssh usuario@vps
sudo mkdir -p /docker/arq-rural
sudo chown $USER /docker/arq-rural
cd /docker/arq-rural
git clone https://github.com/anamamoreno/Arquitectura-rural.git .
```

---

## 2. Levantar el contenedor

```bash
cd /docker/arq-rural
docker compose up -d --build
```

Verificar:

```bash
docker ps | grep uxtic-artefacto-viviendarural
docker logs uxtic-artefacto-viviendarural --tail 20
# Debe mostrar: "You can now view your Streamlit app... URL: http://0.0.0.0:8501"

# Desde otro contenedor de la misma red, probar:
docker exec uxtic-nginx wget -qO- http://uxtic-artefacto-viviendarural:8501/artefactos/viviendarural/_stcore/health
# Debe responder: ok
```

---

## 3. Configurar `uxtic-nginx` para enrutar la ruta

Editar el `nginx.conf` o `default.conf` del contenedor `uxtic-nginx` (en `uxtic-git/nginx/`).

Agregar dentro del `server` que sirve `app.uxtic.co`:

```nginx
location /artefactos/viviendarural/ {
    # Basic auth (D9)
    auth_basic "Arquitectura Rural - Acceso restringido";
    auth_basic_user_file /etc/nginx/.htpasswd_arqrural;

    # Proxy a Streamlit con WebSocket support
    proxy_pass http://uxtic-artefacto-viviendarural:8501;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

    # WebSocket (crítico para Streamlit)
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 86400;
}
```

Crear el archivo de credenciales basic auth:

```bash
# En el host VPS, generar hash (apache2-utils debe estar instalado)
sudo htpasswd -c /docker/uxtic-git/nginx/.htpasswd_arqrural ana
# Solicita password 2 veces

# Agregar más usuarios (sin -c):
sudo htpasswd /docker/uxtic-git/nginx/.htpasswd_arqrural philippe
sudo htpasswd /docker/uxtic-git/nginx/.htpasswd_arqrural arquitecto1
```

Asegurarse de que `uxtic-nginx` tenga el `.htpasswd_arqrural` montado. En `docker-compose.yml` de `uxtic-git`, el volumen del nginx debe incluirlo (típicamente ya monta `./nginx/:/etc/nginx/`).

Aplicar:

```bash
docker exec uxtic-nginx nginx -t
docker exec uxtic-nginx nginx -s reload
```

---

## 4. Probar

```bash
# Desde tu máquina (no el VPS):
curl -I -u ana:tu_password https://app.uxtic.co/artefactos/viviendarural/
# Debe responder: HTTP/2 200
```

Abrir en navegador: `https://app.uxtic.co/artefactos/viviendarural/`
- Pide usuario/contraseña → ingresar las credenciales del `.htpasswd_arqrural`
- Debería verse la app con el banner "🔒 Modo solo lectura"

---

## 5. Actualizar contenido (cuando Ana valide casos en local)

Flujo:

```bash
# En local de Ana:
git add docs/F0-Matriz_casos_exito.csv
git commit -m "Validación CAS-001 a CAS-005 (Ana, 2026-XX-XX)"
git push

# En el VPS:
cd /docker/arq-rural
git pull
docker compose up -d --build
# El --build es necesario porque el CSV está dentro de la imagen (D6)
```

Tiempo total: ~30 segundos para rebuild (la imagen es liviana).

---

## 6. Logs y debugging

```bash
docker logs uxtic-artefacto-viviendarural -f                # logs en tiempo real
docker exec uxtic-artefacto-viviendarural ls /app/docs/     # verificar que el CSV está dentro
docker exec uxtic-artefacto-viviendarural env | grep READ   # debe mostrar READ_ONLY=true
docker compose restart                       # reiniciar sin rebuild
docker compose down && docker compose up -d --build  # rebuild completo
```

---

## 7. Apagar / desinstalar

```bash
cd /docker/arq-rural
docker compose down
# Para borrar también la imagen:
docker rmi arq-rural-uxtic-artefacto-viviendarural
# Para borrar todo el repo local:
sudo rm -rf /docker/arq-rural
# Borrar el location en uxtic-nginx y reload
```

---

## Notas

- **READ_ONLY=true por defecto** en el contenedor (vía `Dockerfile`). Para correr local en modo lectura+escritura, **no** uses Docker — usa `python -m streamlit run scripts/app_matriz_estandares.py --server.port 8504` directo.
- **Los PDFs no están en el contenedor** (gitignored). En el VPS el botón "📄 Abrir PDF" no aparece, solo se muestra el nombre del archivo.
- **Las imágenes (UIP-Imagenes_M2) están diferidas** — cuando se implementen, decidir si las imágenes van dentro de la imagen Docker o vía volumen.
- **Backup de auth:** copiar `/docker/uxtic-git/nginx/.htpasswd_arqrural` a `/docker/nginx-host-backup/`.

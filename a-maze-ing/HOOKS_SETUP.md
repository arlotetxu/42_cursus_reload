# Git Hooks Configuration

Este proyecto usa **pre-commit framework** para ejecutar verificaciones automáticas antes de cada commit.

## ¿Qué sucede?

Cuando ejecutas `git commit`, el hook automáticamente:

1. ✅ Ejecuta `make lint-strict` (flake8 + mypy --strict)
2. ✅ Si pasa → Ejecuta `uv build`
3. ❌ Si falla cualquiera → **Bloquea el commit**

## Instalación (Una sola vez)

```bash
# 1. Instalar pre-commit framework
pip install pre-commit
# o si usas uv:
uv pip install pre-commit

# 2. Instalar los hooks en tu repositorio local
pre-commit install

# 3. (Opcional) Ejecutar los hooks en todos los archivos
pre-commit run --all-files
```

## Uso

Solo haz `git commit` normalmente, el hook se ejecutará automáticamente.

### Si necesitas saltarte el hook (NO recomendado):
```bash
git commit --no-verify
```

### Para ejecutar manualmente:
```bash
# Todos los archivos
make lint-strict && uv build

# O solo lint
make lint-strict

# O solo build
uv build
```

## Archivos relevantes

- `.pre-commit-config.yaml` → Configuración del framework
- `.github/hooks/pre-commit-lint-build.sh` → Script que ejecuta las verificaciones
- `Makefile` → Actualizado para reportar errores correctamente

## Troubleshooting

**Q: El hook no se ejecuta**
```bash
# Verify hooks are installed
ls -la .git/hooks/

# If not, run:
pre-commit install
```

**Q: Quiero actualizar la configuración**
Edita `.pre-commit-config.yaml` y ejecuta:
```bash
pre-commit install --install-hooks
```

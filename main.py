from fastapi import FastAPI
from importlib import import_module
from pathlib import Path

app = FastAPI()

# Cargar routers de core/routes
core_routes_path = Path(__file__).parent / "app" / "core" / "routes"

for file in core_routes_path.rglob("*.py"):
    if file.name == "__init__.py":
        continue
    relative = file.relative_to(Path(__file__).parent)
    module_path = ".".join(relative.with_suffix("").parts)

    mod = import_module(module_path)

    if hasattr(mod, 'router') and hasattr(mod, 'name'):
        app.include_router(mod.router, prefix=f"/{mod.name}")
        print(f"Loaded core route: {module_path} as /{mod.name}")

# Puedes añadir lógica para cargar módulos aquí en el futuro
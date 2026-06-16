"""
py_package_dependency_resolver

Write a function that determines a valid package installation order by
resolving dependencies. Use topological sorting to ensure dependencies are
installed below the package that required that package dependency resolver.


def py_package_dependency_resolver (packages: dict[str, list[str]]) -> list[str]:


The function should:

- Take a dictionary where the keys are package names and the values are lists
	of package names that the key package depends on.
- Return packages in the order they should be installed, with dependencies
	appearing before the packages that depend on them.
- Return an empty list if there is a circular dependency.
- Return empty list in not a valid order exist.
- Handle empty input and isolated dependency chains.
- Ignore references to packages that are not in the input dictionary.

{
    A: [],
    B: ['A'],
    C: ['A', 'B'],
}
=> ['A', 'B', 'C']

{
    "app": ["DB"],
    "DB": ["driver"],
    "driver": []
}
=> driver > DB > app

{
    "x": ["y"],
    "y": ["x"]
}
=> Circular dependency detected, x need y and y need x, so no valid order exists
=> []
"""

from collections import deque

def py_package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    # Manejar caso de entrada vacía
    if not packages:
        return []

    # 1. Inicializar estructuras
    # in_degree cuenta cuántas dependencias pendientes tiene cada paquete
    in_degree = {pkg: 0 for pkg in packages}
    # graph mapea: paquete -> [lista de paquetes que dependen de él]
    graph = {pkg: [] for pkg in packages}

    # 2. Construir el grafo y calcular las dependencias pendientes
    for pkg, deps in packages.items():
        for dep in deps:
            # Regla: Ignorar referencias a paquetes que no están en el diccionario de entrada
            if dep in packages:
                # Añadimos 'pkg' a la lista de dependientes de 'dep'
                graph[dep].append(pkg)
                # 'pkg' tiene una dependencia pendiente más
                in_degree[pkg] += 1

    # 3. Inicializar la cola con los paquetes que NO tienen dependencias pendientes
    queue = deque([pkg for pkg, degree in in_degree.items() if degree == 0])

    installed_order = []

    # 4. Procesar la cola
    while queue:
        # Tomamos un paquete que ya se puede instalar
        current_pkg = queue.popleft()
        installed_order.append(current_pkg)

        # Revisamos qué paquetes dependían del que acabamos de instalar
        for dependent in graph[current_pkg]:
            # Le restamos 1 a sus dependencias pendientes
            in_degree[dependent] -= 1
            # Si ya no le faltan dependencias, está listo para instalarse
            if in_degree[dependent] == 0:
                queue.append(dependent)

    # 5. Comprobar si hay dependencias circulares
    # Si instalamos todos los paquetes, el orden es válido
    if len(installed_order) == len(packages):
        return installed_order
    # Si instalamos menos paquetes, hay un ciclo (ej. A necesita B y B necesita A)
    else:
        return []

# === PRUEBAS ===
if __name__ == "__main__":
    # Prueba 1: Orden normal
    test1 = {
        'A': [],
        'B': ['A'],
        'C': ['A', 'B'],
    }
    print(f"Test 1: {py_package_dependency_resolver(test1)}")
    # Esperado: ['A', 'B', 'C']

    # Prueba 2: Cadenas aisladas e invertidas
    test2 = {
        "app": ["DB"],
        "DB": ["driver"],
        "driver": []
    }
    print(f"Test 2: {py_package_dependency_resolver(test2)}")
    # Esperado: ['driver', 'DB', 'app']

    # Prueba 3: Dependencia circular
    test3 = {
        "x": ["y"],
        "y": ["x"]
    }
    print(f"Test 3: {py_package_dependency_resolver(test3)}")
    # Esperado: []

    # Prueba 4: Paquetes externos ignorados
    test4 = {
        "A": ["Z"], # Z no existe en las claves
        "B": ["A"]
    }
    print(f"Test 4: {py_package_dependency_resolver(test4)}")
    # Esperado: ['A', 'B'] (asumiendo que al ignorar Z, A no tiene dependencias)

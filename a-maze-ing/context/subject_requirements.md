# Requisitos del subject — A-Maze-ing v2.1

Documento de referencia basado en el subject oficial del proyecto de 42 School.

---

## Parte obligatoria

### Resumen
<cite index="1-321,1-322">Implementar un generador de laberintos en Python que tome un archivo de configuración, genere un laberinto (posiblemente perfecto, con un único camino entre entrada y salida), y lo escriba en un archivo usando representación hexadecimal de paredes. También debe proporcionar una representación visual del laberinto y organizar el código de forma que la lógica de generación pueda reutilizarse.</cite>

### Uso
<cite index="1-323,1-324,1-325,1-326,1-327">El programa debe ejecutarse con:
```
python3 a_maze_ing.py config.txt
```
- `a_maze_ing.py` es el archivo principal. **Debe usarse este nombre.**
- `config.txt` es el único argumento. Es un archivo de texto plano que define las opciones de generación. Se puede usar un nombre de archivo diferente.</cite>

<cite index="1-328,1-329">El programa debe manejar todos los errores de forma elegante: configuración inválida, archivo no encontrado, sintaxis incorrecta, parámetros imposibles, etc. Nunca debe crashear inesperadamente y siempre debe proporcionar un mensaje de error claro al usuario.</cite>

### Formato del archivo de configuración
<cite index="1-330,1-331">El archivo de configuración debe contener un par `CLAVE=VALOR` por línea. Las líneas que empiezan con `#` son comentarios y deben ignorarse.</cite>

<cite index="1-332,1-333">Las siguientes claves son **obligatorias**:

| Clave | Descripción | Ejemplo |
|-------|-------------|---------|
| `WIDTH` | Ancho del laberinto (número de celdas) | `WIDTH=20` |
| `HEIGHT` | Alto del laberinto | `HEIGHT=15` |
| `ENTRY` | Coordenadas de entrada (x,y) | `ENTRY=0,0` |
| `EXIT` | Coordenadas de salida (x,y) | `EXIT=19,14` |
| `OUTPUT_FILE` | Nombre del archivo de salida | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | ¿Es el laberinto perfecto? | `PERFECT=True` |</cite>

<cite index="1-334,1-335">Se pueden añadir claves adicionales (ej: seed, algorithm, display mode) si son útiles. Un archivo de configuración por defecto debe estar disponible en el repositorio Git.</cite>

### Requisitos del laberinto

<cite index="1-336">El laberinto debe generarse aleatoriamente, pero se requiere reproducibilidad mediante una semilla.</cite>

<cite index="1-337">Cada celda del laberinto tiene entre 0 y 4 paredes, en cada punto cardinal (Norte, Este, Sur, Oeste).</cite>

<cite index="1-338,1-339,1-340,1-341,1-342">El laberinto debe ser válido, lo que significa:
- Entrada y salida existen, son diferentes y están dentro de los límites del laberinto.
- La estructura garantiza conectividad total y no hay celdas aisladas (excepto el patrón '42').
- Como entrada y salida son celdas específicas, debe haber paredes en los bordes externos.
- Los datos generados deben ser coherentes: cada celda vecina debe tener la misma pared si existe alguna. Por ejemplo, está prohibido tener una primera celda con pared en el lado este y la segunda celda detrás de esa pared sin pared en el lado oeste.</cite>

<cite index="1-343,1-344,1-345">El laberinto no puede tener grandes zonas abiertas. Los pasillos no pueden tener más de 2 celdas de ancho. Por ejemplo, se puede tener una zona abierta de 2×3 o 3×2, pero nunca de 3×3.</cite>

<cite index="1-346">Cuando se representa visualmente, el laberinto debe contener un "42" visible dibujado por varias celdas completamente cerradas.</cite>

<cite index="1-347">Si el flag `PERFECT` está activado, el laberinto debe contener exactamente un camino entre la entrada y la salida (es decir, debe ser un laberinto perfecto).</cite>

<cite index="1-348,1-349,1-350">El patrón "42" puede omitirse si el tamaño del laberinto no lo permite (demasiado pequeño). En ese caso, imprimir un mensaje de error en la consola.</cite>

### Formato del archivo de salida

<cite index="1-351">El laberinto debe escribirse en el archivo de salida usando un dígito hexadecimal por celda, donde cada dígito codifica qué paredes están cerradas:

| Bit | Dirección |
|-----|-----------|
| 0 (LSB) | Norte |
| 1 | Este |
| 2 | Sur |
| 3 | Oeste |</cite>

<cite index="1-352,1-353,1-354">Una pared cerrada pone el bit a 1, abierta significa 0. Ejemplo: `3` (binario `0011`) significa que las paredes sur y oeste están abiertas. O `A` (binario `1010`) significa que las paredes este y oeste están cerradas.</cite>

<cite index="1-355,1-356,1-357">Las celdas se almacenan fila por fila, una fila por línea. Después de una línea vacía, los siguientes 3 elementos se insertan en el archivo de salida en 3 líneas: las coordenadas de entrada, las coordenadas de salida, y el camino más corto válido desde la entrada hasta la salida, usando las cuatro letras N, E, S, W. Todas las líneas terminan con `\n`.</cite>

---

## Representación visual

<cite index="1-361">El programa debe proporcionar una forma de mostrar el laberinto visualmente, usando:
- Renderizado ASCII en terminal, o
- Una pantalla gráfica usando la librería MiniLibX (MLX).</cite>

<cite index="1-362">La visualización debe mostrar claramente paredes, entrada, salida y el camino solución.</cite>

<cite index="1-363,1-364,1-365,1-366,1-367">Las interacciones de usuario deben estar disponibles, al menos para las siguientes tareas:
- Re-generar un nuevo laberinto y mostrarlo.
- Mostrar/Ocultar un camino más corto válido desde la entrada hasta la salida.
- Cambiar los colores de las paredes del laberinto.
- Opcional: establecer colores específicos para mostrar el patrón "42".

Se pueden añadir interacciones de usuario adicionales.</cite>

---

## Requisitos de reutilización de código

<cite index="1-371">Se debe implementar la generación del laberinto como una clase única (ej: `MazeGenerator`) dentro de un módulo independiente que pueda importarse en un proyecto futuro.</cite>

<cite index="1-372,1-373,1-374">Se debe proporcionar una documentación breve describiendo cómo:
- Instanciar y usar el generador, con al menos un ejemplo básico.
- Pasar parámetros personalizados (ej: tamaño, semilla).
- Acceder a la estructura generada y acceder al menos a una solución.</cite>

<cite index="1-376,1-377,1-378,1-379">Este módulo reutilizable completo (código y documentación) debe estar disponible en un único archivo adecuado para instalación posterior con pip. El paquete debe llamarse `mazegen-*` y el archivo debe estar en la raíz del repositorio git. Se permiten las extensiones `.tar.gz` y `.whl`. Ejemplo de nombre completo: `mazegen-1.0.0-py3-none-any.whl`.</cite>

<cite index="1-380,1-381">Se deben proporcionar en el repositorio Git todos los elementos necesarios para construir el paquete. Esto se pedirá durante la evaluación: en un virtualenv o equivalente, instalar las herramientas necesarias y construir el paquete de nuevo desde las fuentes.</cite>

<cite index="1-382">El archivo `README.md` principal (no parte del módulo reutilizable) también debe contener esta documentación breve.</cite>

---

## Reglas generales (Common Instructions)

<cite index="1-293,1-294">El proyecto debe estar escrito en **Python 3.10 o posterior**. El proyecto debe adherirse al estándar de codificación **flake8**.</cite>

<cite index="1-295,1-296,1-297,1-298">Las funciones deben manejar excepciones de forma elegante para evitar crashes. Usar bloques `try-except` para gestionar errores potenciales. Preferir context managers para recursos como archivos o conexiones. Si el programa crashea por excepciones no manejadas durante la revisión, se considerará no funcional.</cite>

<cite index="1-301,1-302,1-303">El código debe incluir type hints para parámetros de funciones, tipos de retorno y variables donde sea aplicable (usando el módulo `typing`). Usar `mypy` para comprobación estática de tipos. Todas las funciones deben pasar mypy sin errores.</cite>

<cite index="1-304">Incluir docstrings en funciones y clases siguiendo PEP 257 (estilo Google o NumPy) para documentar propósito, parámetros y retornos.</cite>

### Makefile obligatorio

<cite index="1-305,1-306,1-307,1-308,1-309">Incluir un Makefile con las siguientes reglas:
- `install`: Instalar dependencias del proyecto usando pip, uv, pipx u otro gestor.
- `run`: Ejecutar el script principal del proyecto.
- `debug`: Ejecutar el script principal en modo debug usando el debugger de Python (ej: pdb).
- `clean`: Eliminar archivos temporales o cachés (`__pycache__`, `.mypy_cache`).</cite>

<cite index="1-311,1-312,1-313">- `lint`: Ejecutar `flake8 .` y `mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs`
- `lint-strict` (opcional): Ejecutar `flake8 .` y `mypy . --strict`</cite>

### Directrices adicionales

<cite index="1-315,1-316">Crear programas de test para verificar la funcionalidad del proyecto (no se entregan ni se califican). Usar frameworks como pytest o unittest para tests unitarios, cubriendo casos límite.</cite>

<cite index="1-317">Incluir un archivo `.gitignore` para excluir artefactos de Python.</cite>

---

## Requisitos del README

<cite index="1-387,1-388,1-389,1-390,1-391">El `README.md` debe incluir al menos:
- La primera línea debe estar en cursiva y leer: *This project has been created as part of the 42 curriculum by \<login1\>[, \<login2\>...]*.
- Una sección "Description" que presente claramente el proyecto, incluyendo su objetivo y una visión general breve.
- Una sección "Instructions" con información relevante sobre compilación, instalación y/o ejecución.
- Una sección "Resources" listando referencias clásicas relacionadas con el tema, así como una descripción de cómo se usó la IA — especificando para qué tareas y qué partes del proyecto.</cite>

<cite index="1-394,1-395,1-396,1-397,1-398,1-400,1-401">Secciones adicionales requeridas específicamente para este proyecto:
- La estructura y formato completos del archivo de configuración.
- El algoritmo de generación de laberintos elegido.
- Por qué se eligió ese algoritmo.
- Qué parte del código es reutilizable y cómo.
- El equipo y gestión del proyecto con: roles de cada miembro, planificación anticipada y cómo evolucionó, qué funcionó bien y qué podría mejorarse, qué herramientas específicas se usaron.</cite>

---

## Bonuses

<cite index="1-405,1-406,1-407">Se pueden añadir varios bonuses al proyecto. Ejemplos posibles:
- Soporte para múltiples algoritmos de generación de laberintos.
- Añadir animación durante la generación del laberinto.</cite>

---

## Evaluación

<cite index="1-412,1-413">Durante la evaluación, puede solicitarse ocasionalmente una modificación breve del proyecto. Esto podría implicar un pequeño cambio de comportamiento, unas pocas líneas de código a escribir o reescribir, o una funcionalidad fácil de añadir.</cite>

<cite index="1-415">Este paso está destinado a verificar la comprensión real de una parte específica del proyecto.</cite>

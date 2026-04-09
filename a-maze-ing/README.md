_This project has been created as part of the 42 curriculum by joflorid, agiron-d_
# 🐍 A-Maze-ing

### 🌿 Description

**Create your own maze generator and display its result!**

A powerful and flexible maze generator and solver written in Python. Create perfect or imperfect mazes with customizable dimensions, visualize them in ASCII or with MLX graphics, and automatically solve them using pathfinding algorithms.

#### 🎯 Project Goal

The goal of **a-maze-ing** is to provide a comprehensive toolkit for procedural maze generation and visualization. Whether you're interested in maze algorithms, pathfinding solutions, or creating visual representations of complex mazes, this project delivers a complete solution with multiple generation strategies, flexible configuration options, and dual visualization modes.

#### 📖 Overview

This project combines powerful maze generation algorithms with intuitive visualization and solving capabilities:

- **Generate** perfect mazes using DFS or Prim's algorithm, or create more organic imperfect mazes
- **Configure** every aspect of your maze: dimensions, entry/exit points, output format
- **Solve** your mazes automatically using BFS pathfinding and export detailed solutions
- **Visualize** results in real-time using ASCII art or interactive MLX graphics
- **Export** maze data in a standardized format for further processing or analysis

Perfect for algorithm enthusiasts, game developers, educational purposes, and anyone curious about procedural generation techniques.


---

## ✨ Features

- 🏗️ **Multiple Maze Generation Algorithms**
  - Depth-First Search (DFS) - Default
  - Prim's Algorithm
  - Perfect and imperfect maze modes

- 🎨 **Dual Visualization Modes**
  - ASCII art renderer for terminal display
  - MLX graphics renderer for visual window display

- 🧩 **Automatic Maze Solving**
  - Breadth-First Search (BFS) pathfinding
  - Solution export with directional notation (N, S, E, W)

- ⚙️ **Highly Configurable**
  - Custom maze dimensions (width × height)
  - Configurable entry and exit points
  - Output file specification
  - Perfect/imperfect maze toggle

- 🎯 **42 Watermark Integration**
  - Optional "42" pattern watermark in maze center according to maze dimensions
  - Smart validation to prevent conflicts with entry/exit

#### Algorithm Selection

The algorithms utilized in this project were selected based on the availability of extensive documentation and their suitability for adaptation to the project requirements. The following implementations were chosen:

* **Maze Generation:** The **DFS (Depth-First Search)** and **Prim’s** algorithms were implemented due to their efficiency in creating complex structures.
* **Maze Resolution:** **BFS (Breadth-First Search)** was integrated to ensure optimal pathfinding and resolution of the generated mazes.
---

## 📋 Requirements

- **Python** 3.10 or higher (recommended 3.14)
- **uv** (recommended) or pip for package management
- **MLX library** (included in `inc/` directory)

---

## 🚀 Installation

In this section, after cloning the repository, the different options to install the project are indicated.
Using the Packaging Python Projects is highly recommended for the project instalation.
Otherwise, a different instructions are provided like using uv or pip.
After finished this instalation, follow to the next section (Instructions).
### First (Necessary)
Independendly of the instalation option selected, the clone process is mandatory.
```bash
# Clone the repository
git clone git@vogsphere.42urduliz.com:vogsphere/intra-uuid-ae58d0d1-f17c-41e7-a2d5-e7ff4894da1f-7234282-joflorid a-maze-ing
cd a-maze-ing

```

### Using Packaging Python Projects (Recommended)

```bash
# Option 1: Development mode installation (recommended for development)
pip install -e .

# Option 2: Installation from the wheel
pip install mazegen-0.1.2-py3-none-any.whl

# Option 3: Installation from source code
pip install mazegen-0.1.2.tar.gz
```

### Using uv

```bash
# Install dependencies
make install
```

### Using pip

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package
pip install -r requirements.txt
```

---

## 🎮 Instructions

### Quick Start
### Using Packaging Python Projects

```bash
# Use the command directly
a-maze-ing config.txt
```
```bash
# You can also use it as a Python module
from a_maze_ing import ft_make_maze
import sys

sys.argv = ['a_maze_ing', 'config.txt']
ft_make_maze()
```
### Using uv / pip

```bash
# 1. Run with default configuration
make run

# 2. Or use the command directly
python3 a-maze-ing config.txt
```


### Command Line

```bash
# General syntax
python3 a-maze-ing <config_file>

# Example
python3 a-maze-ing my_maze_config.txt
```

### Configuration File Format

Create a configuration file (e.g., `config.txt`) with the following parameters:

```plaintext
WIDTH=40          # Maze width in cells
HEIGHT=15         # Maze height in cells
ENTRY=0,0         # Entry point coordinates (x,y)
EXIT=5,14         # Exit point coordinates (x,y)
OUTPUT_FILE=output_maze.txt  # File to save maze seed
PERFECT=false     # true for perfect maze, false for imperfect
PRINT_MODE=mlx    # Display mode: 'ascii' or 'mlx'
```

#### Configuration Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `WIDTH` | integer | Width of the maze (minimum 9) | `40` |
| `HEIGHT` | integer | Height of the maze (minimum 7) | `15` |
| `ENTRY` | x,y | Starting coordinates | `0,0` |
| `EXIT` | x,y | Ending coordinates | `39,14` |
| `OUTPUT_FILE` | string | Path to output file | `output_maze.txt` |
| `PERFECT` | boolean | Perfect maze flag | `true` or `false` |
| `PRINT_MODE` | string | Visualization mode | `ascii` or `mlx` |
| `SEED` | string | Seed file to be reproduced | output/output_maze.txt |
| `SEED_CODE` | integer | Seed code that indentifies the maze | 1244 |

---

## 📁 Project Structure

```
a-maze-ing/
├── a_maze_ing.py              # Main entry point for the application
├── config.txt                 # Default configuration file
├── pyproject.toml             # Project metadata and dependencies
├── Makefile                   # Build and run automation
├── LICENSE                    # MIT License
├── README.md                  # This file
├── requirements.txt           # Python dependencies list
├── inc/                       # MLX graphics library (binaries)
│   └── mlx/                   # MLX library wheels and resources
├── src/                       # Main source code directory
│   ├── __init__.py
│   ├── config/                # Configuration and constants
│   │   ├── __init__.py
│   │   └── enums.py           # Color codes, walls, and enum definitions
│   ├── core/                  # Core algorithm implementations
│   │   ├── maze_generator.py  # MazeGenerator class - standalone maze generation logic
│   │   ├── solve_maze.py      # SolveMaze class - BFS maze solving algorithm
│   │   └── seed_file.py       # SeedFile class - maze seed export/management
│   ├── model/                 # Data model classes
│   │   ├── __init__.py
│   │   ├── cell.py            # Cell class - individual maze cell representation
│   │   ├── maze.py            # Maze class - maze grid container and initialization
│   │   └── seed.py            # Seed class - load mazes from seed files
│   ├── parser/                # Configuration file parsing
│   │   ├── __init__.py
│   │   ├── config_model.py    # Pydantic configuration model with validation
│   │   └── ft_parser_config.py # Config file parser and adapter
│   ├── utils/                 # Utility functions and helpers
│   │   └── utils_maze.py      # UtilsMaze class - maze utilities (navigation, watermark, open_areas)
│   └── visual/                # Visualization modules (renderers)
│       ├── __init__.py
│       ├── print_ascii.py     # MazePainter_ascii - terminal ASCII renderer with menu
│       ├── print_minilib.py   # MazePainter_mlx - MLX graphics window renderer
│       └── print_seed_ascii.py # SeedPainter_ascii - ASCII renderer for loaded seeds
├── output/                    # Generated maze output files directory
├── tests/                     # Test suite
│   ├── test_a_maze_ing.py
│   ├── test_parser_config.py
│   └── tests.py
└── .venv/                     # Python virtual environment (created during installation)
```

### Directory Descriptions

- **`src/core/`**: Reusable, standalone algorithm implementations
  - `MazeGenerator`: Class for maze generation using DFS or Prim's algorithm
  - `SolveMaze`: Class for solving mazes with BFS pathfinding
  - `SeedFile`: Class for exporting and managing maze seed files

- **`src/utils/`**: Shared utility functions for maze manipulation
  - `UtilsMaze`: Navigation, boundary checking, watermarking, and area management

- **`src/visual/`**: Rendering engines for maze visualization
  - ASCII: Terminal-based rendering with menu interaction
  - MLX: Graphical window rendering with keyboard controls
  - Seed: Read-only ASCII rendering for loaded maze seeds

---

## 🛠️ Development

### Running Tests

```bash
# Run tests with pytest
uv run pytest

# Run specific test file
uv run pytest tests/test_a_maze_ing.py
```

### Code Quality

```bash
# Type checking with mypy
make mypy

# Linting with flake8
make flake8

# Run both linters (flake8 + mypy)
make lint

# Run strict linting
make lint-strict
```

### Debugging

```bash
# Run in debug mode
make debug
```

### Cleaning Build Artifacts

```bash
# Remove cache and build files
make clean
```

---

## 📊 Output Format

The maze is exported to the specified output file in the following format:

```
MAZE_SEED_LINE_1
MAZE_SEED_LINE_2
<entry_x>,<entry_y>
<exit_x>,<exit_y>
...
SOLUTION_DIRECTIONS
```

### Maze Seed Encoding

Each cell in the maze is represented by a hexadecimal digit (0-F) where each bit represents a wall:
- **North**: 1 (0x1)
- **East**: 2 (0x2)
- **South**: 4 (0x4)
- **West**: 8 (0x8)

Example: A cell with value `C` (0xC = 12 = 0b1100) has South and West walls.

### Solution Format

The solution is a string of directional characters:
- `N` - North
- `S` - South
- `E` - East
- `W` - West

---

## 🧪 Examples

### Generate a Small Perfect Maze

```plaintext
# small_maze.txt
WIDTH=20
HEIGHT=10
ENTRY=0,0
EXIT=19,9
OUTPUT_FILE=small_output.txt
PERFECT=true
PRINT_MODE=ascii
SEED=
SEED_CODE=
```

```bash
a-maze-ing small_maze.txt
```

### Generate a Large Imperfect Maze with MLX

```plaintext
# large_maze.txt
WIDTH=60
HEIGHT=30
ENTRY=0,0
EXIT=59,29
OUTPUT_FILE=large_output.txt
PERFECT=false
PRINT_MODE=mlx
SEED=
SEED_CODE=
```

---

## 🐾 General Information
---
### Code Reusability and Structure

To ensure modularity and scalability, the codebase has been structured into several reusable components:

* **Classes:** Two primary classes were developed to facilitate project modularization and ease of use.
* **Functions:** Discrete functions were implemented to handle specific, individualized actions.
* **Methods:** These were utilized to modularize distinct behaviors within the classes.
* **Enums:** These were integrated to serve as unequivocal, centralized data references.
* **Modules:** Specific responsibilities were delegated to the following modules:
  * Parsing
  * Configuration
  * Construction
  * Representation

Consequently, a significant portion of the logic developed for the program's construction is designed to be reusable across various segments of the application.


### Project Planning and Evolution

The project was initiated with the creation of a flowchart sketch, which served as the foundation for the structural design. Based on the requirements outlined in the project subject, individual tasks were identified and managed via a **Kanban board** within the GitHub repository.



### Retrospective: Successes and Improvements

* **Communication:** Effective communication was maintained throughout the project, despite the challenges of asynchronous and remote collaboration.
* **Peer-to-Peer Learning:** A peer-to-peer methodology was applied from inception to completion, fostering a respectful and continuous learning environment.
* **Areas for Improvement:** It is noted that physical co-location of team members could have further accelerated the final delivery of the project.



### Tools Utilized

The following tools and libraries were employed during development:

* **GitHub:** Utilized for version control and project management (Kanban).
* **Pydantic:** Used for data validation.
* **Icecream:** Employed to facilitate the debugging process.
* **ipdb:** Used for advanced debugging and code inspection.
* **Pytest:** Implemented for unit testing.
* **IDEs:** Various Integrated Development Environments were used by the team.
---

## 🔎 Resources

- **[Búsqueda en amplitud en 4 minutos](https://youtu.be/HZ5YTanv5QE)**
- **[Representación de grafos](https://es.khanacademy.org/computing/computer-science/algorithms)**
- **[Grafos completo](https://youtu.be/ElRsxnYpWaQ)**
- **[https://oa.upm.es/76050/1/TFG_JOSE_ANTONIO_MARTINEZ_MARTINEZ.pdf](https://oa.upm.es/76050/1/TFG_JOSE_ANTONIO_MARTINEZ_MARTINEZ.pdf)**
- **[10 casos de uso REALES basados en tecnología de grafos](https://www.grapheverywhere.com/10-casos-de-uso-reales-basados-en-tecnologia-de-grafos/)**
- **[Algoritmo de la ruta más corta de Dijkstra - Introducción gráfica y detallada](https://www.freecodecamp.org/espanol/news/algoritmo-de-la-ruta-mas-corta-de-dijkstra-introduccion-grafica/)**
- **[Difference between Prim's and Kruskal's algorithm for MST](https://www.geeksforgeeks.org/dsa/difference-between-prims-and-kruskals-algorithm-for-mst/)**
- **IA**: We use AI to help with the project, to document ourselves and to unlock problems that arise in software development implementations when you are not very familiar with the tool and its capabilities.

---

## 👥 Authors and Team Members

- **Jose Manuel Florido Pereña** - [joflorid@student.42urduliz.com](mailto:joflorid@student.42urduliz.com)
- **Angela Patricia Girón Duque** - [agiron-d@student.42urduliz.com](mailto:agiron-d@student.42urduliz.com)

### Team Roles and Responsibilities

Although a Project Leader was designated, the workload was balanced and shared equally by both team members. The general distribution of responsibilities was organized as follows:

* **Jose Manuel Florido:**
  * Project Leadership
  * Quality Assurance (Q&A)
  * Development (Parsing & Visualization)


* **Angela Patricia Giron:**
  * General Code Quality Oversight
  * Development (Algorithm Design)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **Repository**: [git@vogsphere.42urduliz.com:vogsphere/intra-uuid-ae58d0d1-f17c-41e7-a2d5-e7ff4894da1f-7234282-joflorid](git@vogsphere.42urduliz.com:vogsphere/intra-uuid-ae58d0d1-f17c-41e7-a2d5-e7ff4894da1f-7234282-joflorid)
- **Issues**: [https://github.com/agiron-d42/a-maze-ing/issues](https://github.com/agiron-d42/a-maze-ing/issues)

---

## 🙏 Acknowledgments

Built as part of the 42 School curriculum at 42 Urduliz.

---
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
<div align="center">

Made with ❤️ by agiron_joflorid the a-maze-ing team

</div>



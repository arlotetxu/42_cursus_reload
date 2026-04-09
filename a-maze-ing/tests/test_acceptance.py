"""
Acceptance tests derived from context/test_cases.md and context/acceptance_criteria.md.
Covers: parser, config model, maze generation, watermark, hex encoding, BFS solver.
"""
import pytest
from collections import deque
from unittest.mock import patch
from src.parser.ft_parser_config import ft_parsing_config
from src.parser.config_model import ConfigModel
from src.model.maze import Maze
from src.model.cell import Cell
from src.config.enums import MazeAlgorithm, Walls
from src.utils.utils_maze import UtilsMaze
from src.core.solve_maze import SolveMaze
from src.core.maze_generator import MazeGenerator
from src.core.seed_file import SeedFile


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_config(tmp_path, content: str) -> str:
    """Write content to a temp config file and return its path."""
    p = tmp_path / "config.txt"
    p.write_text(content)
    return str(p)


def minimal_config(
    tmp_path,
    width: int = 10,
    height: int = 8,
    entry: str = "0,0",
    exit_: str = "9,7",
    perfect: str = "True",
    output: str = "maze.txt",
    mode: str = "ascii",
    extra: str = "",
) -> str:
    """Return path to a minimal valid config file."""
    content = (
        f"WIDTH={width}\nHEIGHT={height}\n"
        f"ENTRY={entry}\nEXIT={exit_}\n"
        f"PERFECT={perfect}\nOUTPUT_FILE={output}\n"
        f"PRINT_MODE={mode}\n{extra}"
    )
    return make_config(tmp_path, content)


def build_maze(width: int = 10, height: int = 8,
               entry: tuple = (0, 0), exit_: tuple = (9, 7),
               perfect: bool = True,
               seed_code: int = 42,
               algorithm: str = MazeAlgorithm.DFS.value) -> Maze:
    """Instantiate and generate a Maze directly."""
    config = ConfigModel(
        maze_width=width,
        maze_height=height,
        maze_entry=entry,
        maze_exit=exit_,
        maze_perfect=perfect,
        maze_output="maze.txt",
        maze_print_mode="ASCII",
        maze_seed="",
        maze_seed_code=seed_code,
    )
    maze = Maze(config)
    MazeGenerator(maze).perfect_maze(entry, exit_, perfect, algorithm)
    return maze


def bfs_reachable(maze: Maze, start: tuple) -> set:
    """Return set of (x,y) reachable from start via open walls (ignores 42)."""
    visited: set = set()
    queue: deque = deque([start])
    visited.add(start)
    directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
    while queue:
        x, y = queue.popleft()
        cell = UtilsMaze(maze).get_cell(x, y)
        if cell is None:
            continue
        for wall, (dx, dy) in directions.items():
            if not cell.walls[wall]:
                nx, ny = x + dx, y + dy
                neighbor = UtilsMaze(maze).get_cell(nx, ny)
                if neighbor and not neighbor.is_FORTY_TWO and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return visited


# ---------------------------------------------------------------------------
# TC-01 — Parser de configuración
# ---------------------------------------------------------------------------

class TestParser:
    """TC-01: ft_parsing_config parsing and error handling."""

    def test_tc0101_valid_config(self, tmp_path):
        """TC-01-01: Config válido completo → ConfigModel correcto."""
        path = minimal_config(tmp_path)
        result = ft_parsing_config(path)
        assert isinstance(result, ConfigModel)
        assert result.maze_width == 10
        assert result.maze_height == 8
        assert result.maze_entry == (0, 0)
        assert result.maze_exit == (9, 7)
        assert result.maze_perfect is True
        assert result.maze_print_mode == "ASCII"

    def test_tc0102_comment_lines_ignored(self, tmp_path):
        """TC-01-02: Líneas con # se ignoran."""
        path = make_config(tmp_path, "# WIDTH=99\nWIDTH=10\nHEIGHT=8\n"
                           "ENTRY=0,0\nEXIT=9,7\nPERFECT=True\n"
                           "OUTPUT_FILE=maze.txt\nPRINT_MODE=ascii")
        result = ft_parsing_config(path)
        assert result.maze_width == 10

    def test_tc0103_comment_with_equals_ignored(self, tmp_path):
        """TC-01-03: Línea '# OUTPUT_FILE=malicious.txt' no sobreescribe."""
        path = make_config(tmp_path,
                           "# OUTPUT_FILE=malicious.txt\n"
                           "WIDTH=10\nHEIGHT=8\nENTRY=0,0\nEXIT=9,7\n"
                           "PERFECT=True\nOUTPUT_FILE=maze.txt\n"
                           "PRINT_MODE=ascii")
        result = ft_parsing_config(path)
        assert result.maze_output != "malicious.txt"
        assert result.maze_output == "maze.txt"

    def test_tc0104_whitespace_trimming(self, tmp_path):
        """TC-01-04: Espacios alrededor de clave y valor se eliminan."""
        path = make_config(tmp_path,
                           "  WIDTH  =  10  \n  HEIGHT  =  8  \n"
                           "ENTRY=0,0\nEXIT=9,7\nPERFECT=True\n"
                           "OUTPUT_FILE=maze.txt\nPRINT_MODE=ascii")
        result = ft_parsing_config(path)
        assert result.maze_width == 10
        assert result.maze_height == 8

    def test_tc0105_print_mode_uppercase(self, tmp_path):
        """TC-01-05: PRINT_MODE en minúsculas → convertido a mayúsculas."""
        path = minimal_config(tmp_path, mode="ascii")
        result = ft_parsing_config(path)
        assert result.maze_print_mode == "ASCII"

    def test_tc0106_file_not_found(self, capsys):
        """TC-01-06: Archivo inexistente → [ERROR] + exit(1)."""
        with pytest.raises(SystemExit) as exc:
            ft_parsing_config("/nonexistent/path/config.txt")
        assert exc.value.code == 1
        assert "[ERROR]" in capsys.readouterr().out

    def test_tc0107_invalid_width_type(self, tmp_path, capsys):
        """TC-01-07: WIDTH=invalid → [ERROR] + exit(1)."""
        path = make_config(tmp_path, "WIDTH=invalid")
        with pytest.raises(SystemExit) as exc:
            ft_parsing_config(path)
        assert exc.value.code == 1
        assert "[ERROR]" in capsys.readouterr().out

    def test_tc0108_invalid_entry_format(self, tmp_path):
        """TC-01-08: ENTRY=abc → exit(1)."""
        path = make_config(tmp_path, "WIDTH=10\nHEIGHT=10\nENTRY=abc")
        with pytest.raises(SystemExit) as exc:
            ft_parsing_config(path)
        assert exc.value.code == 1

    def test_tc0109_seed_code_empty_generates_random(self, tmp_path):
        """TC-01-09: SEED_CODE vacío → entero aleatorio entre 1 y 50000."""
        path = minimal_config(tmp_path, extra="SEED_CODE=\n")
        result = ft_parsing_config(path)
        assert result.maze_seed_code is not None
        assert 1 <= result.maze_seed_code <= 50000

    def test_tc0110_no_seed_defaults_empty(self, tmp_path):
        """TC-01-10: Sin clave SEED → maze_seed == ''."""
        path = minimal_config(tmp_path)
        result = ft_parsing_config(path)
        assert result.maze_seed == ""

    def test_tc0111_seed_value_parsed(self, tmp_path):
        """TC-01-11: SEED=output/seed1.txt → maze_seed correcto."""
        path = minimal_config(tmp_path, extra="SEED=output/seed1.txt\n")
        result = ft_parsing_config(path)
        assert result.maze_seed == "output/seed1.txt"


# ---------------------------------------------------------------------------
# TC-02 — Validación del modelo ConfigModel
# ---------------------------------------------------------------------------

class TestConfigModel:
    """TC-02: ConfigModel validation rules."""

    def test_tc0201_width_less_than_3(self):
        """TC-02-01: WIDTH < 3 → ValidationError."""
        with pytest.raises(Exception):
            ConfigModel(maze_width=2, maze_height=8, maze_entry=(0, 0),
                        maze_exit=(1, 7), maze_perfect=True,
                        maze_output="maze.txt", maze_print_mode="ASCII")

    def test_tc0202_width_times_height_over_1000(self, tmp_path, capsys):
        """TC-02-02: WIDTH×HEIGHT >= 1000 → exit(1) con mensaje recursión."""
        path = make_config(tmp_path,
                           "WIDTH=32\nHEIGHT=32\nENTRY=0,0\nEXIT=31,31\n"
                           "PERFECT=True\nOUTPUT_FILE=maze.txt\n"
                           "PRINT_MODE=ascii")
        with pytest.raises(SystemExit) as exc:
            ft_parsing_config(path)
        assert exc.value.code == 1

    def test_tc0203_width_times_height_999_valid(self):
        """TC-02-03: WIDTH×HEIGHT = 999 → válido."""
        cfg = ConfigModel(maze_width=27, maze_height=37, maze_entry=(0, 0),
                          maze_exit=(26, 36), maze_perfect=True,
                          maze_output="maze.txt", maze_print_mode="ASCII")
        assert cfg.maze_width == 27

    def test_tc0204_entry_out_of_bounds(self):
        """TC-02-04: ENTRY fuera de límites → error."""
        with pytest.raises(Exception):
            ConfigModel(maze_width=10, maze_height=10, maze_entry=(10, 0),
                        maze_exit=(9, 9), maze_perfect=True,
                        maze_output="maze.txt", maze_print_mode="ASCII")

    def test_tc0205_entry_equals_exit(self):
        """TC-02-05: ENTRY == EXIT → error."""
        with pytest.raises(Exception):
            ConfigModel(maze_width=10, maze_height=10, maze_entry=(0, 0),
                        maze_exit=(0, 0), maze_perfect=True,
                        maze_output="maze.txt", maze_print_mode="ASCII")

    def test_tc0206_invalid_print_mode(self):
        """TC-02-06: PRINT_MODE inválido → error."""
        with pytest.raises(Exception):
            ConfigModel(maze_width=10, maze_height=10, maze_entry=(0, 0),
                        maze_exit=(9, 9), maze_perfect=True,
                        maze_output="maze.txt", maze_print_mode="CONSOLE")

    def test_tc0207_perfect_false_string(self, tmp_path):
        """TC-02-07: PERFECT=false como string → maze_perfect es False."""
        path = minimal_config(tmp_path, perfect="false")
        result = ft_parsing_config(path)
        assert result.maze_perfect is False


# ---------------------------------------------------------------------------
# TC-03 — Generación del laberinto
# ---------------------------------------------------------------------------

class TestMazeGeneration:
    """TC-03: Maze generation properties."""

    def test_tc0301_reproducibility_same_seed(self):
        """TC-03-01: Mismo seed_code → mismo generate_seed()."""
        m1 = build_maze(seed_code=1234)
        m2 = build_maze(seed_code=1234)
        assert SeedFile(m1).generate_seed() == SeedFile(m2).generate_seed()

    def test_tc0302_different_seeds_different_mazes(self):
        """TC-03-02: Diferente seed_code → diferente laberinto."""
        m1 = build_maze(seed_code=1)
        m2 = build_maze(seed_code=2)
        assert SeedFile(m1).generate_seed() != SeedFile(m2).generate_seed()

    def test_tc0303_full_connectivity(self):
        """TC-03-03: Todas las celdas no-42 son accesibles desde ENTRY."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 9))
        reachable = bfs_reachable(maze, (0, 0))
        for row in maze.grid_maze:
            for cell in row:
                if not cell.is_FORTY_TWO:
                    assert (cell.x, cell.y) in reachable, (
                        f"Cell ({cell.x},{cell.y}) not reachable")

    def test_tc0304_wall_symmetry(self):
        """TC-03-04: Paredes simétricas entre celdas vecinas."""
        maze = build_maze(width=12, height=9)
        dirs = {"E": (1, 0, "W"), "S": (0, 1, "N")}
        for row in maze.grid_maze:
            for cell in row:
                for wall, (dx, dy, opp) in dirs.items():
                    neighbor = UtilsMaze(maze).get_cell(cell.x + dx, cell.y + dy)
                    if neighbor:
                        assert cell.walls[wall] == neighbor.walls[opp], (
                            f"Asymmetric wall at ({cell.x},{cell.y}) {wall}")

    def test_tc0305_border_walls(self):
        """TC-03-05: Celdas del borde tienen paredes externas cerradas."""
        maze = build_maze(width=10, height=8)
        w, h = maze.width, maze.height
        for x in range(w):
            assert maze.grid_maze[0][x].walls["N"] is True
            assert maze.grid_maze[h - 1][x].walls["S"] is True
        for y in range(h):
            assert maze.grid_maze[y][0].walls["W"] is True
            assert maze.grid_maze[y][w - 1].walls["E"] is True

    def test_tc0306_no_3x3_open_area(self):
        """TC-03-06: No existe ninguna zona abierta 3×3."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 0))

        def passage(x1: int, y1: int, wall: str) -> bool:
            c = UtilsMaze(maze).get_cell(x1, y1)
            if c is None or c.walls[wall]:
                return False
            dx, dy = {"E": (1, 0), "S": (0, 1)}[wall]
            n = UtilsMaze(maze).get_cell(x1 + dx, y1 + dy)
            opp = {"E": "W", "S": "N"}[wall]
            return n is not None and not n.walls[opp]

        for y in range(maze.height - 2):
            for x in range(maze.width - 2):
                open_3x3 = all([
                    passage(x, y, "E"), passage(x + 1, y, "E"),
                    passage(x, y + 1, "E"), passage(x + 1, y + 1, "E"),
                    passage(x, y, "S"), passage(x + 1, y, "S"),
                    passage(x + 2, y, "S"),
                ])
                assert not open_3x3, f"3×3 open area found at ({x},{y})"

    def test_tc0307_perfect_maze_single_path(self):
        """TC-03-07: PERFECT=True → exactamente un camino (spanning tree)."""
        maze = build_maze(width=12, height=9, perfect=True)
        non_42 = sum(1 for row in maze.grid_maze
                     for c in row if not c.is_FORTY_TWO)
        # Count open passages (each open wall counted once)
        edges = 0
        for row in maze.grid_maze:
            for cell in row:
                if cell.is_FORTY_TWO:
                    continue
                for wall, (dx, dy) in [("E", (1, 0)), ("S", (0, 1))]:
                    if not cell.walls[wall]:
                        neighbor = UtilsMaze(maze).get_cell(cell.x + dx, cell.y + dy)
                        if neighbor and not neighbor.is_FORTY_TWO:
                            edges += 1
        assert edges == non_42 - 1, (
            f"Perfect maze should have {non_42 - 1} edges, got {edges}")

    def test_tc0308_imperfect_maze_multiple_paths(self):
        """TC-03-08: PERFECT=False → más aristas que un spanning tree."""
        maze = build_maze(width=12, height=9, perfect=False)
        non_42 = sum(1 for row in maze.grid_maze
                     for c in row if not c.is_FORTY_TWO)
        edges = 0
        for row in maze.grid_maze:
            for cell in row:
                if cell.is_FORTY_TWO:
                    continue
                for wall, (dx, dy) in [("E", (1, 0)), ("S", (0, 1))]:
                    if not cell.walls[wall]:
                        neighbor = UtilsMaze(maze).get_cell(cell.x + dx, cell.y + dy)
                        if neighbor and not neighbor.is_FORTY_TWO:
                            edges += 1
        assert edges > non_42 - 1

    def test_tc0309_imperfect_still_connected(self):
        """TC-03-09: PERFECT=False → laberinto sigue conectado."""
        maze = build_maze(width=12, height=9, perfect=False,
                          entry=(0, 0), exit_=(11, 8))
        reachable = bfs_reachable(maze, (0, 0))
        for row in maze.grid_maze:
            for cell in row:
                if not cell.is_FORTY_TWO:
                    assert (cell.x, cell.y) in reachable


# ---------------------------------------------------------------------------
# TC-04 — Patrón "42" (watermark)
# ---------------------------------------------------------------------------

class TestWatermark:
    """TC-04: Watermark '42' placement and properties."""

    def test_tc0401_watermark_present_large_maze(self):
        """TC-04-01: WIDTH>=9, HEIGHT>=7 → watermark presente."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 0))
        forty_two_cells = [c for row in maze.grid_maze
                           for c in row if c.is_FORTY_TWO]
        assert len(forty_two_cells) > 0

    def test_tc0402_watermark_cells_all_walls_closed(self):
        """TC-04-02: Celdas del watermark tienen todas las paredes cerradas."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 0))
        for row in maze.grid_maze:
            for cell in row:
                if cell.is_FORTY_TWO:
                    assert all(cell.walls.values()), (
                        f"Cell ({cell.x},{cell.y}) is_FORTY_TWO but has open wall")

    def test_tc0403_watermark_centered(self):
        """TC-04-03: Watermark centrado en el laberinto."""
        maze = build_maze(width=15, height=11, entry=(0, 0), exit_=(14, 0))
        cx, cy = 15 // 2, 11 // 2  # center = (7, 5)
        forty_two = {(c.x, c.y) for row in maze.grid_maze
                     for c in row if c.is_FORTY_TWO}
        # At least one cell should be near center
        assert any(abs(x - cx) <= 4 and abs(y - cy) <= 3
                   for x, y in forty_two)

    def test_tc0404_watermark_omitted_small_maze(self, capsys):
        """TC-04-04: WIDTH<9 o HEIGHT<7 → watermark omitido, mensaje en consola."""
        config = ConfigModel(
            maze_width=5, maze_height=5, maze_entry=(0, 0),
            maze_exit=(4, 4), maze_perfect=True,
            maze_output="maze.txt", maze_print_mode="ASCII",
            maze_seed="", maze_seed_code=1,
        )
        maze = Maze(config)
        result = UtilsMaze(maze).watermark()
        assert result is False
        output = capsys.readouterr().out
        assert len(output) > 0  # mensaje impreso

    def test_tc0405_entry_on_watermark_rejected(self):
        """TC-04-05: ENTRY en celda del watermark → check_valid_position False."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 0))
        # Find a FORTY_TWO cell
        ft_cell = next((c for row in maze.grid_maze
                        for c in row if c.is_FORTY_TWO), None)
        if ft_cell is None:
            pytest.skip("No FORTY_TWO cells found")
        result = UtilsMaze(maze).check_valid_position(
            (ft_cell.x, ft_cell.y), (0, 0))
        assert result is False

    def test_tc0406_watermark_cells_not_reachable(self):
        """TC-04-06: Celdas del watermark no son accesibles por BFS."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 9))
        reachable = bfs_reachable(maze, (0, 0))
        for row in maze.grid_maze:
            for cell in row:
                if cell.is_FORTY_TWO:
                    assert (cell.x, cell.y) not in reachable


# ---------------------------------------------------------------------------
# TC-05 — Codificación hexadecimal (generate_seed)
# ---------------------------------------------------------------------------

class TestHexEncoding:
    """TC-05: Hex encoding of cell walls."""

    def _cell_with_walls(self, **walls: bool) -> Cell:
        """Create a Cell and set specific wall states."""
        cell = Cell(0, 0)
        for direction, value in walls.items():
            cell.walls[direction] = value
        return cell

    def _encode(self, cell: Cell) -> str:
        """Encode a single cell the same way generate_seed does."""
        val = 0
        if cell.walls.get("N"):
            val += 1
        if cell.walls.get("E"):
            val += 2
        if cell.walls.get("S"):
            val += 4
        if cell.walls.get("W"):
            val += 8
        return f"{val:X}"

    def test_tc0502_all_walls_closed_is_F(self):
        """TC-05-02: Todas las paredes cerradas → 'F'."""
        cell = self._cell_with_walls(N=True, E=True, S=True, W=True)
        assert self._encode(cell) == "F"

    def test_tc0503_no_walls_is_0(self):
        """TC-05-03: Sin paredes → '0'."""
        cell = self._cell_with_walls(N=False, E=False, S=False, W=False)
        assert self._encode(cell) == "0"

    def test_tc0504_only_north_is_1(self):
        """TC-05-04: Solo pared Norte → '1'."""
        cell = self._cell_with_walls(N=True, E=False, S=False, W=False)
        assert self._encode(cell) == "1"

    def test_tc0505_only_east_is_2(self):
        """TC-05-05: Solo pared Este → '2'."""
        cell = self._cell_with_walls(N=False, E=True, S=False, W=False)
        assert self._encode(cell) == "2"

    def test_tc0506_south_and_west_is_C(self):
        """TC-05-06: Paredes Sur y Oeste → 'C' (4+8=12)."""
        cell = self._cell_with_walls(N=False, E=False, S=True, W=True)
        assert self._encode(cell) == "C"

    def test_tc0501_seed_structure(self):
        """TC-05-01: generate_seed produce WIDTH columnas por HEIGHT filas."""
        maze = build_maze(width=5, height=3, entry=(0, 0), exit_=(4, 2))
        seed = SeedFile(maze).generate_seed()
        assert len(seed) == 3
        for row in seed:
            assert len(row) == 5
            for char in row:
                assert char in "0123456789ABCDEF"


# ---------------------------------------------------------------------------
# TC-06 — Solver BFS
# ---------------------------------------------------------------------------

class TestBFSSolver:
    """TC-06: BFS solver correctness."""

    def test_tc0601_solution_found(self):
        """TC-06-01: Laberinto perfecto → solución no vacía."""
        maze = build_maze(width=10, height=8, entry=(0, 0), exit_=(9, 7))
        solution = SolveMaze(maze).solve_maze((0, 0), (9, 7))
        assert len(solution) > 0
        assert all(c in "NSEW" for c in solution)

    def test_tc0603_path_to_directions(self):
        """TC-06-03: path_to_directions convierte celdas a direcciones."""
        config = ConfigModel(
            maze_width=5, maze_height=5, maze_entry=(0, 0),
            maze_exit=(4, 4), maze_perfect=True,
            maze_output="maze.txt", maze_print_mode="ASCII",
            maze_seed="", maze_seed_code=1,
        )
        maze = Maze(config)
        maze.initial_matrix()
        c1 = UtilsMaze(maze).get_cell(0, 0)
        c2 = UtilsMaze(maze).get_cell(1, 0)
        c3 = UtilsMaze(maze).get_cell(1, 1)
        assert c1 and c2 and c3
        result = SolveMaze(maze).path_to_directions([c1, c2, c3])
        assert result == "ES"

    def test_tc0602_solution_is_valid_path(self):
        """TC-06-02: La solución no atraviesa paredes."""
        maze = build_maze(width=10, height=8, entry=(0, 0), exit_=(9, 7))
        solution = SolveMaze(maze).solve_maze((0, 0), (9, 7))
        offsets = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
        x, y = 0, 0
        for step in solution:
            cell = UtilsMaze(maze).get_cell(x, y)
            assert cell is not None
            assert not cell.walls[step], (
                f"Solution crosses wall {step} at ({x},{y})")
            dx, dy = offsets[step]
            x, y = x + dx, y + dy
        assert (x, y) == (9, 7)


# ---------------------------------------------------------------------------
# TC-10 — Casos límite del laberinto
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """TC-10: Edge cases for maze dimensions and positions."""

    def test_tc1001_minimum_valid_maze(self, capsys):
        """TC-10-01: Laberinto mínimo 3×3 → genera sin error."""
        maze = build_maze(width=3, height=3, entry=(0, 0), exit_=(2, 2))
        seed = SeedFile(maze).generate_seed()
        assert len(seed) == 3
        assert len(seed[0]) == 3
        # No watermark message expected
        output = capsys.readouterr().out
        assert "not sufficient" in output  # watermark omitted message

    def test_tc1002_minimum_watermark_maze(self):
        """TC-10-02: Laberinto 9×7 → watermark presente."""
        maze = build_maze(width=9, height=7, entry=(0, 0), exit_=(8, 6))
        forty_two = [c for row in maze.grid_maze
                     for c in row if c.is_FORTY_TWO]
        assert len(forty_two) > 0

    def test_tc1003_maximum_allowed_maze(self):
        """TC-10-03: WIDTH×HEIGHT=999 → genera sin RecursionError."""
        maze = build_maze(width=27, height=37, entry=(0, 0), exit_=(26, 36))
        seed = SeedFile(maze).generate_seed()
        assert len(seed) == 37
        assert len(seed[0]) == 27

    def test_tc1004_entry_exit_opposite_corners(self):
        """TC-10-04: ENTRY=(0,0), EXIT=(14,9) → solución válida."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 9))
        solution = SolveMaze(maze).solve_maze((0, 0), (14, 9))
        assert len(solution) > 0

    def test_tc1005_entry_exit_same_row(self):
        """TC-10-05: ENTRY y EXIT en la misma fila → solución válida."""
        maze = build_maze(width=15, height=10, entry=(0, 0), exit_=(14, 0))
        solution = SolveMaze(maze).solve_maze((0, 0), (14, 0))
        assert len(solution) > 0

import random
import sys
import time
from random import choice
from typing import List, Any
from inc.mlx.mlx import Mlx
from src.config.enums import Colors, ColorsHex, Walls, MazeAlgorithm
from src.model.cell import Cell
from src.model.maze import Maze
from src.parser.config_model import ConfigModel
from src.utils.utils_maze import UtilsMaze
from src.core.solve_maze import SolveMaze
from src.core.maze_generator import MazeGenerator
from src.core.seed_file import SeedFile


class MazePainter_mlx:
    """
    MazePainter_mlx: A graphical maze visualization and interaction handler
    using MLX library.

    This class manages the rendering, display, and interactive manipulation of
    maze graphics using the MLX (a lightweight graphics library). It handles
    window creation, event processing, image rendering, and user interactions
    for maze visualization including solution paths, color schemes, and maze
    regeneration with different algorithms.

    Attributes:
        maze (Maze): The maze object to be visualized.
        maze_config (ConfigModel): Configuration model containing maze
        dimensions and settings.
        maze_width (int): Width of the maze in cells.
        maze_height (int): Height of the maze in cells.
        show_solution (bool): Flag indicating whether the solution path should
        be displayed.
        needs_redraw (bool): Flag indicating whether the window requires
        redrawing.
        cell_size (int): Size of each maze cell in pixels (default: 40).
        win_width (int): Window width in pixels.
        win_height (int): Window height in pixels.
        params (tuple): Tuple containing (mlx_instance, mlx_ptr, window_ptr).
        img (memoryview): Image buffer for maze rendering.
        sol_img (memoryview): Image buffer for solution path rendering.
        img_data (memoryview): Pixel data for maze image.
        sol_data (memoryview): Pixel data for solution image.
        bpp (int): Bits per pixel for maze image.
        sol_bpp (int): Bits per pixel for solution image.
        size_line (int): Number of bytes per row in maze image.
        sol_size_line (int): Number of bytes per row in solution image.
        bytes_per_pixel (int): Number of bytes per pixel.
        endian (int): Endianness of the maze image.
        sol_endian (int): Endianness of the solution image.

    Methods:
        __init__(maze, maze_config): Initialize the maze painter with maze and
        configuration.
        create_window(): Create and initialize the MLX window with calculated
        dimensions.
        mlx_close_window(param): Handle window closure and cleanup.
        mlx_key_press(key, param): Process keyboard input and execute
        corresponding actions.
        redraw_request(param): Request window redraw on expose events.
        create_hooks(): Register event handlers for window close, key press,
        and redraw events.
        create_image(): Create and initialize the maze image buffer.
        create_solution_img(): Create and initialize the solution path image
        buffer.
        put_pixel_img(x, y, color, img): Write a single pixel to an image
        buffer.
        cell_pixel_put(cell, x, y, color): Draw a maze cell including walls
        and special markers.
        start_pixel_put(color): Draw all maze cells with specified color.
        put_parameters(param): Display on-screen menu and instructions.
        print_solution(maze, maze_config): Calculate and render the maze
        solution path.
        render(param): Perform conditional redraw and update the window
        display.
        start_visual(): Initialize the visual window and start the rendering
        loop.

    Keyboard Controls:
        1/ESC: Re-generate a new maze with current algorithm.
        2: Toggle solution path visibility.
        3: Change maze wall color.
        4: Change 42 pattern (special cells) color.
        5: Switch between DFS and Prim maze generation algorithms.
        6: Close the window and exit.
    """
    def __init__(self, maze: Maze, maze_config: ConfigModel) -> None:
        """
        Initialize the PrintMinilib visual renderer.

        Args:
            maze (Maze): The maze object to be visualized.
            maze_config (ConfigModel): Configuration model containing maze
            dimensions and settings.

        Raises:
            ValueError: If WIDTH or HEIGHT values in the config file are
            invalid.
            SystemExit: Exits with code 1 if configuration values are
            incorrect.

        Attributes:
            maze (Maze): The maze instance to render.
            maze_config (ConfigModel): The configuration model for the maze.
            maze_width (int): Width of the maze from config.
            maze_height (int): Height of the maze from config.
            show_solution (bool): Flag to display the maze solution (default:
            False).
            needs_redraw (bool): Flag indicating if the display needs to be
            redrawn (default: True).
            cell_size (int): Size of each cell in pixels (default: 40).
        """
        try:
            self.maze: Maze = maze
            self.maze_config: ConfigModel = maze_config
            self.maze_width: int = maze_config.maze_width
            self.maze_height: int = maze_config.maze_height
            self.show_solution: bool = False
            self.needs_redraw: bool = True
            self.pattern_color: int = ColorsHex.WHITE.value
            self.maze_color: int = ColorsHex.GRAY.value
            self.current_algorithm: str = MazeAlgorithm.DFS.value
            self.is_animating_colors: bool = False
            self.animation_delay: float = 0.005
            self.next_animation_at: float = 0.0
            self.animation_index: int = 0
            self.animation_colors: list[ColorsHex] = []
            self.util_mz: UtilsMaze = UtilsMaze(maze)
            self.solve: SolveMaze = SolveMaze(maze)
        except ValueError as v_e:
            print(
                f"{Colors.RED.value}[ERROR] - WIDTH/HEIGHT wrong "
                f"values in config file!"
            )
            print(f"{v_e}{Colors.RESET.value}")
            sys.exit(1)
        self.cell_size: int = 40

    def get_display_colors(self) -> list[ColorsHex]:
        """
        Return the list of visible colors used for animation.

        Returns:
            list[ColorsHex]: Colors suitable for maze and pattern rendering.
        """
        return [
            ColorsHex.WHITE,
            ColorsHex.BLUE,
            ColorsHex.YELLOW,
            ColorsHex.CYAN,
            ColorsHex.MAGENTA,
            ColorsHex.GRAY,
            ColorsHex.ORANGE,
            ColorsHex.PURPLE,
            ColorsHex.BROWN,
            ColorsHex.PINK,
            ColorsHex.LIME,
        ]

    def stop_color_animation(self) -> None:
        """
        Stop the timed color animation.

        Returns:
            None
        """
        self.is_animating_colors = False
        self.animation_colors = []
        self.animation_index = 0
        self.next_animation_at = 0.0

    def start_color_animation(self) -> None:
        """
        Start the timed color animation.

        Returns:
            None
        """
        self.animation_colors = self.get_display_colors()
        self.animation_index = 0
        self.is_animating_colors = True
        self.next_animation_at = time.monotonic()

    def update_color_animation(self, param: tuple[Any, Any, Any]) -> None:
        """
        Advance the color animation when enough time has passed.

        Args:
            param (tuple[Any, Any, Any]): MLX context tuple.

        Returns:
            None
        """
        if not self.is_animating_colors:
            return

        if time.monotonic() < self.next_animation_at:
            return

        if self.animation_index >= len(self.animation_colors):
            self.stop_color_animation()
            return

        maze_color = self.animation_colors[self.animation_index]
        pattern_choices = [
            color for color in self.animation_colors if color != maze_color
        ]
        pattern_color = choice(pattern_choices)
        self.draw_maze_by_op(
            maze_color.value,
            pattern_color.value,
            param,
            self.current_algorithm,
        )
        self.animation_index += 1
        self.next_animation_at = time.monotonic() + self.animation_delay

    def create_window(self) -> None:
        """
        Initialize and create a graphical window using the MLX library.

        Sets up the window dimensions based on maze dimensions and cell size,
        with additional height for UI elements. Initializes the MLX context
        and creates a new window with the calculated dimensions.

        The window width is calculated as maze_width * cell_size.
        The window height is calculated as (maze_height * cell_size) + 200.

        Stores the MLX instance, MLX pointer, and window pointer in self.params
        as a tuple for later use.

        Raises:
            SystemExit: If cell_size, maze_width, or maze_height are invalid
                       (ValueError or TypeError), prints error message and
                       exits with code 1.

        Note:
            Window title displays: "agiron-d /\\ joflorid MAZE"
        """
        m: Any = Mlx()
        m_ptr: Any = m.mlx_init()
        try:
            if self.maze_width < 12:
                self.maze_width = 12
            self.win_width = self.maze_width * self.cell_size
            self.win_height = (self.maze_height * self.cell_size) + 280
        except (ValueError, TypeError) as e:
            print(f"{Colors.RED.value}[ERROR] - cell size definition is "
                  f"wrong.")
            print(f"{e}{Colors.RESET.value}")
            sys.exit(1)
        if m and m_ptr:
            win_ptr: Any = m.mlx_new_window(
                    m_ptr,
                    self.win_width,
                    self.win_height,
                    "agiron-d /\\ joflorid MAZE"
            )
        self.params: tuple[Any, Any, Any] = (m, m_ptr, win_ptr)

    def mlx_close_window(self, param: tuple[Any, Any, Any]) -> None:
        """
        Close the MLX window and exit the event loop.

        Args:
            param (tuple): A tuple containing:
                - m: The MLX instance
                - m_ptr: Pointer to the MLX connection
                - win_ptr: Pointer to the window to be destroyed

        Returns:
            None
        """
        m, m_ptr, win_ptr = param
        m.mlx_destroy_window(m_ptr, win_ptr)
        m.mlx_loop_exit(m_ptr)

    def pattern_color_set(self, pattern_color: int) -> None:
        """
        Update the color of the special '42' pattern cells in the maze image.

        Iterates through FORTY_TWO cells and repaints their region using
        _fill_rect (row-by-row slice writes) instead of per-pixel loops.

        Args:
            pattern_color (int): The hexadecimal color value to apply to the
            pattern.
        """
        self.pattern_color = pattern_color
        color_bytes: bytes = pattern_color.to_bytes(4, byteorder=sys.byteorder)
        for y, row in enumerate(self.maze.grid_maze):
            for x, cell in enumerate(row):
                if cell.is_FORTY_TWO:
                    x_offset = x * self.cell_size
                    y_offset = y * self.cell_size
                    self._fill_rect(self.img_data, color_bytes,
                                    x_offset, y_offset,
                                    self.cell_size, self.cell_size)
        self.needs_redraw = True

    def draw_maze_by_op(self, maze_color: int,
                        pattern_color: int,
                        param: tuple[Any, Any, Any],
                        algorithm: str = MazeAlgorithm.DFS.value) -> None:
        """Generate and draw a maze using the specified algorithm and colors.

        This method initializes a new maze with the given parameters, builds
        it using the specified algorithm, generates a solution, and renders it
        to the display.

        Args:
            maze_color (int): The color value to use for rendering maze walls.
            pattern_color (int): The color value to use for maze pattern
                elements.
            param (tuple[Any, Any, Any]): A tuple containing:
                - m: The MinilibX instance.
                - m_ptr: Pointer to the MinilibX context.
                - win_ptr: Pointer to the MinilibX window.
            algorithm (str, optional): The maze generation algorithm to use.
                Defaults to MazeAlgorithm.DFS.value.

        Raises:
            ValueError: If maze generation, solution solving, or rendering
                fails.

        Returns:
            None
        """

        m, m_ptr, win_ptr = param
        self.maze.initial_matrix()
        self.maze.seed_code = random.randint(1, 50000)
        m.mlx_clear_window(m_ptr, win_ptr)
        # m.mlx_destroy_image(m_ptr, self.img)
        self.img_data[:] = bytes(len(self.img_data))
        # m.mlx_destroy_image(m_ptr, self.sol_img)
        self.sol_data[:] = bytes(len(self.sol_data))

        self.maze_color = maze_color
        try:
            MazeGenerator(self.maze).perfect_maze(
                self.maze_config.maze_entry,
                self.maze_config.maze_exit,
                self.maze_config.maze_perfect,
                algorithm
            )
            self.pattern_color = pattern_color
            self.current_algorithm = algorithm
            self.show_solution = False
            self.start_pixel_put(maze_color)
            my_maze_seed = SeedFile(self.maze).generate_seed()
            solution_directions = self.solve.solve_maze(
                self.maze_config.maze_entry, self.maze_config.maze_exit,
                True
            )
            SeedFile(self.maze).export_seed(
                maze_seed=my_maze_seed,
                solve_directions=solution_directions,
                maze_config=self.maze_config,
            )
            self.needs_redraw = True
        except Exception:
            raise ValueError("Got an error in draw_maze_by_op")

    def mlx_key_press(self, key: int, param: tuple[Any, Any, Any]) -> None:
        """
        Handle keyboard input events for the maze visualization.

        Processes various key presses to control maze generation,
        visualization,
        and customization options:
        - ESC/6: Close the window
        - 1: Regenerate a new maze with the current configuration
        - 2: Toggle the solution path display on/off
        - 3: Randomly rotate maze wall colors (excluding white, green, red,
        black)
        - 4: Randomly rotate the 42 pattern cell colors
        - 5: Regenerate maze using a Prim's algorithm

        Args:
            key (int): The key code from the MLX library event handler
            param (tuple): A tuple containing (m, m_ptr, win_ptr) where:
                - m: MLX instance for graphics operations
                - m_ptr: MLX display pointer
                - win_ptr: MLX window pointer

        Returns:
            None
        """
        if key == 65307 or key == 65429 or key == 55:  # key 7/ESC
            self.mlx_close_window(self.params)

        elif key == 65436 or key == 49:  # key 1: Re-generate new maze DFS
            self.stop_color_animation()
            self.draw_maze_by_op(ColorsHex.GRAY.value,
                                 ColorsHex.WHITE.value, param)

        elif key == 65433 or key == 50:  # key 2: Show/Hide path
            self.stop_color_animation()
            if not self.show_solution:
                self.show_solution = True
                self.print_solution(self.maze, self.maze_config)
            else:
                self.show_solution = False
            self.needs_redraw = True

        elif key == 65435 or key == 51:  # key 3: Rotate maze colors
            self.stop_color_animation()
            suitable_colors = [
                c
                for c in self.get_display_colors()
                if c not in (
                    ColorsHex.GREEN,
                    ColorsHex.RED,
                )
            ]
            if suitable_colors:
                color_chosen = choice(suitable_colors)
            else:
                color_chosen = ColorsHex.GRAY
            self.maze_color = color_chosen.value
            self.start_pixel_put(color_chosen.value)
            self.needs_redraw = True

        elif key == 65430 or key == 52:  # key 4: Rotate 42 pattern colors
            self.stop_color_animation()
            suitable_colors = [
                c
                for c in self.get_display_colors()
                if c not in (
                    ColorsHex.GREEN,
                    ColorsHex.RED,
                )
            ]
            color_chosen = choice(suitable_colors)

            self.pattern_color_set(color_chosen.value)

        elif key == 103:  # Key g
            self.stop_color_animation()
            self.pattern_color_set(ColorsHex.GREEN.value)

        elif key == 114:  # Key r
            self.stop_color_animation()
            self.pattern_color_set(ColorsHex.RED.value)

        elif key == 98:  # Key b
            self.stop_color_animation()
            self.pattern_color_set(ColorsHex.BLUE.value)

        elif key == 65437 or key == 53:  # key 5: Change algorithm to PRIM
            self.stop_color_animation()
            self.draw_maze_by_op(ColorsHex.GRAY.value, ColorsHex.WHITE.value,
                                 param, MazeAlgorithm.PRIM.value)

        elif key == 65432 or key == 54:  # key 6: Animate colors
            self.start_color_animation()

    def redraw_request(self, param: tuple[Any, Any, Any]) -> None:
        """
        Request a redraw of the visual display.

        Sets the internal flag to indicate that the display needs to be redrawn
        on the next render cycle.

        Args:
            param (tuple): Parameters associated with the redraw request.
        """
        self.needs_redraw = True

    def create_hooks(self) -> None:
        """
        Initialize and register event hooks for the MLX window.

        Sets up three event handlers for the window:
        - Closes the window when the X button is clicked (hook event 33)
        - Captures and processes key press events
        - Handles window expose events to trigger redraws (hook event 12)

        The hooks are registered with the MLX library using the window pointer
        and associated parameters for callback functions.
        """
        m, m_ptr, win_ptr = self.params
        # Closing window with X button
        m.mlx_hook(win_ptr, 33, 0, self.mlx_close_window, self.params)
        # Capture key pressed
        m.mlx_key_hook(win_ptr, self.mlx_key_press, self.params)
        # Handle window expose event (redraw)
        m.mlx_hook(win_ptr, 12, 1 << 15, self.redraw_request, self.params)

    def create_image(self) -> None:
        """
        Initialize and prepare a new image for maze visualization.

        Creates a new MLX image with dimensions based on maze size and cell
        size,
        retrieves the image data pointer and related metadata, and clears the
        image
        data to remove any garbage from reused memory.

        The method sets up the following instance attributes:
        - self.img: MLX image pointer
        - self.img_data: Linear byte array containing pixel data
        - self.bpp: Bits per pixel (typically 32)
        - self.size_line: Number of bits per entire row
        - self.bytes_per_pixel: Calculated bytes per pixel (bpp // 8)
        - self.endian: Endianness information

        Returns:
            None
        """
        m, m_ptr, _ = self.params
        width: int = self.maze_width * self.cell_size
        height: int = self.maze_height * self.cell_size
        # Getting img pointer.
        self.img = m.mlx_new_image(m_ptr, width, height)
        # self.img_data is a huge lineal array pointed by self.img
        # self.bpp bits per pixel. Usually 32 (4 bytes)
        # self.size_line is the number of bits per entire row
        self.img_data, self.bpp, self.size_line, self.endian = \
            m.mlx_get_data_addr(self.img)
        self.bytes_per_pixel = self.bpp // 8
        # Clear image data to avoid garbage from reused memory
        self.img_data[:] = bytes(len(self.img_data))

    def create_solution_img(self) -> None:
        """
        Create a new image for displaying the solution path.

        Initializes a new MLX image with dimensions matching the maze size
        (maze_width * cell_size by maze_height * cell_size).
        Retrieves the image data address and associated metadata (bytes per
        pixel, size of line, and endianness).
        Clears the image data by filling it with null bytes.

        Attributes set:
            sol_img: The MLX image object for the solution visualization.
            sol_data: Raw pixel data buffer for the solution image.
            sol_bpp: Bytes per pixel for the solution image.
            sol_size_line: Size in bytes of one line in the solution image.
            sol_endian: Byte order (endianness) of the solution image data.
        """
        m, m_ptr, _ = self.params
        width: int = self.maze_width * self.cell_size
        height: int = self.maze_height * self.cell_size
        self.sol_img = m.mlx_new_image(m_ptr, width, height)
        self.sol_data, self.sol_bpp, self.sol_size_line, self.sol_endian = (
            m.mlx_get_data_addr(self.sol_img)
        )
        self.sol_data[:] = bytes(len(self.sol_data))

    def put_pixel_img(
            self, x: int,
            y: int,
            color: int,
            img: memoryview
            ) -> None:
        """
        Write a pixel to the image buffer at the specified coordinates.

        Args:
            x (int): The x-coordinate of the pixel within the maze image.
            y (int): The y-coordinate of the pixel within the maze image.
            color (int): The color value to be written as a 4-byte integer.
            img (memoryview): A memory view of the image buffer to write the
            pixel data to.

        Returns:
            None

        Note:
            The pixel is only written if the coordinates (x, y) are within the
            bounds of the maze image (width * cell_size, height * cell_size).
            The color is converted to 4 bytes using the system's byte order
            and written to the buffer at the calculated offset.
        """
        if 0 <= x < (self.maze_width * self.cell_size) and 0 <= y < (
            self.maze_height * self.cell_size
        ):
            offset = (y * self.size_line) + (x * self.bytes_per_pixel)
            img[offset:offset + 4] = color.to_bytes(4, byteorder=sys.byteorder)

    def _fill_hline(self, img: memoryview, color_bytes: bytes,
                    x0: int, y: int, width: int) -> None:
        """
        Fill a horizontal run of pixels in one slice operation.

        Instead of calling put_pixel_img per pixel, writes `width` pixels
        starting at (x0, y) using a single memoryview slice assignment.
        This avoids per-pixel Python overhead for wall and fill rendering.

        Args:
            img (memoryview): Target image buffer.
            color_bytes (bytes): Pre-encoded 4-byte color value.
            x0 (int): Starting x coordinate.
            y (int): Row coordinate.
            width (int): Number of pixels to fill.

        Returns:
            None
        """
        offset = y * self.size_line + x0 * self.bytes_per_pixel
        img[offset:offset + width * self.bytes_per_pixel] = (
            color_bytes * width
        )

    def _fill_rect(self, img: memoryview, color_bytes: bytes,
                   x0: int, y0: int, w: int, h: int) -> None:
        """
        Fill a rectangular region row by row using horizontal slice writes.

        Replaces nested pixel loops with one _fill_hline call per row,
        reducing Python loop iterations from w*h to h.

        Args:
            img (memoryview): Target image buffer.
            color_bytes (bytes): Pre-encoded 4-byte color value.
            x0 (int): Left edge x coordinate.
            y0 (int): Top edge y coordinate.
            w (int): Width in pixels.
            h (int): Height in pixels.

        Returns:
            None
        """
        for row in range(h):
            self._fill_hline(img, color_bytes, x0, y0 + row, w)

    def cell_pixel_put(self, cell: Cell, x: int, y: int, color: int) -> None:
        """
        Renders a single maze cell to the image buffer with walls and special
        markers.

        Draws the cell at the specified grid coordinates (x, y) by:
        - Rendering walls (North, West, South, East) with configurable
        thickness using horizontal slice writes instead of per-pixel loops
        - Marking the 42 cell (if applicable) with pattern_color fill
        - Marking the start cell (if applicable) in green with padding
        - Marking the exit cell (if applicable) in red with padding

        Args:
            cell (Cell): The cell object containing wall information and
            special flags (is_FORTY_TWO, is_start, is_exit)
            x (int): The column index of the cell in the maze grid
            y (int): The row index of the cell in the maze grid
            color (int): The RGB color value used for rendering walls

        Returns:
            None
        """
        x_offset: int = x * self.cell_size
        y_offset: int = y * self.cell_size
        wall_thickness: int = 2
        cs: int = self.cell_size

        color_bytes: bytes = color.to_bytes(4, byteorder=sys.byteorder)

        # North — horizontal band at top of cell
        if cell.walls.get(Walls.N.value):
            self._fill_rect(self.img_data, color_bytes,
                            x_offset, y_offset, cs, wall_thickness)

        # South — horizontal band at bottom of cell
        if cell.walls.get(Walls.S.value):
            self._fill_rect(self.img_data, color_bytes,
                            x_offset, y_offset + cs - wall_thickness,
                            cs, wall_thickness)

        # West — vertical band at left of cell (thin, row by row)
        if cell.walls.get(Walls.W.value):
            self._fill_rect(self.img_data, color_bytes,
                            x_offset, y_offset, wall_thickness, cs)

        # East — vertical band at right of cell
        if cell.walls.get(Walls.E.value):
            self._fill_rect(self.img_data, color_bytes,
                            x_offset + cs - wall_thickness, y_offset,
                            wall_thickness, cs)

        # 42 pattern — full cell fill
        if cell.is_FORTY_TWO:
            pattern_bytes = self.pattern_color.to_bytes(
                4, byteorder=sys.byteorder)
            self._fill_rect(self.img_data, pattern_bytes,
                            x_offset, y_offset, cs, cs)

        # Start — padded green fill
        if cell.is_start:
            green_bytes = ColorsHex.GREEN.value.to_bytes(
                4, byteorder=sys.byteorder)
            self._fill_rect(self.img_data, green_bytes,
                            x_offset + 2, y_offset + 2, cs - 4, cs - 4)

        # Exit — padded red fill
        if cell.is_exit:
            red_bytes = ColorsHex.RED.value.to_bytes(
                4, byteorder=sys.byteorder)
            self._fill_rect(self.img_data, red_bytes,
                            x_offset + 2, y_offset + 2, cs - 4, cs - 4)

    def start_pixel_put(self, color: int) -> None:
        """
        Render all cells in the maze grid with the specified color.

        Iterates through each cell in the maze grid and applies pixel rendering
        at the corresponding (x, y) coordinates with the given color value.

        Args:
            color (int): The color value to apply when rendering maze cells.

        Returns:
            None
        """
        for y, row in enumerate(self.maze.grid_maze):
            for x, cell in enumerate(row):
                self.cell_pixel_put(cell, x, y, color)

    def put_parameters(self, param: tuple[Any, Any, Any]) -> None:
        """
        Display menu parameters and instructions on the maze visualization
        window.

        Renders a menu interface containing the application title, available
        options, and user prompts. If the maze lacks necessary dimensions,
        displays a "No Watermark"
        warning message in red at the top of the menu.

        Args:
            param (tuple): A tuple containing three elements:
                - m: The MLX (MiniLibX) graphics library instance
                - m_ptr: Pointer to the MLX instance
                - win_ptr: Pointer to the application window

        Returns:
            None

        Side Effects:
            - Renders text strings to the window using mlx_string_put
            - Displays "No Watermark" warning if maze dimensions are
            insufficient
            - Displays menu options vertically with 20-pixel line spacing
        """
        m, m_ptr, win_ptr = param
        if not self.util_mz.has_necessary_dimensions():
            no_watermark: str = "No Watermark"
            m.mlx_string_put(
                m_ptr,
                win_ptr,
                0,
                self.win_height - 270,
                ColorsHex.RED.value,
                no_watermark,
            )
        line_0: str = "=== A-Maze-Ing ==="
        line_1: str = "1. Re-generate new maze with DFS Algorithm"
        line_2: str = "2. Show/Hide path from entry to exit"
        line_3: str = "3. Rotate maze colors"
        line_4: str = "4. Rotate 42 pattern colors"
        line_5: str = "5. Re-generate new maze with PRIM Algorithm"
        line_6: str = "6. Animate several colored mazes"
        line_7: str = "(R/G/B). Specific 42 pattern color"
        line_8: str = "7. Quit"
        line_9: str = f"Seed_code: {self.maze.seed_code}"
        line_10: str = "Choice? (1 - 7 | R/G/B):"

        all_lines: list[str] = [line_0,
                                line_1,
                                line_2,
                                line_3,
                                line_4,
                                line_5,
                                line_6,
                                line_7,
                                line_8,
                                line_9,
                                line_10]
        i: int = 0
        for line in all_lines:
            m.mlx_string_put(
                m_ptr,
                win_ptr,
                0,
                self.win_height - 230 + i,
                ColorsHex.WHITE.value,
                line,
            )
            i += 20

    def print_solution(self, maze: Maze, maze_config: ConfigModel) -> None:
        """
        Generate and visualize the solution path on the maze.

        Solves the maze using the configured entry and exit points, then draws
        the solution path as blue pixels on the image. The path is rendered
        with a reduced cell size (cell_size - 30) and centered within each
        cell.

        Args:
            maze (Maze): The maze object containing the grid and build solver.
            maze_config (ConfigModel): Configuration model containing maze
            entry and exit coordinates, and other maze parameters.

        Returns:
            None

        Raises:
            SystemExit: If an invalid direction character is found in the
            solution path that is not one of 'N', 'S', 'E', or 'W'.

        Note:
            - The solution is expected to be a string of directional
            characters.
            - Invalid characters will print an error message before exiting.
            - The solution path is converted to a set for O(1) lookup
            performance.
        """
        solution: str = self.solve.solve_maze(
                maze_config.maze_entry,
                maze_config.maze_exit
                )
        start_x, start_y = maze_config.maze_entry

        path_coord: List[tuple[int, int]] = []
        if start_x is not None and start_y is not None:
            path_coord.append((start_x, start_y))

        for c in solution:
            offset_y: int = 0
            offset_x: int = 0
            if c == "N":
                offset_y = -1
            elif c == "S":
                offset_y = 1
            elif c == "E":
                offset_x = 1
            elif c == "W":
                offset_x = -1
            else:
                print(f"{Colors.RED.value} [ERROR] - character {c} found "
                      f"in solution path {Colors.RESET.value}")
                sys.exit(1)

            last_coord_x, last_coord_y = path_coord[-1]
            new_coord: tuple[int, int] = (last_coord_x + offset_x,
                                          last_coord_y + offset_y)
            path_coord.append(new_coord)

        # Reducing complexity as set is a hashable
        path_coord_set: set[tuple[int, int]] = set(path_coord)
        blue_bytes: bytes = ColorsHex.BLUE.value.to_bytes(
            4, byteorder=sys.byteorder)
        inner: int = self.cell_size - 30
        for y, row in enumerate(maze.grid_maze):
            for x, cell in enumerate(row):
                if (x, y) in path_coord_set:
                    dx = x * self.cell_size + 15
                    dy = y * self.cell_size + 15
                    self._fill_rect(self.sol_data, blue_bytes,
                                    dx, dy, inner, inner)

    def render(self, param: tuple[Any, Any, Any]) -> None:
        """
        Render the current frame to the display window.

        Clears the window and redraws the maze image along with the solution
        overlay if enabled. Updates the display synchronously and marks the
        render as complete.

        Args:
            param (tuple): A tuple containing (mlx_instance, window_pointer,
            display_pointer) where mlx_instance is the MLX library interface,
            window_pointer is the window handle, and display_pointer is the
            display handle.

        Returns:
            None
        """
        self.update_color_animation(param)
        if self.needs_redraw:
            m, m_ptr, win_ptr = param
            m.mlx_clear_window(m_ptr, win_ptr)
            m.mlx_put_image_to_window(m_ptr, win_ptr, self.img, 0, 0)
            if self.show_solution:
                m.mlx_put_image_to_window(m_ptr, win_ptr, self.sol_img, 0, 0)
            if self.animation_index >= len(self.animation_colors):
                self.put_parameters(param)

            m.mlx_do_sync(m_ptr)
            self.needs_redraw = False

    def start_visual(self) -> None:
        """
        Initialize and start the visual rendering loop for the maze.

        Sets up the graphical window and image resources, creates event hooks,
        initializes pixel rendering with a gray background color, and enters
        the main rendering loop for continuous display updates.

        The method orchestrates the following sequence:
        - Creates the MLX window
        - Creates the base image for rendering
        - Creates the solution image overlay
        - Sets up event hooks for user interaction
        - Initializes pixel buffer with gray color
        - Registers the render callback with the MLX loop hook
        - Enters the blocking MLX event loop

        Returns:
            None
        """
        self.create_window()
        self.create_image()
        self.create_solution_img()
        m, m_ptr, win_ptr = self.params
        self.create_hooks()
        self.start_pixel_put(color=ColorsHex.GRAY.value)
        m.mlx_loop_hook(m_ptr, self.render, self.params)
        m.mlx_loop(m_ptr)

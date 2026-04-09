import pytest
from unittest.mock import Mock, patch
import sys
from a_maze_ing import ft_make_maze, export_maze_to_file
from src.config.enums import PrintMode
from src.parser.config_model import ConfigModel


@pytest.fixture
def mock_config():
    """
    Create a mock ConfigModel instance for testing purposes.

    Returns:
        Mock: A Mock object configured with test maze parameters:
            - maze_width (int): Width of the maze set to 10
            - maze_height (int): Height of the maze set to 10
            - maze_entry (tuple): Entry point coordinates at (0, 0)
            - maze_exit (tuple): Exit point coordinates at (9, 9)
            - maze_perfect (bool): Flag indicating a perfect maze, set to True
            - maze_print_mode (str): Print mode set to ASCII value
    """
    config = Mock(spec=ConfigModel)
    config.maze_width = 10
    config.maze_height = 10
    config.maze_entry = (0, 0)
    config.maze_exit = (9, 9)
    config.maze_perfect = True
    config.maze_print_mode = PrintMode.ASCII.value
    config.maze_seed = ""
    return config


@pytest.fixture
def mock_maze():
    """
    Create a mock maze object for testing purposes.

    Returns a Mock object configured with the attributes required by the
    current architecture.

    Returns:
        Mock: A configured mock maze object with predefined behavior for
        testing.
    """
    maze = Mock()
    maze.grid_maze = []
    maze.seed_code = 1234
    maze.solve_maze_seed = ""
    return maze


@patch('a_maze_ing.MazePainter_ascii')
@patch('a_maze_ing.export_maze_to_file')
@patch('a_maze_ing.SolveMaze')
@patch('a_maze_ing.MazeGenerator')
@patch('a_maze_ing.Maze')
@patch('a_maze_ing.ft_parsing_config')
def test_ft_make_maze_ascii_mode(mock_parsing,
                                 mock_maze_class,
                                 mock_generator_class,
                                 mock_solver_class,
                                 mock_export,
                                 mock_painter_ascii,
                                 mock_config, mock_maze):
    """
    Test that ft_make_maze correctly processes ASCII mode maze generation.

    Verifies that when ft_make_maze is called with a config file argument,
    it properly:
    - Parses the configuration file
    - Instantiates a Maze object with correct dimensions
    - Builds a perfect maze
    - Exports the maze
    - Starts ASCII visual rendering

    Uses mocks for parsing, maze class, export functionality, ASCII painter,
    config object, and maze instance to isolate the function's behavior.
    """
    mock_parsing.return_value = mock_config
    mock_maze_class.return_value = mock_maze
    mock_generator_instance = Mock()
    mock_generator_class.return_value = mock_generator_instance
    mock_solver_instance = Mock()
    mock_solver_instance.solve_maze.return_value = "NSEW"
    mock_solver_class.return_value = mock_solver_instance
    mock_painter_instance = Mock()
    mock_painter_ascii.return_value = mock_painter_instance

    sys.argv = ['prog', 'config.json']
    ft_make_maze()

    mock_parsing.assert_called_once_with('config.json')
    mock_maze_class.assert_called_once_with(mock_config)
    mock_generator_instance.perfect_maze.assert_called_once_with(
        (0, 0), (9, 9), True
    )
    mock_solver_instance.solve_maze.assert_called_once_with((0, 0), (9, 9))
    mock_export.assert_called_once()
    mock_painter_instance.start_visual.assert_called_once()


@patch('a_maze_ing.MazePainter_mlx')
@patch('a_maze_ing.export_maze_to_file')
@patch('a_maze_ing.SolveMaze')
@patch('a_maze_ing.MazeGenerator')
@patch('a_maze_ing.Maze')
@patch('a_maze_ing.ft_parsing_config')
def test_ft_make_maze_mlx_mode(mock_parsing,
                               mock_maze_class,
                               mock_generator_class,
                               mock_solver_class,
                               mock_export,
                               mock_painter_mlx,
                               mock_config,
                               mock_maze):
    """
    Test that ft_make_maze correctly initializes and uses the MLX painter in
    visual mode.
    This test verifies that when the maze print mode is set to MLX, the
    ft_make_maze function:
    - Parses the configuration from command-line arguments
    - Creates a maze instance
    - Instantiates the MLX painter
    - Calls start_visual() exactly once to begin the visual rendering
    Args:
        mock_parsing: Mock for the argument parsing function
        mock_maze_class: Mock for the Maze class constructor
        mock_export: Mock for the export functionality
        mock_painter_mlx: Mock for the MLX painter class
        mock_config: Mock configuration object with maze_print_mode attribute
        mock_maze: Mock maze instance
    Returns:
        None
    Raises:
        AssertionError: If start_visual() is not called exactly once on the
        painter instance
    """
    mock_config.maze_print_mode = PrintMode.MLX.value
    mock_parsing.return_value = mock_config
    mock_maze_class.return_value = mock_maze
    mock_generator_class.return_value = Mock()
    mock_solver_instance = Mock()
    mock_solver_instance.solve_maze.return_value = "NSEW"
    mock_solver_class.return_value = mock_solver_instance
    mock_painter_instance = Mock()
    mock_painter_mlx.return_value = mock_painter_instance

    sys.argv = ['prog', 'config.json']
    ft_make_maze()

    mock_painter_instance.start_visual.assert_called_once()


@patch('a_maze_ing.ft_parsing_config')
@patch('a_maze_ing.MazeGenerator')
@patch('a_maze_ing.SolveMaze')
@patch('a_maze_ing.MazePainter_ascii')
def test_ft_make_maze_calls_perfect_maze(mock_ascii_painter,
                                         mock_solver_class,
                                         mock_generator_class,
                                         mock_parsing,
                                         mock_config,
                                         mock_maze):
    """
    Test that ft_make_maze correctly calls the perfect_maze method with
    expected parameters.

    Verifies that when ft_make_maze is invoked with a config file argument,
    it instantiates a Maze object and calls its build.perfect_maze method
    with the correct starting position (0, 0), ending position (9, 9),
    and bias flag set to True.

    Args:
        mock_parsing: Mock object for configuration parsing function
        mock_config: Mock configuration object returned by parsing
        mock_maze: Mock Maze instance

    Asserts:
        - perfect_maze method is called exactly once
        - perfect_maze is called with parameters: (0, 0), (9, 9), True
    """
    mock_parsing.return_value = mock_config
    mock_generator_instance = Mock()
    mock_generator_class.return_value = mock_generator_instance
    mock_solver_instance = Mock()
    mock_solver_instance.solve_maze.return_value = "NSEW"
    mock_solver_class.return_value = mock_solver_instance
    mock_ascii_painter.return_value = Mock()

    with patch('a_maze_ing.Maze', return_value=mock_maze):
        with patch('a_maze_ing.export_maze_to_file'):
            sys.argv = ['prog', 'config.json']
            ft_make_maze()

    mock_generator_instance.perfect_maze.assert_called_once_with(
        (0, 0), (9, 9), True
    )


@patch('a_maze_ing.ft_parsing_config')
@patch('a_maze_ing.MazeGenerator')
@patch('a_maze_ing.SolveMaze')
@patch('a_maze_ing.MazePainter_ascii')
def test_ft_make_maze_calls_solve_maze(mock_ascii_painter,
                                       mock_solver_class,
                                       mock_generator_class,
                                       mock_parsing,
                                       mock_config,
                                       mock_maze):
    """
    Test that ft_make_maze calls the solve_maze method with the correct start
    and end coordinates.
    This test verifies that when ft_make_maze is executed with a valid config
    file,
    it properly initializes a Maze object and calls its build.solve_maze method
    with the expected maze start position (0, 0) and end position (9, 9).
    Args:
        mock_parsing: Mock object for parsing configuration.
        mock_config: Mock configuration object returned by the parser.
        mock_maze: Mock Maze object instance.
    Validates:
        - The parsing function returns the mocked config.
        - The Maze class is instantiated.
        - The export_maze_to_file function is called (but not checked in
        detail).
        - solve_maze is called exactly once with start coordinates (0, 0) and
        end coordinates (9, 9).
    """

    mock_parsing.return_value = mock_config
    mock_generator_class.return_value = Mock()
    mock_solver_instance = Mock()
    mock_solver_instance.solve_maze.return_value = "NSEW"
    mock_solver_class.return_value = mock_solver_instance
    mock_ascii_painter.return_value = Mock()

    with patch('a_maze_ing.Maze', return_value=mock_maze):
        with patch('a_maze_ing.export_maze_to_file'):
            sys.argv = ['prog', 'config.json']
            ft_make_maze()

    mock_solver_instance.solve_maze.assert_called_once_with((0, 0), (9, 9))


@patch('a_maze_ing.SeedFile')
def test_export_maze_to_file(mock_seed_file_class, mock_config, mock_maze):
    """
    Test that export_maze_to_file correctly generates and exports a maze seed.
    Tests the integration between maze generation and export functionality by:
    - Mocking the maze object to return a predefined seed pattern
    - Verifying that generate_seed is called exactly once
    - Verifying that export_seed is called once with the correct parameters:
        the generated seed, movement directions string ("UDLR"), and config
        object
    Args:
            mock_parsing: Mocked parsing module
            mock_maze_class: Mocked Maze class
            mock_export: Mocked export functionality
            mock_config: Mocked configuration object
            mock_maze: Mocked maze instance
    """

    mock_seed_instance = Mock()
    mock_seed_instance.generate_seed.return_value = [["F", "C"], ["8", "0"]]
    mock_seed_file_class.return_value = mock_seed_instance

    export_maze_to_file(mock_maze, "UDLR", mock_config)

    assert mock_seed_file_class.call_count == 2
    mock_seed_instance.generate_seed.assert_called_once()
    mock_seed_instance.export_seed.assert_called_once_with(
        [["F", "C"], ["8", "0"]],
        "UDLR",
        mock_config,
    )


@patch('a_maze_ing.Seed')
@patch('a_maze_ing.ft_parsing_config')
def test_ft_make_maze_seed_mode(mock_parsing, mock_seed_class, mock_config):
    """
    Test that ft_make_maze uses the Seed path when maze_seed is set.

    Verifies that when a config has maze_seed set to a non-empty value,
    ft_make_maze instantiates Seed and calls create_grid_from_seed().
    """
    mock_config.maze_seed = "output/seed1.txt"
    mock_parsing.return_value = mock_config
    mock_seed_instance = Mock()
    mock_seed_class.return_value = mock_seed_instance

    sys.argv = ['prog', 'config.json']
    ft_make_maze()

    mock_seed_class.assert_called_once_with(mock_config)
    mock_seed_instance.create_grid_from_seed.assert_called_once()

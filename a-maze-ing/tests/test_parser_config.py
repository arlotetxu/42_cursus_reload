import pytest
from unittest.mock import mock_open, patch, MagicMock
from src.parser.ft_parser_config import ft_parsing_config
from src.parser.config_model import ConfigModel


class TestFtParsingConfig:
    """
    Test suite for the ft_parsing_config function.
    This test class validates the configuration file parsing functionality,
    including valid configurations, error handling, data type conversions,
    and edge cases such as whitespace trimming and comment skipping.
    Tests cover:
    - Valid configuration file parsing and ConfigModel instantiation
    - Default behavior when config file path is empty
    - Error handling for missing files with appropriate exit codes
    - Type validation for configuration parameters (WIDTH, HEIGHT)
    - Format validation for coordinate parameters (ENTRY, EXIT)
    - Pydantic validation error handling for invalid values
    - Correct parsing of key=value format
    - Case conversion for PRINT_MODE parameter
    - Skipping of malformed lines without equals signs
    - Whitespace trimming around keys and values
    """

    def test_valid_config_file(self, tmp_path):
        """
        Test that a valid configuration file is correctly parsed into a
        ConfigModel.
        This test verifies that the ft_parsing_config function properly reads
        and parses a configuration file containing maze parameters (width,
        height, entry point, exit point,
        perfect maze flag, output file, and print mode), and returns a
        ConfigModel instance with all attributes correctly set to their
        expected values.
        Args:
            tmp_path: pytest fixture providing a temporary directory for test
            file creation.
        Raises:
            AssertionError: If the parsed result is not a ConfigModel instance
            or if any of the configuration values do not match the expected
            values.
        """

        config_file = tmp_path / "config.txt"
        config_content = (
            "WIDTH=10\n"
            "HEIGHT=8\n"
            "ENTRY=1,1\n"
            "EXIT=9,7\n"
            "PERFECT=True\n"
            "OUTPUT_FILE=maze.txt\n"
            "PRINT_MODE=mlx"
        )
        config_file.write_text(config_content)

        result = ft_parsing_config(str(config_file))
        assert isinstance(result, ConfigModel)
        assert result.maze_width == 10
        assert result.maze_height == 8
        assert result.maze_entry == (1, 1)
        assert result.maze_exit == (9, 7)

    def test_empty_config_file_path(self, tmp_path):
        """
        Test that ft_parsing_config handles an empty config file path
        correctly.
        This test verifies that when an empty string is passed as the config
        file path, the function still attempts to parse configuration and the
        ConfigModel is instantiated exactly once. The test mocks the file
        opening operation to return predefined WIDTH and HEIGHT values, and
        ensures that ConfigModel is called with the appropriate parameters.
        Args:
            tmp_path: pytest fixture providing a temporary directory unique to
            the test.
        """

        with patch(
            "builtins.open",
            mock_open(
                read_data=(
                    "WIDTH=5\nHEIGHT=5\nENTRY=0,0\nEXIT=4,4\n"
                    "PERFECT=True\nOUTPUT_FILE=maze.txt\nPRINT_MODE=ascii"
                )
            ),
        ):
            with (patch("src.parser.ft_parser_config.ConfigModel") as
                  mock_model):
                mock_model.return_value = MagicMock(spec=ConfigModel)
                ft_parsing_config("")
                # Verify open was called with config.txt
                mock_model.assert_called_once()

    def test_file_not_found(self, capsys):
        """
        Test that ft_parsing_config exits with code 1 when config file is not
        found.
        Verifies that when ft_parsing_config is called with a non-existent
        file path, it raises SystemExit with exit code 1 and outputs an error
        message containing "[ERROR]" to stdout.
        Args:
            capsys: pytest fixture to capture stdout and stderr output.
        """

        with pytest.raises(SystemExit) as exc_info:
            ft_parsing_config("/nonexistent/path/config.txt")
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "[ERROR]" in captured.out

    def test_invalid_width_type(self, tmp_path, capsys):
        """
        Test that the parser correctly handles invalid WIDTH type in config
        file.
        Verifies that when a config file contains a WIDTH parameter with a
        non-numeric value,
        the parser exits with code 1 and outputs an error message containing
        "[ERROR]".
        Args:
            tmp_path: pytest fixture providing a temporary directory for test
            files
            capsys: pytest fixture for capturing stdout/stderr output
        Raises:
            AssertionError: If the function doesn't exit with code 1 or
            doesn't output "[ERROR]"
        """

        config_file = tmp_path / "config.txt"
        config_file.write_text("WIDTH=invalid")

        with pytest.raises(SystemExit) as exc_info:
            ft_parsing_config(str(config_file))
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "[ERROR]" in captured.out

    def test_invalid_entry_format(self, tmp_path, capsys):
        """
        Test that an invalid entry format in the configuration file causes the
        parser to exit with code 1.

        This test verifies that when the ENTRY parameter in a configuration
        file contains an invalid format (not a valid coordinate pair), the
        ft_parsing_config function properly validates the input and exits with
        status code 1.

        Args:
            tmp_path: pytest fixture that provides a temporary directory for
            test files
            capsys: pytest fixture for capturing standard output and error
            streams

        Raises:
            AssertionError: If the SystemExit code is not 1
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text("WIDTH=10\nHEIGHT=10\nENTRY=invalid")

        with pytest.raises(SystemExit) as exc_info:
            ft_parsing_config(str(config_file))
        assert exc_info.value.code == 1

    def test_pydantic_validation_error(self, tmp_path, capsys):
        """
        Test that ft_parsing_config properly handles pydantic validation
        errors.

        Verifies that when a config file contains invalid values (e.g.,
        negative WIDTH),
        the function raises SystemExit with code 1.

        Args:
            tmp_path: pytest fixture providing a temporary directory
            capsys: pytest fixture for capturing stdout/stderr

        Raises:
            AssertionError: if SystemExit is not raised or exit code is not 1
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text("WIDTH=-5\nHEIGHT=10")

        with pytest.raises(SystemExit) as exc_info:
            ft_parsing_config(str(config_file))
        assert exc_info.value.code == 1

    def test_key_value_parsing(self, tmp_path):
        """
        Test parsing of key-value pairs from a configuration file.

        Verifies that the ft_parsing_config function correctly reads and parses
        configuration parameters (WIDTH, HEIGHT, OUTPUT_FILE) from a text file
        and returns an object with the expected attributes (maze_width,
        maze_height,
        maze_output) set to their corresponding values.

        Args:
            tmp_path: pytest fixture providing a temporary directory path.
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text(
            "WIDTH=12\nHEIGHT=9\nENTRY=0,0\nEXIT=11,8\n"
            "PERFECT=True\nOUTPUT_FILE=output.txt\nPRINT_MODE=ascii"
        )

        result = ft_parsing_config(str(config_file))
        assert result.maze_width == 12
        assert result.maze_height == 9
        assert result.maze_output == "output.txt"

    def test_print_mode_uppercase_conversion(self, tmp_path):
        """
        Test that the print mode configuration value is converted to uppercase.

        Verifies that a valid lowercase mode value is converted to uppercase,
        resulting in result.maze_print_mode == "ASCII".
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text(
            "WIDTH=10\nHEIGHT=10\nENTRY=0,0\nEXIT=9,9\n"
            "PERFECT=True\nOUTPUT_FILE=maze.txt\nPRINT_MODE=ascii"
        )

        result = ft_parsing_config(str(config_file))
        assert result.maze_print_mode == "ASCII"

    def test_skip_lines_without_equals(self, tmp_path):
        """
        Test that the parser skips lines without an equals sign.

        Verifies that the configuration parser correctly:
        - Ignores comment lines starting with '#'
        - Parses valid key=value pairs (WIDTH, HEIGHT)
        - Skips malformed lines that don't contain an equals sign
        - Returns a config object with the correct parsed values

        This ensures robustness of the parser when encountering invalid or
        incomplete
        configuration entries.
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text(
            "# Comment line\nWIDTH=10\nHEIGHT=8\nENTRY=0,0\nEXIT=9,7\n"
            "PERFECT=True\nOUTPUT_FILE=maze.txt\nPRINT_MODE=ascii\n"
            "Invalidline"
        )

        result = ft_parsing_config(str(config_file))
        assert result.maze_width == 10
        assert result.maze_height == 8

    def test_whitespace_trimming(self, tmp_path):
        """
        Test that the configuration parser correctly trims whitespace from
        keys and values.

        Verifies that a config file with extra whitespace around the equals
        sign and parameter values is parsed correctly, with all whitespace
        properly removed.

        Args:
            tmp_path: pytest fixture providing a temporary directory for test
            files.
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text(
            "  WIDTH  =  10  \n  HEIGHT  =  8  \n"
            " ENTRY = 0,0 \n EXIT = 9,7 \n PERFECT = True \n"
            " OUTPUT_FILE = maze.txt \n PRINT_MODE = ascii "
        )

        result = ft_parsing_config(str(config_file))
        assert result.maze_width == 10
        assert result.maze_height == 8

    def test_config_without_seed_defaults_to_empty(self, tmp_path):
        """
        Test that configs without a SEED key produce maze_seed == "".

        Verifies that when no SEED entry is present in the configuration file,
        the resulting ConfigModel has maze_seed set to the empty string (the
        default), rather than raising a validation error.
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text(
            "WIDTH=10\nHEIGHT=8\nENTRY=0,0\nEXIT=9,7\n"
            "PERFECT=True\nOUTPUT_FILE=maze.txt\nPRINT_MODE=mlx"
        )

        result = ft_parsing_config(str(config_file))
        assert isinstance(result, ConfigModel)
        assert result.maze_seed == ""

    def test_config_with_seed_is_parsed(self, tmp_path):
        """
        Test that a SEED entry in the config file is correctly parsed.

        Verifies that when a SEED key is present in the configuration file,
        the resulting ConfigModel has maze_seed set to the provided value.
        """
        config_file = tmp_path / "config.txt"
        config_file.write_text(
            "WIDTH=10\nHEIGHT=8\nENTRY=0,0\nEXIT=9,7\n"
            "PERFECT=True\nOUTPUT_FILE=maze.txt\nPRINT_MODE=mlx\n"
            "SEED=output/seed1.txt"
        )

        result = ft_parsing_config(str(config_file))
        assert isinstance(result, ConfigModel)
        assert result.maze_seed == "output/seed1.txt"

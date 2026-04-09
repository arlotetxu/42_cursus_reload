
define HEADER

   ░███            ░███     ░███    ░███    ░█████████ ░██████████         ░██████░███    ░██   ░██████
  ░██░██           ░████   ░████   ░██░██         ░██  ░██                   ░██  ░████   ░██  ░██   ░██
 ░██  ░██          ░██░██ ░██░██  ░██  ░██       ░██   ░██                   ░██  ░██░██  ░██ ░██
░█████████ ░██████ ░██ ░████ ░██ ░█████████    ░███    ░█████████  ░██████   ░██  ░██ ░██ ░██ ░██  █████
░██    ░██         ░██  ░██  ░██ ░██    ░██   ░██      ░██                   ░██  ░██  ░██░██ ░██     ██
░██    ░██         ░██       ░██ ░██    ░██  ░██       ░██                   ░██  ░██   ░████  ░██  ░███
░██    ░██         ░██       ░██ ░██    ░██ ░█████████ ░██████████         ░██████░██    ░███   ░█████░█



endef
export HEADER

# ===============================DEFINITIONS===============================
DEF_COLOR   = \033[0;39m
GRAY        = \033[0;90m
RED         = \033[0;31m
GREEN       = \033[0;92m
YELLOW      = \033[0;93m
BLUE        = \033[0;94m
MAGENTA     = \033[0;95m
CYAN        = \033[0;96m
WHITE       = \033[0;97m

MAIN_FILE = a_maze_ing.py
SRC = src/

all: install run

install: pyproject.toml
	@echo "$(YELLOW)Installing dependencies with uv...$(DEF_COLOR)"
	@uv sync
	@echo "$(GREEN)Dependencies installed!!$(DEF_COLOR)"

run: install
	@echo "$(CYAN)$$HEADER$(DEF_COLOR)"
	uv run a_maze_ing.py config.txt

debug: install
	@echo "$(YELLOW)Entering debugging mode...$(DEF_COLOR)"
	uv run python3 -m pdb -c continue a_maze_ing.py config.txt

clean:
	@echo "$(YELLOW)\nRemoving __pycache__ directories...$(DEF_COLOR)"
	@find . -type d -name "*pycache*" -exec rm -rf {} +
	@echo "$(YELLOW)Removing .ruff_cache directories...$(DEF_COLOR)"
	@find . -type d -name ".ruff_cache" -exec rm -rf {} +
	@echo "$(YELLOW)Removing .mypy__cache directories...$(DEF_COLOR)"
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +
	@find . -type d -name ".mypy__cache" -exec rm -rf {} +
	@echo "$(YELLOW)Removing .pytest_cache directories...$(DEF_COLOR)"
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type d -name "*egg-info" -exec rm -rf {} +
	@echo "$(GREEN)Clean process completed!!$(DEF_COLOR)"

flake8:
	@echo "$(YELLOW)\nChecking with flake8...$(DEF_COLOR)"
	-@uv run flake8 $(MAIN_FILE) $(SRC)
	@echo "$(GREEN)Flake8 completed!!$(DEF_COLOR)"

mypy:
	@echo "$(YELLOW)Checking mypy...$(DEF_COLOR)"
	-@uv run mypy $(MAIN_FILE) $(SRC) --warn-return-any --warn-unused-ignores \
	--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs \
	--follow-imports=silent
	@echo "$(GREEN)mypy completed!!$(DEF_COLOR)"

lint: clean flake8 mypy

lint-strict: clean
	@echo "$(YELLOW)Checking with flake8 and mypy --strict...$(DEF_COLOR)"
	@flake8_status=0; mypy_status=0; \
	uv run flake8 $(MAIN_FILE) $(SRC) || flake8_status=1; \
	uv run mypy $(MAIN_FILE) $(SRC) --strict --follow-imports=silent || mypy_status=1; \
	if [ $$flake8_status -eq 1 ]; then echo "$(RED)flake8 failed$(DEF_COLOR)"; fi; \
	if [ $$mypy_status -eq 1 ]; then echo "$(RED)mypy failed$(DEF_COLOR)"; fi; \
	if [ $$flake8_status -eq 1 ] || [ $$mypy_status -eq 1 ]; then exit 1; fi; \
	echo "$(GREEN)Lint-strict passed!!$(DEF_COLOR)"

.PHONY: all run clean lint lint-strict

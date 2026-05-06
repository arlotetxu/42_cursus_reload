
define HEADER

 .---.   .--.  .-.   .-.      .-.   .-..----.   .-.   .-.  .--..-.  .-..----. .----.
/  ___} / {} \ | |   | |      |  `.'  || {_     |  `.'  | / {} \\ \/ / | {}  }| {_
\     }/  /\  \| `--.| `--.   | |\ /| || {__    | |\ /| |/  /\  \}  {  | {}  }| {__
 `---' `-'  `-'`----'`----'   `-' ` `-'`----'   `-' ` `-'`-'  `-'`--'  `----' `----'


              _              _
            .|:|oooooooooooo|:|.
         d888|:|888888888888|:|888b
       d88888|:|888888888888|:|88888b
     d88888888\:\8888888888/:/88888888b
   d8888888888"|:|""""""""|:|"8888888888b
  d888888888"  |:|        |:|  "888888888b
 d888888888    |:|________|:|    888888888b
d8888888888b  .d888888888888b.  d8888888888b
d888888888b") 8888888888888888 ("d888888888b
d888888b".-'8888888888888888888b`-."d888888b
 d88"_.-' d88888b"'______`"d88888b `-._"88b\\
  `-'    d888b" .-' _   _`-. "d888b    `-' \\
        d88b" .' _ (3) (2) _`. "d88b       //
        88/  /  (4)       (1)_\  \88       \\
        88| |  _    .d8b. ==' `| |88       //
        88| | (5)   88888  (O) | |88      //
        88| |   _   "d8b"  _   | |88      \\
       .88\  \ (6)  _   _ (9) /  /88.     //
       d888b. `.   (7) (8)  .' .d888b     \\
      d888888b. `-.______.-' .d888888b    //
     88888888888q.________.p88888888888 _//
    888888888888888888888888888888888888-'
   d888888888888888888888888888888888888b
   00000000000000000000000000000000000000


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

MAIN_FILE = src/__main__.py
SRC = src/

all: install run

install: pyproject.toml
	@echo "$(YELLOW)Installing dependencies with uv...$(DEF_COLOR)"
	@uv sync
	@echo "$(GREEN)Dependencies installed!!$(DEF_COLOR)"

run: install
	@echo "$(YELLOW)$$HEADER$(DEF_COLOR)"
	uv run python -m src

debug: install
	@echo "$(YELLOW)Entering debugging mode...$(DEF_COLOR)"
	uv run python3 -m pdb -c continue $(MAIN_FILE)

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
	-@uv run flake8 $(SRC)
	@echo "$(GREEN)Flake8 completed!!$(DEF_COLOR)"

mypy:
	@echo "$(YELLOW)Checking mypy...$(DEF_COLOR)"
	-@uv run mypy $(SRC) --warn-return-any --warn-unused-ignores \
	--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs \
	--follow-imports=silent
	@echo "$(GREEN)mypy completed!!$(DEF_COLOR)"

lint: clean flake8 mypy

lint-strict: clean
	@echo "$(YELLOW)Checking with flake8 and mypy --strict...$(DEF_COLOR)"
	@flake8_status=0; mypy_status=0; \
	uv run flake8 $(SRC) || flake8_status=1; \
	uv run mypy $(SRC) --strict --follow-imports=silent || mypy_status=1; \
	if [ $$flake8_status -eq 1 ]; then echo "$(RED)flake8 failed$(DEF_COLOR)"; fi; \
	if [ $$mypy_status -eq 1 ]; then echo "$(RED)mypy failed$(DEF_COLOR)"; fi; \
	if [ $$flake8_status -eq 1 ] || [ $$mypy_status -eq 1 ]; then exit 1; fi; \
	echo "$(GREEN)Lint-strict passed!!$(DEF_COLOR)"

.PHONY: all run clean lint lint-strict

*This project has been created as part of the 42 curriculum by arlo.*

# Call Me Maybe

## Description
`call-me-maybe` is a function-calling engine designed to accurately extract structured data from natural language queries using a lightweight Large Language Model (LLM). The primary goal of this project is to force a small LLM to output perfectly valid JSON matching specific function signatures (like parameters and function names) by intercepting and altering its thought process mathematically.

By utilizing constrained decoding techniques, the program eliminates the hallucination and formatting errors commonly found in small-parameter models, guaranteeing reliable data extraction.

## Instructions

### Prerequisites
- Python `^3.10` (as defined in `pyproject.toml`)
- `uv` package manager installed.

### Installation
To install the project dependencies and set up the environment, run:
```bash
make install
```

### Execution
You can execute the program with the default parameters using the Makefile:
```bash
make run
```

Alternatively, you can run it manually and specify custom paths for the function definitions, the input prompts, and the output file:
```bash
uv run python -m src \
    --functions_definition data/input/functions_definition.json \
    --input data/input/function_calling_tests.json \
    --output data/output/function_calling_results.json
```

## Example Usage

**Input Prompt:**
`"What is the sum of 4 and 2?"`

**Execution:**
```bash
make run
```

**Output Generated (JSON):**
```json
[
    {
        "prompt": "What is the sum of 4 and 2?",
        "name": "fn_add_numbers",
        "parameters": {
            "a": 4.0,
            "b": 2.0
        }
    }
]
```

## Algorithm Explanation
This project heavily relies on a technique known as **Constrained Decoding** via **Logit Masking**.

Standard LLMs generate text by assigning probabilities (logits) to every possible token in their vocabulary and picking the highest one. In this project, right before the model selects its next token, the engine intercepts the logits array.

Depending on the context (e.g., generating a function name or a numeric parameter), a mask is generated. This mask iterates over the entire vocabulary and sets the probabilities of invalid tokens to `-infinity`.
- **`add_name_mask`**: Allows only tokens that are valid substrings of the provided function names.
- **`add_numeric_mask`**: Restricts the model strictly to digits (`0-9`), commas, closing brackets, and negative signs, dynamically allowing decimals or signs depending on the parsed string state.

By mathematically preventing the model from predicting illegal tokens, it is forced to generate syntactically perfect JSON fields.

## Design Decisions
- **Pydantic Validation**: `pydantic` was chosen to strictly validate the structural integrity of both the input configuration files and the LLM's generated output before writing to the disk.
- **NumPy for Logits Manipulation**: Because LLM vocabularies can contain over 100,000 tokens, iterating and masking them in raw Python is slow. `numpy` arrays (`NDArray`) are used for highly optimized, C-level manipulation of the logit probabilities (`np.full_like`, `np.argmax`).
- **Type Safety**: The project follows strict static typing rules enforced by `mypy --strict`, enhancing maintainability and reducing runtime errors.

## Performance Analysis
- **Accuracy**: The constrained decoding approach guarantees 100% structural accuracy for function names and numeric types, entirely bypassing the model's standard hallucination rates.
- **Speed**: Utilizing `numpy` keeps the overhead of logit masking minimal, allowing the lightweight `Small_LLM_Model` (Qwen3-0.6B) to run efficiently on standard hardware.
- **Reliability**: While highly reliable for structured outputs, the system requires careful mask design to prevent the model from entering infinite loops if the generated string falls into an edge case where no valid tokens make grammatical sense.

## Challenges Faced
- **Infinite Loops in Generation**: When the LLM forgot to output punctuation (like a comma) before jumping to the next field, the strict numeric masks trapped the model into outputting endless streams of zeros or spaces. This was fixed by making the break conditions tolerant to grouped punctuation tokens (e.g., checking if `,` is *in* the token rather than matching it exactly).
- **Mypy Strict Conflicts**: Integrating external libraries (like `pydantic` or the custom `llm_sdk`) without `stubs` caused severe pipeline failures during strict static analysis. This was resolved by properly configuring `MYPYPATH` and using targeted `# type: ignore` directives.

## Testing Strategy
The implementation was validated using a multi-layered approach:
1. **Schema Validation**: Unit testing the JSON structures using `pydantic` models (`FuncDefVal`, `FuncCallVal`, `OutputVal`) to ensure files are read and written flawlessly.
3. **Edge-case Execution**: Running prompts that target vulnerabilities in small models, such as negative numbers, multi-parameter extraction, and complex regex strings, directly testing the effectiveness of the NumPy logit masks.

## Resources
- **How Large Language Models work**: [https://medium.com/data-science-at-microsoft/how-large-language-models-work-91c362f5b78f]
- **Controlling your LLM: Deep dive into Constrained Generation**: [https://medium.com/@docherty/controlling-your-llm-deep-dive-into-constrained-generation-1e561c736a20]

- **AI Usage**: AI assistants (like Gemini/ChatGPT) were utilized during the development process primarily as debugging partners. AI was exclusively used for theoretical explanations and debugging guidance without generating the core architectural code.
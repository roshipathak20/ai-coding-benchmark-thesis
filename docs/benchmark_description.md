# Benchmark Description

This repository contains the benchmark used in the thesis:

"AI-assisted software development".

## Benchmark structure

The benchmark contains 20 tasks:

- 10 implementation tasks
- 10 maintenance tasks

Implementation tasks evaluate the ability of the AI system to generate new code based on a specification.

Maintenance tasks evaluate the ability of the AI system to modify existing code and resolve predefined issues.

## Experimental workflow

Each task follows the same procedure:

1. A structured prompt is provided to the AI assistant.
2. The AI generates a code solution.
3. The generated code is inserted into the solution file.
4. Automated tests are executed using pytest.
5. Results are recorded in `results/results.csv`.

## Evaluation metrics

The following metrics are recorded:

- Pass rate (based on pytest results)
- Time to generate the solution
- Number of attempts
- Presence of hallucinated APIs or imports
- Code quality observation

## Development environment

The benchmark was executed using:

- Visual Studio Code
- Python
- pytest testing framework
- GitHub version control
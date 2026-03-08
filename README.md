# AI Coding Benchmark Thesis

This repository contains the Phase 2 experiment benchmark for evaluating AI-assisted software development.

## Categories
- 10 implementation tasks
- 10 maintenance tasks

## Workflow per task
1. Open the prompt file
2. Paste the prompt into ChatGPT
3. Save the raw AI response in ai_outputs/
4. Paste the generated code into solutions/
5. Run the corresponding pytest file
6. Take screenshots
7. Record the result in results/results.csv

## Screenshot policy
For each task, save:
- one screenshot of prompt/AI answer
- one screenshot of code in VS Code
- one screenshot of pytest result

## Main command
pytest tests/test_IT_1.py -q

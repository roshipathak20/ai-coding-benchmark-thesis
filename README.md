# AI Coding Benchmark Thesis

This repository contains the benchmark implementation and experiment artifacts used in the Bachelor thesis:

**AI in Software Development: Benefits vs Risks**  
Centria University of Applied Sciences  
Bachelor of Information Technology Engineering  
Authors: **Roshani Pathak** and **Sushil Poudel**  
Year: **2026**

This repository supports the empirical evaluation described in the thesis, especially the benchmark-based analysis of AI-assisted software development tasks.

---

## Repository Purpose

The purpose of this repository is to provide a structured benchmark for evaluating how an AI coding assistant performs in realistic software development tasks.

The benchmark was designed to examine both the **benefits** and **risks** of AI-assisted software development. The evaluation focuses on areas such as:

- functional correctness
- number of attempts required
- task completion time
- hallucination occurrence
- code quality
- patch reliability in maintenance tasks

The repository also supports **transparency** and **reproducibility** by preserving prompts, source files, tests, results, and screenshots from the experiment.

---

## Benchmark Categories

The benchmark consists of **40 tasks** divided into five categories:

### 1. Algorithmic Tasks (10)
Structured computational problems used to evaluate logical reasoning and algorithm correctness.

### 2. Implementation Tasks (10)
Tasks that require generating new functionality from a task description.

### 3. Maintenance Tasks (10)
Tasks that require fixing or modifying existing faulty code.

### 4. Library and API Usage Tasks (5)
Tasks that evaluate the correct use of common Python libraries and APIs.

### 5. Code Refactoring Tasks (5)
Tasks that improve code readability and structure without changing behaviour.

---

## Repository Structure

```text
ai-coding-benchmark-thesis/
│
├── docs/
│   Supporting documentation related to the benchmark and thesis
│
├── maintenance_sources/
│   Existing faulty or incomplete source files used in maintenance tasks
│
├── prompts/
│   Natural language prompts used during the benchmark experiment
│
├── results/
│   Benchmark result files, logs, and recorded outcomes
│
├── screenshots/
│   Screenshots of prompts, generated code, and pytest runs
│
├── solutions/
│   AI-generated or completed solution files for benchmark tasks
│
├── tasks/
│   Task descriptions and benchmark task definitions
│
├── tests/
│   Automated pytest files used for validation
│
├── .gitignore
│   Git ignore configuration
│
├── README.md
│   Repository overview and documentation
│
├── bootstrap_phase2.py
│   Script used to create the Phase 2 benchmark structure
│
└── bootstrap_phase2_extra.py
    Additional script used to extend the benchmark structure

# Week 4: Make It Production-Ready

This repository contains the beginner-friendly notebooks and slides used in Week 4. Observe what your application does, measure answer quality, and improve reliability before your final demo.

## The big picture

Application request -> model route -> answer

Langfuse records the execution. Evaluations judge the result. LiteLLM selects a model and handles configured failures. These are separate teaching examples; apply the ideas to your existing project afterwards.

## Learning path

1. [Langfuse](01-langfuse/) — traces, debugging, prompts, scores and experiments.
2. [LiteLLM](02-litellm/) — a common model interface, routing, fallbacks and a local proxy.
3. [Evaluations](03-evals/) — datasets, rules, LLM judges, human review and regressions.
4. [LLMOps wrap-up](04-llmops/) — connect the lessons to running and improving your final product.

Each practical folder contains one notebook, its slides, a detailed guide, pinned requirements and an API-key template.

## Easiest way to run

On GitHub choose **Code → Codespaces → New with options**, then select the lesson's dev container configuration. Setup installs that lesson's environment and named Jupyter kernel. Open its notebook and select **Python (Week 4 langfuse)**, **Python (Week 4 evals)** or **Python (Week 4 litellm)** as appropriate. Codespaces usage follows your GitHub account allowance. Stop the Codespace when finished.

Alternatively, upload a notebook and its requirements file to Colab, or use local Jupyter/VS Code. Run from inside the lesson folder.

## Local Python environments

Install Python 3.12, then from the repository root:

```bash
python3.12 scripts/setup.py
```

Windows: use `py -3.12 scripts/setup.py`. To install one lesson, append its folder name. Setup creates a separate `.venv` in each lesson and registers its kernel. It prints the command to launch Jupyter. Separate environments preserve the notebooks' different OpenAI SDK pins. A combined root requirements file would introduce conflicting versions.

## API keys

All three lessons need your OpenAI API key and model access. Langfuse also needs a project public key, secret key and matching region URL. Copy each lesson's `.env.example` to `.env`. Missing keys are requested privately by the notebook. Never commit credentials or private outputs.

GitHub deployment Environments do not provide notebook runtimes: the runnable GitHub environments here are the three Codespaces dev container configurations. Credentials stay in your private lesson environment files or your own Codespaces secrets.

## Final project practice

- Add tracing to one real workflow and explain a failure using its trace.
- Create a representative evaluation set, include boundary/unsupported questions, and compare a baseline with one change.
- Review correctness, latency and cost together; document any regressions.
- Verify fallback behavior and describe what it cannot handle.
- Submit the final live product, repository/README and a short evidence-based demo.

These notebooks use fictional support policies and small datasets. Results vary and do not establish production readiness. See each lesson guide for cleanup and troubleshooting.

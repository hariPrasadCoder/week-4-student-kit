# Evals: measure answer quality

Build an eight-case dataset, generate baseline answers, combine deterministic checks with a structured LLM judge, review human/judge agreement, and compare a revised prompt for regressions.

## Folder contents

- `Evals_101.ipynb`: guided notebook, run from top to bottom.
- `LLM Evals 101.pdf`: accompanying lesson slides.
- `requirements.txt`: pinned dependencies for this lesson.
- `.env.example`: credential template; copy to private `.env`.

## Before you begin

Use Python 3.12. OpenAI API key with access to the application and judge models. Model calls use your account credits. No keys are included.

From the repository root, run `python scripts/setup.py 03-evals`, then open Jupyter with the command printed by setup. In VS Code select **Python (Week 4 evals)**.

Copy this folder's `.env.example` to `.env` and fill in your own credentials. Start Jupyter in this folder so requirements and environment files resolve correctly. Run each cell in order, inspecting the outputs. Restart the kernel if package installation requests it.

For Colab, upload the notebook and requirements file to the same runtime directory. Use hidden key prompts; never paste keys into code cells. Interactive review cells require your input. The optional Langfuse clipboard step is for a local computer.

## Practice

Fill in the human review labels. Identify one judge disagreement and one regression or improvement, using the actual answers as evidence.

## Troubleshooting and cleanup

If imports fail, confirm the selected kernel belongs to this lesson, rerun setup, then restart the kernel. For authentication errors, check key names, account credit and model access.

Human review labels start as None. Fill them in with True or False before interpreting agreement. Judge scores are fallible; eight cases do not establish production readiness.

Never commit `.env`, keys, or notebook outputs containing private data. Clear outputs before sharing.

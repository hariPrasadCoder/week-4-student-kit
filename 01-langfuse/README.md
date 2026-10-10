# Langfuse: observe and debug

Record a support-bot trace, debug incorrect policy data, inspect latency and errors, version prompts, attach human scores, and run a dataset experiment.

## Folder contents

- `Langfuse_101.ipynb`: guided notebook, run from top to bottom.
- `requirements.txt`: pinned dependencies for this lesson.
- `.env.example`: credential template; copy to private `.env`.

## Before you begin

Use Python 3.12. OpenAI API key and a Langfuse project public/secret key. Set the base URL to your project region. Model calls use your account credits. No keys are included.

From the repository root, run `python scripts/setup.py 01-langfuse`, then open Jupyter with the command printed by setup. In VS Code select **Python (Week 4 langfuse)**.

Copy this folder's `.env.example` to `.env` and fill in your own credentials. Start Jupyter in this folder so requirements and environment files resolve correctly. Run each cell in order, inspecting the outputs. Restart the kernel if package installation requests it.

For Colab, upload the notebook and requirements file to the same runtime directory. Use hidden key prompts; never paste keys into code cells. Interactive review cells require your input. The optional Langfuse clipboard step is for a local computer.

## Practice

Find the wrong-policy trace and explain which step introduced the error. Compare prompt versions on the same questions.

## Troubleshooting and cleanup

If imports fail, confirm the selected kernel belongs to this lesson, rerun setup, then restart the kernel. For authentication errors, check key names, account credit and model access, and that both Langfuse keys match the selected region.

Use a separate demo Langfuse project. This notebook creates traces, prompts, scores and a dataset; remove them in your project when finished. Run flush cells before closing the kernel.

Never commit `.env`, keys, or notebook outputs containing private data. Clear outputs before sharing.

# LiteLLM: route models and handle failures

Call a model through one interface, configure primary and backup routes, simulate failures, start a local proxy, and verify proxy failover using deployment IDs.

## Folder contents

- `LiteLLM_101.ipynb`: guided notebook, run from top to bottom.
- `requirements.txt`: pinned dependencies for this lesson.
- `.env.example`: credential template; copy to private `.env`.

## Before you begin

Use Python 3.12. OpenAI API key with access to both configured models. The proxy needs no database for this lesson. Model calls use your account credits. No keys are included.

From the repository root, run `python scripts/setup.py 02-litellm`, then open Jupyter with the command printed by setup. In VS Code select **Python (Week 4 litellm)**.

Copy this folder's `.env.example` to `.env` and fill in your own credentials. Start Jupyter in this folder so requirements and environment files resolve correctly. Run each cell in order, inspecting the outputs. Restart the kernel if package installation requests it.

For Colab, upload the notebook and requirements file to the same runtime directory. Use hidden key prompts; never paste keys into code cells. Interactive review cells require your input. The optional Langfuse clipboard step is for a local computer.

## Practice

Verify the backup deployment serves each failure scenario. Explain why two models on one provider cannot protect against a provider-wide outage.

## Troubleshooting and cleanup

If imports fail, confirm the selected kernel belongs to this lesson, rerun setup, then restart the kernel. For authentication errors, check key names, account credit and model access.

Run the final cleanup cell to stop the proxy and remove temporary configuration and logs. If interrupted, restart the kernel and stop any leftover demo proxy process. The proxy binds only to localhost.

Never commit `.env`, keys, or notebook outputs containing private data. Clear outputs before sharing.

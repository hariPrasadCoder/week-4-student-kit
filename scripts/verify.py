"""Validate notebook structure, Python syntax and imports without paid API calls."""
import argparse
import ast
import importlib
from pathlib import Path
import nbformat
from IPython.core.interactiveshell import InteractiveShell

p = argparse.ArgumentParser()
p.add_argument('lesson')
a = p.parse_args()
folder = Path(__file__).resolve().parents[1] / a.lesson
for file in folder.glob('*.ipynb'):
    notebook = nbformat.read(file, as_version=4)
    nbformat.validate(notebook)
    modules = set()
    for i, cell in enumerate(notebook.cells):
        if cell.cell_type != 'code':
            continue
        assert not cell.outputs and cell.execution_count is None, 'Clear notebook outputs before publishing'
        source = InteractiveShell.instance().input_transformer_manager.transform_cell(cell.source)
        tree = ast.parse(source, filename=f'{file.name}:cell-{i}')
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(alias.name.split('.')[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])
    for module in sorted(modules):
        importlib.import_module(module)
    print(f'{file.name}: valid schema, clean outputs, compiled cells, imported {len(modules)} modules')
if a.lesson == '01-langfuse':
    from langfuse import get_client, propagate_attributes
    from langfuse.langchain import CallbackHandler
    from langgraph.graph import StateGraph, START, END
    from langchain_openai import ChatOpenAI
elif a.lesson == '03-evals':
    from openai import OpenAI
    assert hasattr(OpenAI, '__init__')
else:
    import litellm
    import litellm.proxy.proxy_cli
    assert callable(litellm.completion)
print('Dependency and API import checks passed; live API calls require your credentials.')

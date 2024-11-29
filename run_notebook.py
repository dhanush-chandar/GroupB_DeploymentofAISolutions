import nbformat
from nbconvert import PythonExporter, ExecutePreprocessor

def run_notebook(input_path, output_path):
    with open(input_path, 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Execute the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(notebook, {'metadata': {'path': '.'}})
    
    # Save the executed notebook
    with open(output_path, 'w') as f:
        nbformat.write(notebook, f)

if __name__ == "__main__":
    run_notebook('model.ipynb', 'executed_model.ipynb')

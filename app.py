import papermill as pm
import argparse
import sys
import os

def run_notebook(input_path, output_path):
    print(f"Running notebook with input={input_path}, output={output_path}...")
    
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        sys.exit(1)

    notebook_path = "bg_remover.ipynb"
    output_notebook = "executed_notebook.ipynb"

    try:
        pm.execute_notebook(
            notebook_path,
            output_notebook,
            parameters=dict(input_path=input_path, output_path=output_path)
        )
        print(f"Notebook executed successfully. Results in {output_notebook}")
    except Exception as e:
        print(f"An error occurred during notebook execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wrapper to run bg_remover.ipynb via papermill.")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("output", help="Path to output video file")
    
    args = parser.parse_args()
    
    run_notebook(args.input, args.output)

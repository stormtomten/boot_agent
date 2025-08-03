import os
import subprocess
import sys

from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute python files with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory. If not provided, returns a file error.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the python file.",
                ),
                description="Optional arguments to pas to the python file.",
            ),
        },
        required=["filepath"],
    ),
)


def run_python_file(working_directory, filepath, args=[]):
    working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, filepath))

    if not os.path.commonpath([working_dir, abs_filepath]) == working_dir:
        return f'Error: Cannot execute "{filepath}" as it is outside the permitted working directory'

    if not os.path.exists(abs_filepath):
        return f'Error: File "{filepath}" not found.'

    _, ext = os.path.splitext(os.path.basename(abs_filepath))
    if not ext == ".py":
        return f'Error: "{filepath}" is not a Python file.'

    try:
        commands = [
            # sys.executable,
            "python",
            abs_filepath,
        ]
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            cwd=working_directory,
            timeout=30,
            check=True,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout.strip()}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr.strip()}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced"

    except Exception as e:
        return f"Error: executing Python file: {e}"

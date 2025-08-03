import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwites content to a file, constrained to the working directory. Creates a new file along with parent directories if they do not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory. If not provided, returns a file error.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write formated as a string.",
            ),
        },
        required=["filepath", "content"],
    ),
)


def write_file(working_directory, filepath, content):
    if not filepath:
        return "Error: no filepath provided"

    working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, filepath))

    if not os.path.commonpath([working_dir, abs_filepath]) == working_dir:
        return f'Error: Cannot write to "{filepath}" as it is outside the permitted working directory'

    if not os.path.exists(abs_filepath):
        try:
            os.makedirs(os.path.dirname(abs_filepath), exist_ok=True)
        except Exception as e:
            return f"Error creating directories: {e}"

    if os.path.exists(abs_filepath) and os.path.isdir(abs_filepath):
        return f'Error: "{filepath}" is a directory, not a file'

    try:
        with open(abs_filepath, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{filepath}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"

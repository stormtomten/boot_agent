import os

from google.genai import types

from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the first {MAX_CHARS} characters from a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory. If not provided, returns a file error.",
            ),
        },
        required=["filepath"],
    ),
)


def get_file_content(working_directory, filepath):
    working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, filepath))

    if not os.path.commonpath([working_dir, abs_filepath]) == working_dir:
        return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_filepath):
        return f'Error: File not found or is not a regular file: "{abs_filepath}"'

    try:
        with open(abs_filepath, "r") as f:
            file_conten_string = f.read(MAX_CHARS)
            if len(file_conten_string) == MAX_CHARS and f.read(1) != "":
                file_conten_string += (
                    f'[...File "{filepath}" truncated at {MAX_CHARS} characters]'
                )
        return file_conten_string

    except Exception as e:
        return f"Error reading file: {e}"

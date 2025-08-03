from functions.get_files_info import get_files_info


def test_file_info():
    working_directory = "calculator"
    directories = [
        ".",
        "pkg",
        "/bin",
        "../",
    ]

    for case in directories:
        result = get_files_info(working_directory, case)
        print(f"Result for '{case}' directory:")
        print(result)
        print("")

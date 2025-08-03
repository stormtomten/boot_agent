from functions.get_file_content import get_file_content


def test_get_content():
    working_directory = "calculator"
    case_files = [
        "main.py",
        "pkg/calculator.py",
        "/bin/cat",
        "pkg/does_not_exist.py",
    ]

    for case in case_files:
        result = get_file_content(working_directory, case)
        print(f"Result for '{case}' file:")
        print(result)
        print("")

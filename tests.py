from file_info_test import test_file_info
from functions.run_python import run_python
from functions.write_file import write_file
from get_content_test import test_get_content
from write_test import test_write


def tests():
    """
    test_file_info()
    test_get_content()
    test_write()
    """

    run_cases = [
        ["calculator", "main.py"],
        ["calculator", "main.py", ["3 + 5"]],
        ["calculator", "tests.py"],
        ["calculator", "../main.py"],
        ["calculator", "nonexistent.py"],
    ]
    print(run_python("calculator", "main.py"))
    print(run_python("calculator", "main.py", ["3 + 5"]))
    print(run_python("calculator", "tests.py"))
    print(run_python("calculator", "../main.py"))
    print(run_python("calculator", "nonexistent.py"))
    print(run_python("calculator", "lorem.txt"))
    print(run_python("calculator", ""))

    print("writeing")
    print(write_file("calculator", "", "nope"))


if __name__ == "__main__":
    tests()

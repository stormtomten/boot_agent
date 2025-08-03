from functions.write_file import write_file


def test_write():
    working_directory = "calculator"

    files = [
        "lorem.txt",
        "pkg/morelorem.txt",
        "/tmp/tmp.txt",
        "",
    ]

    content = [
        "wait, this isn't lorem ipsum",
        "lorem ipsum dolor sit amet",
        "this should not be allowed",
    ]
    for i in range(len(files)):
        result = write_file(working_directory, files[i], content[i])
        print(result)

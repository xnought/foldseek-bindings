import subprocess


def exec(cmd: str | list[str]) -> str:
    return subprocess.check_output(cmd, shell=True).decode()


def parse_output(filepath: str) -> list[list]:
    with open(filepath, "r") as f:
        lines = f.readlines()

        parsed_lines = []
        for line in lines:
            parsed_line = []
            for column in line.strip("\n").split("\t"):
                try:
                    column = float(column)
                except ValueError:
                    pass
                parsed_line.append(column)
            parsed_lines.append(parsed_line)

    return parsed_lines


def easy_search(
    query: str,
    targets: str,
    out_file=".foldseek_cache/output",
    temp_dir=".foldseek_cache",
    print_stdout=False,
    foldseek_executable="foldseek",
) -> list[list]:
    """easy_search just calls foldseek easy-search under the hood
    TODO: use pybind to call the C++ function instead

    Returns:
        list[list]: a list of the matches from the search
    """

    # don't continue unless they actually have foldseek installed
    if exec(f"which {foldseek_executable}") == "":
        raise Exception("foldseek not found in PATH")

    # Then call the easy-search
    cmd = f"{foldseek_executable} easy-search {query} {targets} {out_file} {temp_dir}"
    stdout = exec(cmd)
    if print_stdout:
        print(stdout)

    # parse the text into array of arrays where each column is a data field
    return parse_output(out_file)


if __name__ == "__main__":
    output = easy_search("test_examples/A.pdb", "test_examples")
    print(output)

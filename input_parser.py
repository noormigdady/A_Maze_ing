import sys


def check_keys(config: dict, file: str) -> None:
    if "WIDTH" not in config:
        raise ValueError(f"Width key is missing in the {file} file")
    if "HEIGHT" not in config:
        raise ValueError(f"Height key is missing in the {file} file")
    if "ENTRY" not in config:
        raise ValueError(f"Entry point key is missing in the {file} file")
    if "EXIT" not in config:
        raise ValueError(f"Exit point key is missing in the {file} file")
    if "OUTPUT_FILE" not in config:
        raise ValueError(f"Output_file key is missing in the {file} file")
    if "PERFECT" not in config:
        raise ValueError(f"Perfect key is missing in the {file} file")


def parse_input(file: str) -> None:
    config = {}
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if line[0] == "#":
                    continue
                if "=" not in line:
                    raise ValueError(f"Bad syntax: {line}, "
                                     "should be in the format: KEY=VALUE")
                key, value = line.split("=")
                key.strip()
                value.strip()
                if key in config:
                    print(f"Duplicate valu for {key}")
                    sys.exit(1)
                config[key] = value
    except Exception as ex:
        print(ex)
    try:
        check_keys(config, file)
    except ValueError as ex:
        print(ex)
        sys.exit(1)

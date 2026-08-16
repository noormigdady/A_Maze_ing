import sys
import typing

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


def parsser(key: str, value: typing.Any) -> typing.Any:
    parsed_value = ""
    try:
        if key is any("HEIGHT", "WIDTH"):
            parsed_value = int(value)
        elif key is any("ENTRY", "EXIT"):
            x, y = value.split(",")
            parsed_value = (int(x), int(y))
        elif key == "OUTPUT_FILE":
            file_name = value.split(".")
            if len(file_name) == 2 and file_name[1] == "txt":
                parsed_value = value
            else:
                raise ValueError("Wrong format for OUTPUT_FILE")
        elif key == "PERFECT":
            v = value.lower()
            if v in any("true", "false"):
                parsed_value = v
            else:
                raise ValueError("Wrong value for PERFECT key")
    except Exception as ex:
        print(ex)
    return parsed_value


def parse_input(file: str) -> None:
    config = {}
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if line[0] == "#":
                    continue
                if "=" not in line:
                    raise ValueError(f"Invalid format: {line}, "
                                     "should be in the format: KEY=VALUE")
                key, value = line.split("=")
                if len(line) != 2:
                    raise ValueError(f"Invalid format: {line}, Should be: KEY=VALUE")
                key.strip()
                value.strip()
                if key in config:
                    print(f"Duplicate value for {key}")
                    sys.exit(1)
                config[key] = value
    except FileNotFoundError as ex:
        print(f"The configration file {ex} wasn't found")
        sys.exit(1)
    except ValueError as ex:
        print(ex)
        sys.exit(1)
    try:
        check_keys(config, file)
    except ValueError as ex:
        print(ex)
        sys.exit(1)

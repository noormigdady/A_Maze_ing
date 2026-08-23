import sys
import typing


def check_keys(config: dict, file: str) -> None:
    if "width" not in config:
        raise ValueError(f"Width key is missing in the {file} file")
    if "height" not in config:
        raise ValueError(f"Height key is missing in the {file} file")
    if "entry" not in config:
        raise ValueError(f"Entry point key is missing in the {file} file")
    if "exit" not in config:
        raise ValueError(f"Exit point key is missing in the {file} file")
    if "output_file" not in config:
        raise ValueError(f"Output_file key is missing in the {file} file")
    if "perfect" not in config:
        raise ValueError(f"Perfect key is missing in the {file} file")


def parsser(key: str, value: typing.Any) -> typing.Any:
    parsed_value: typing.Any
    if key in ("height", "width"):
        parsed_value = int(value)
    elif key in ("entry", "exit"):
        point = value.split(",")
        if len(point) != 2:
            raise ValueError(f"Wrong format for a {key.upper()} "
                             "must be : (x, y)")
        try:
            parsed_value = (int(point[0]), int(point[1]))
        except ValueError:
            print(f"'{key.upper()}' coordinates must be integers")
            sys.exit(1)
    elif key == "output_file":
        file_name = value.split(".")
        if len(file_name) == 2 and file_name[1] == "txt":
            parsed_value = value
        else:
            raise ValueError("Wrong format for OUTPUT_FILE")
    elif key == "perfect":
        v = value.lower()
        if v in ("true", "false"):
            parsed_value = v
        else:
            raise ValueError("Wrong value for PERFECT key")
    else:
        parsed_value = value
    return parsed_value


def parse_input(file: str) -> None:
    config = {}
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line[0] == "#":
                    continue
                if "=" not in line:
                    raise ValueError(f"Invalid format: {line}, "
                                     "should be in the format: KEY=VALUE")
                parts = line.split("=")
                if len(parts) != 2:
                    raise ValueError(f"Invalid format: {line}, "
                                     "Should be: KEY=VALUE")
                key, value = parts
                key = key.strip().lower()
                value = value.strip()
                if key in config:
                    print(f"Duplicate value for {key}")
                    sys.exit(1)
                config[key] = value
    except FileNotFoundError as ex:
        print(f"The configuration file {ex} wasn't found")
        sys.exit(1)
    except ValueError as ex:
        print(ex)
        sys.exit(1)
    try:
        check_keys(config, file)
    except ValueError as ex:
        print(ex)
        sys.exit(1)
    try:
        for key, value in config.items():
            parsser(key, value)
    except ValueError as ex:
        print(ex)
        sys.exit(1)

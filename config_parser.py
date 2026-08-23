class DuplicateError(Exception):
    def __init__(self):
        super.__init__("Duplicate configuration")


class FormateError(Exception):
    def __init__(self):
        super.__init__("Invalid formate, must be KEY=VALUE")


def config_parser(file):
    required = ["HEIGHT", "WIDTH", "ENTRY", "EXIT", "PERFECT", "OUTPUT_FILE"]
    CONFIG = {}
    with open(file, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            if "=" not in line:
                raise FormateError
            lst = line.strip().split("=")
            if len(lst) != 2:
                raise FormateError
            if lst[0] in ["HEIGHT", "WIDTH"]:
                if lst[0] in CONFIG:
                    raise DuplicateError
                CONFIG[lst[0]] = int(lst[1])
            if lst[0] in ["ENTRY", "EXIT"]:
                if lst[0] in CONFIG:
                    raise DuplicateError
                pair = lst[1].split(",")
                i, j = pair
                if len(pair) != 2:
                    raise Exception("ENTRY/EXIT must be pairs (a, b)")
                CONFIG[lst[0]] = (int(i), int(j))
            if lst[0] == "OUTPUT_FILE":
                if not lst[1].strip("\n").endswith(".txt"):
                    raise Exception("Invalid file extention, must be .txt")
                CONFIG[lst[0]] = lst[1]
            if lst[0] == "PERFECT":
                if lst[1].lower() == "true":
                    CONFIG[lst[0]] = True
                if lst[1].lower == "false":
                    CONFIG[lst[0]] = False
            if lst[0] == "SEED":
                CONFIG["SEED"] = lst[1]

        for i in required:
            if i not in CONFIG:
                raise Exception(f"MISSING A REQUIRED CONFIGURATION <{i}>")
    return CONFIG


if __name__ == "__main__":
    try:
        config = config_parser("config.txt")
        print(config)
    except Exception as e:
        message = str(e).split(",")
        print(message[0])

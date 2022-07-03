from config import PATH_TO_STATS_FILE

def read_stats_from_file():
    counter = {}
    with open(PATH_TO_STATS_FILE, 'r') as f:
        for req in f.readlines():
            splitted_row = req.strip().split(": ")
            counter[splitted_row[0]] = int(splitted_row[1])
        return counter


def write_stats_to_file(data: dict):
    with open(PATH_TO_STATS_FILE, 'w') as f:
        for key, val in data.items():
            f.write(f"{key}: {val}\n")




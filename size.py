def get_size(bytes, suffix="B"):

    factor = 1024
    for unit in ['', "k", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

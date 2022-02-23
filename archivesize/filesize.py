

def human_size(bytes_count: int) -> str:
    """Given an integer size, return a short string formatted with a binary prefix """
    if bytes_count < 1024:
        return f"{bytes_count} Bytes"
    unite = 0
    suffix = "BKMGTPEZY"
    while bytes_count >= 1024:
        bytes_count /= 1024
        unite += 1
    if unite > 6:
        return "> 1024 YiP"
    return f"{bytes_count:.1f} {suffix[unite]}iB"


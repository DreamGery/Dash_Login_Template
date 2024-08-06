import hashlib


def str2md5(input_str: str):
    md5 = hashlib.md5()
    md5.update(input_str.encode("utf-8"))
    return md5.hexdigest()

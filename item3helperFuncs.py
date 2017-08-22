# -----****minimal Python 3 effective usage guide****-----
# bytes, string, and unicode differences

# always converts to str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

# always converts to bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value
# create str var a and make sure its str
a = to_str("andrew")
print(a)
# create str var and convert to bytes
a = to_bytes(a)
print(a)

# bytes are sequences of 8-bit values
# bytes and str instances are not compatible
# use helper functions to ensure inputs are proper type
# always open file in binary mode('rb' or 'wb') if you want to
# read or write to file

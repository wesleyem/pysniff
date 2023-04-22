import datetime

def timestamped(string, time_format):
    """Timestamp the given string"""
    return f"{datetime.datetime.utcnow().strftime(time_format)}-{string}"
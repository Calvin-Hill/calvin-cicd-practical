from datetime import datetime

def get_time(name: str, timezone: int):
    """
    this function greets the user and gives the time in their timezone
    first_name (str): first name of user
    last_name (str): first name of user
    timezone (int): timezone of the user as +/- from UTC
    """
    user = name
    now = datetime.utcnow()
    current_time = now.strftime("{}:%M:%S".format(now.hour+timezone))
    response = "Hello " + user + ", the time is currently " + current_time

    return user, current_time, response

import datetime

SESSION_EXPIRY_MINUTES = 60

class Session:
    def __init__(self, username):
        self.username = username
        self.creation_time = datetime.datetime.now(datetime.timezone.utc)
        self.expiration_time = self.creation_time + \
            datetime.timedelta(minutes=SESSION_EXPIRY_MINUTES)
        print(self.expiration_time.tzinfo)

    def is_expired(self):
        current_time = datetime.datetime.now(datetime.timezone.utc)
        return current_time >= self.expiration_time

    def __str__(self):
        return f"Username: {self.username}\nCreated: {self.creation_time}\nExpires: {self.expiration_time}"



from psycopg2 import OperationalError

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

class DeployError(Exception):
    def __init__(self, error):
        self.error = error

    @staticmethod
    def db_starting_up(ex: OperationalError) -> bool:
        failure = False
        if str(ex).find("The database system is starting up") > 0:
            failure = True
        return failure
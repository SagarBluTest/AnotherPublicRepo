password = "Pass12345!!XXabc"
user_pwd = "OpenF3ast123@"


class db:
  def __init__(self, connection):
    self._connection = connection
    
  def connect_to_db(self):
    self._connection.connect(user=credentials, password=password)
    password = "Micro@12345!!XXabc"

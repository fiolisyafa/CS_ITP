class User():
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print('First Name: ' + self.first_name + '\nLast Name: ' + self.last_name + '\nUsername: ' + self.username)

    def greet_user(self):
        print('Good evening, ' + self.username)

user = User('Aldi', 'Arief', 'aldi_4000')
user2 = User('Aditya', 'Pribadi', 'adityapribadi3')
user3 = User('Veronika', 'Stephanie', 'veronikastephanie')

user.describe_user()
user.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

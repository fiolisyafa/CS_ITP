class User():
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print('First Name: ' + self.first_name + '\nLast Name: ' + self.last_name + '\nUsername: ' + self.username)

    def greet_user(self):
        print('Good evening, ' + self.username)

class Admin(User):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

user = User('First', 'Last', 'Username')
admin = Admin('First', 'Last', 'Username')
admin.show_privileges()

# print(oct(7))
# print(oct(8))
# print(oct(11))
# print(oct(1232))


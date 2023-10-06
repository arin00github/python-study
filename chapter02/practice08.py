class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addr = addr
    def print_info(self):
        print('Nmae: ', self.name)
        print('Phone: ', self.phone_number)
        print('E-mail: ', self.email)
        print('Address: ', self.addr)
        
        
def set_contact():
    name = input("Name: ", )
    phone_number = input('Phone: ')
    e_mail = input('E-mail: ')
    addr = input('Address: ')
    print(name, phone_number, e_mail, addr)


def run():
    set_contact()
    
    
if __name__ == '__main__':
    run()
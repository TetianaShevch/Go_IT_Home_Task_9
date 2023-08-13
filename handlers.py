AddressBook = {
'Mary':'0503335476',
'John':'0679876543'
}

def input_error1(func):
    def inner(args):
        if not args or len(args.split(' ',1)) == 1:
            print('Give me name and phone please')
            return 
        func(args)
    return inner

def input_error2(func):
    def inner(args):
        if not args:
            print('Enter user name please')
            return 
        func(args)
    return inner

def exit_handler(args):
    print('Good bye!')
    is_exit = True
    return is_exit
    
def hello_handler(args):
    print('How can I help you?')

@input_error1
def add_contact(args):
    contact = args.strip().split(' ',1)
    AddressBook[contact[0]] = contact[1].strip()
    print(f'Contact of {contact[0]} was added')

@input_error1
def change_contact(args):
    contact = args.strip().split(' ',1)
    for key, value in AddressBook.items():
        if key == contact[0]:
            AddressBook[contact[0]] = contact[1].strip()
            print(f'Contact for {contact[0]} was changed')
            return
    print('This name is not found')
   

@input_error2
def phone_of_person(args):
    contact = args.strip().split(' ',1)
    for key, value in AddressBook.items():
        if key == contact[0]:
            print(f'The phone of {key} is {value}')
            return
    print('This name is not found')
             
def show_all(args):
    for key, value in AddressBook.items():
        print(key,value)
from handlers import exit_handler, hello_handler, add_contact, change_contact, phone_of_person, show_all

COMMANDS = {exit_handler: ['good bye','close','exit'], 
            hello_handler: ['hello'], 
            add_contact: ['add'], 
            change_contact: ['change'],
            phone_of_person: ['phone'],
            show_all: ['show all']         
}

def user_input_handler(user_input:str):
    user_input = user_input.strip()
    for key, value in COMMANDS.items():
        for command in value:
            if user_input.lower().startswith(command):
                args = user_input[len(command)::].strip()
                return key, args
    print('Your command is mistaken. Please, try again')
    return None, ''


if __name__ == "__main__":
    is_exit = False
    while not is_exit:
        user_input = input("Enter a command: ")
        key, args = user_input_handler(user_input)
        if key:
            is_exit = key(args)
        continue
      
        
        
        


usernames = ['jimbo', 'giltson98', 'derekf',
             'WhatSup', 'NicolEye', 'swei45',\
             'BaseInterpreterInterface', 'BaseStdIn', \
             'Command', 'ExecState', 'InteractiveConsole', \
             'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Enter name: ")

if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")
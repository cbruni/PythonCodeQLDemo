import os

def run_system_command(user_input):
    command = f"ls {user_input}"
    os.system(command)

user_input = input("Enter the directory or file name: ")
run_system_command(user_input)

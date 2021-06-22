# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def autoCheckIn():
    """
    attempt to auto check in upon starting program, 
    """
    import genshinstats
    genshinstats.set_cookie_auto()
    while True:
        success = genshinstats.sign_in()
        if success:
            print('Claimed daily reward.')
            exit(1)
        else:
            print('Could not claim daily rewards')
            exit(-1)
    pass


def mainLoop():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    autoCheckIn()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

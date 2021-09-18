# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def autoCheckIn():
    """
    attempt to auto check in upon starting program, 
    """
    import genshinstats as gs
    gs.set_cookie_auto()
    reward = gs.claim_daily_reward()
    if reward is not None:
        print(f"Claimed daily reward - {reward['cnt']}x {reward['name']}")
    else:
        print("Could not claim daily reward")


def mainLoop():
    pass


def tmp():
    import schedule
    import time
    schedule.every().day.at('17:00').do(autoCheckIn)
    while True:
        schedule.run_pending()
        time.sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    autoCheckIn()
    tmp()

"""
import genshinstats
genshinstats.set_cookie_auto()
while True:
    success = genshinstats.sign_in()
    if success:
        if str is not None:
            print('Claimed daily reward.')
            exit(1)
    else:
        if str is not None:
            print('Could not claim daily rewards')
            exit(-1)

# Press the green button in the gutter to run the script.
import schedule
import time
schedule.every().day.at('01:00').do(autoCheckIn,"a")
while True:
    schedule.run_pending()
    time.sleep(1)
    

"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

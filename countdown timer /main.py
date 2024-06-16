import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print('Time\'s up!')

def main():
    try:
        seconds = int(input("Enter the time in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print("Please enter an integer value for the time.")

if __name__ == "__main__":
    main()

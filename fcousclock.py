import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Time left: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

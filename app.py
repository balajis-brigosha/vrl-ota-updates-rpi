import time

while True:

    with open("/tmp/heartbeat.txt", "w") as f:
        f.write(str(time.time()))

    print("Running Version 21")

    time.sleep(3)

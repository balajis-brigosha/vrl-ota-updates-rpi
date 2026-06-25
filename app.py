import time

while True:

    with open("/tmp/heartbeat.txt", "w") as f:
        f.write(str(time.time()))

    print("Running Version 22")

    time.sleep(3)

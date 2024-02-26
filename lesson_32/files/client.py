import time

while True:
    with open("middleware.txt") as file:
        message = file.read()

    print(message)

    time.sleep(1)

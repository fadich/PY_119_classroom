import time

while True:
    message = input("Message: ")
    with open("middleware.txt", "w") as file:
        file.write(message)
        time.sleep(1)

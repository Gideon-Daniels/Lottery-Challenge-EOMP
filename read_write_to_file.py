def writing_file(name, surname, id, email, day, month, year):
    f = open("users.txt", "w+")
    try:
        f.write(name)

    finally:
        f.close()


def reading_file():
    f = open("users.txt", "r+")
    try:
        f.readline()

    finally:
        f.close()


def append(appending):
    f = open("users.txt", "a")
    try:
        f.write(appending)
    finally:
        f.close()

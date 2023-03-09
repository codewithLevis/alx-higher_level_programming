#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    values = dir(hidden_4)
    for value in values:
        if value[:2] != "__":
            print(value)

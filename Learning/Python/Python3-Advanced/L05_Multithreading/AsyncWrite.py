import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, "a") as f:
            f.write(self.text+"\n")
        time.sleep(2)
        print("Finished Background File Write to %s." % self.out)

def Main():
    message = input("Enter a string to store: ")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("The program can continue while it write in another thread.")
    print("100 + 400 = ",100+400)

    background.join()
    print("Waited util thread was completed.")

if __name__ == "__main__":
    Main()
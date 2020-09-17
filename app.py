from flask import Flask
import threading
import time

COUNTER_MAX = 5000

#Create a threaded task which will update a counter
#every 1 second. 
class ThreadedTask(threading.Thread):
    def __init__(self,):
        self.counter = 0
        self.COUNTER_MAX = 5000
        threading.Thread.__init__(self)
        
    def run(self):
        while True:
            self.counter += 1
            if self.counter > self.COUNTER_MAX:
                self.counter = 0
            time.sleep(5)  # Simulate long running process
            print("hello")

#Create our flask application
app = Flask(__name__)

#Always return a Hello World message and the counter value
@app.route("/")
def index():
    return "Hello World!\nCounter is {}".format(task.counter)

#Start our threaded task and flask
task = ThreadedTask()
task.start()
app.run(host="0.0.0.0", port=5000, debug=True)

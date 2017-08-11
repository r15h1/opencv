import sys
from trainer import trainer

options = "1. train system\n2. arm\n3. exit"

def run():    
    while True:
        print "\n----------spycam intelligent surveillance----------------"
        prompt = "select an option:\n{0}\nspycam:\\>"
        option = raw_input(prompt.format(options))
        if option == "3":
            print "see you later mater"
            break;
        elif option == "1":
            trainSystem()
        elif option == "2":
            armSystem()

def trainSystem():
    t = trainer()
    t.train()
    pass

def armSystem():
    print "arming system"
    pass

run()
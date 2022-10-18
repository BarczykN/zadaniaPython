

#stworzyć klasę Fork i metodę take
class Fork:
    def __init__(self,name,state):
        self.name = name
        self.state = state

    def take(self):
        if self.state == False:
            print("already in use")
            return 1
        else:
            self.state = False
            return 0


    def returnFork(self):
        self.state = True

    def __str__(self):
        return str(self.state)


forks = [Fork("1",True), Fork("2",True), Fork("3",True), Fork("4",True), Fork("5",True)]


class Philosoph:
    def __init__(self, name, fork1, fork2):
        self.name = name
        self.fork1 = fork1-1
        self.fork2 = fork2-1
        self.state = "think"
        self.counter = 0
        self.forks = []

    def eat(self,count):
        self.state = "eat"
        self.counter = count
        if self.forks.count(self.fork1) != True or self.forks.count(self.fork2) != True:
            result1 = forks[self.fork1].take()
            result2 = forks[self.fork2].take()
            if result1 == 1 and result2 == 0:
                print("Unsuccesfull")
                self.state = "wantEat"
                self.counter = 0
                forks[self.fork2].returnFork()
            elif result2 == 1 and result1 == 0:
                print("Unsuccesfull")
                self.state = "wantEat"
                self.counter = 0
                forks[self.fork1].returnFork()
            elif result2 == 1 and result1 == 1:
                print("Unsuccesfull")
                self.state = "wantEat"
                self.counter = 0



    def think(self):
        self.state = "think"

    def wantEat(self):
        self.state = "wantEat"

    def giveFork(self, index):
        self.forks.append(index)
        print(self.name)
        print("forks check:"+str(self.forks.count(self.fork1) and self.forks.count(self.fork2)))
        if self.forks.count(self.fork1) and self.forks.count(self.fork2):
            print(self.name)
            print("can eat")
            self.eat(4)

    def checkState(self):
        if self.state == "eat":
            print(self.name+" is eating...")
            self.counter -= 1
            if self.counter == 0:
                forks[self.fork1].returnFork()
                forks[self.fork2].returnFork()
                self.forks.clear()
                self.think()

        if self.state == "think":
            print(self.name + " is thinking...")
        elif self.state == "wantEat":
            print(self.name + " wants to eat something...")

    def __str__(self):
        return self.name

def main():

    philosophes = [Philosoph("A",1,5), Philosoph("B",1,2), Philosoph("C",2,3), Philosoph("D",3,4), Philosoph("E",4,5)]
    queue = []

    philosophes[0].eat(4)
    philosophes[1].eat(4)
    philosophes[2].eat(5)
    philosophes[1].state = "wantEat"
    philosophes[3].state = "wantEat"



    for i in range(0,10):

        for p in philosophes:
            p.checkState()
            state = p.state
            print(state)
            if state == "wantEat":
                if p not in queue:
                    queue.append(p)



        counter = 0



        print()



        pop_from_Queue = []

        for p in queue:
            if forks[p.fork1].state:
                forks[p.fork1].take()
                p.giveFork(p.fork1)

            if forks[p.fork2].state:
                forks[p.fork2].take()
                p.giveFork(p.fork2)

            if p.state == "eat":
                pop_from_Queue.append(counter)

            counter += 1


        for i in pop_from_Queue:
            queue.pop(i)
            pop_from_Queue[i+1] -= 1

if __name__ == '__main__':
    main()
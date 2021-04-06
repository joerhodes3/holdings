class assests():
    def __init__(self):
        self.stuff = []

    def buy(self,???):





        indexes = []
        lenShoe = len(self.shoe)
        self.shuffled = []
        for i in range(lenShoe):
           num = random.randrange(0,lenShoe,1)
           while num in indexes:
               # keep guessing again until is unique
               num = random.randrange(0,lenShoe,1)
           indexes.append(num)
        print("DEBUG all indexes: %s out of len: %s",(indexes,len(indexes)))
        for num in indexes:
            self.shuffled.append(self.shoe[num])

    def deal(self, numCards):
        self.hand = []
        for i in range(numCards):
            self.hand.append(self.shuffled[i])

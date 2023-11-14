class Asker():
    @staticmethod
    def askall(lst):
        for i in lst:
            i.report()


class Sender():
    first = True

    @classmethod
    def report(self):
        if self.first:
            print("Greetings!")
            self.first = False
        else:
            print("Get away!")


Asker.askall([Sender(), Sender(), Sender()])

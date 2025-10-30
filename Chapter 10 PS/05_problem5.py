# if we change self to slf or harry the propraam will run 
# but we have to change self to slf or harry from in all apperences
# but its not a good practice, it will disturb the readability of program


from random import randint

class Train:

    def __init__(slf, trainNo, fro, to):
        slf.trainNo = trainNo
        slf.fro = fro
        slf.to = to
        
    def bookTicket(slf):
        print(f"Ticket is booked in train No: {slf.trainNo} from {slf.fro} to {slf.to}")

    def getStatus(slf):
        print(f"Train no {slf.trainNo} is running on time.")

    def getFareInfo(slf):
        print(f"Ticket fare in train No: {slf.trainNo} from {slf.fro} to {slf.to} is {randint(3000, 6000)}")

t = Train(4322, "Mansehra", "Karachi")
t.bookTicket()
t.getStatus()
t.getFareInfo()


# we can also write it

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time")

    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
 

import random
class Checkout():
    def __init__(self, customers, stations):
        self.customers = [[i,None] for i in range(customers)]
        self.stations = [[i,0] for i in range(stations)]

    def start(self):
        self.currentCustomerInLine = 1
        self.checkIfAvailable()

    def checkIfAvailable(self):
        for i in self.stations:
            if i[1] == 0:
                self.customers[self.currentCustomerInLine-1][]

    def processCustomer(self):
        pass

    def newCustomerToLine(self):
        pass

    def nextPersonToStation(self):
        pass

class TicketCounterSimulation :
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
    self.arriveProb = 1.0 / betweenTime
    self.serviceTime = serviceTime
    self.numMinutes = numMinutes
    self.passengerQ = []
    self.theAgents = Array( numAgents )
    for i in range( numAgents ) :
    self.theAgents[i] = TicketAgent(i+1)
    self.totalWaitTime = 0
    self.numPassengers = 0

    def run( self ):
        for curTime in range(self._numMinutes + 1) :
            self._handleArrival( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
        len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )
from event import Event
from brother import Brother


def buildBrotherList():
	f = open("brotherList.txt", "r")
	lines = f.readlines()
	returnArr = []
	brotherList = []
	count = 0
	for line in lines:
		if count == 0:
			arr = []
		arr.append(line.strip())
		count +=1
		if count == 5:
			returnArr.append(arr)
			count = 0
	
	for bruh in returnArr:
		bro = Brother(bruh[0], bruh[1], bruh[2], bruh[3], bruh[4])
		brotherList.append(bro)

	f.close()
	return brotherList



def buildEventList():
	f = open("events.txt", "r")
	lines = f.readlines()
	events = []

	for line in lines:
		ev = Event(line.strip(), "NA")
		events.append(ev)

	f.close()
	return events

def getBrother(brothers, name):
	for bro in brothers:
		if bro.name == name:
			return bro

def findEvent(events, event):
	for ev in events:
		if ev.name == event:
			return ev
		else:
			temp = Event("Error")
			return temp

def eventFull(event):
	if len(event.brothers) >= 4 and "Party" in event.name:
		return True
	elif len(event.brothers) >= 2 and "Social" in event.name:
		return True
	else:
		return False

def printBrothers(broList):
	for bro in broList:
		print("Name: " + bro.name + ", Number: " + bro.number + ", Prefrences: " + bro.event1 + ", " + bro.event2 + ", " + bro.event3)


def printEvents(events):
	for event in events:
		print("--- " + event.name + " ---")
		for i in range(0, len(event.brothers)):
			print(event.brothers[i])
		print("\n")

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high].number     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j].number <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

#****************************************************************************#
# Given lists of sorted brothers and events, it will assign max of 2 shifts per 
# brother depending on the brother's number and preference.
#****************************************************************************#
def assignShiftsByPreferance(events, brothers):
	noPrefList = []
	secondFilterList = []
	thirdFilterlist = []

	# Preference Filter 1
	brotherCopy = brothers.copy()
	for bro in brotherCopy:
		print(bro.name)

		# If brother at max shifts skip that brother
		if bro.numShifts == 2:
			continue

		pref1 = findEvent(events, bro.event1)
		pref2 = findEvent(events, bro.event2)
		pref3 = findEvent(events, bro.event3)

		# If brother has no preferances, add him to the no preference list
		if bro.event1 == "NA" and bro.event2 == "NA" and bro.event3 == "NA":
			noPrefList.append(bro)
			brothers.remove(bro)
			continue
		elif eventFull(pref1) == False:
			bro.numShifts += 1
			pref1.brothers.append(bro)
		else:
			brothers.remove(bro)
			secondFilterList.append(bro)

	print("*******************************************************************")
	printBrothers(noPrefList)
	print("*******************************************************************")

	for bro in brothers:
		secondFilterList.append(bro)
	printBrothers(secondFilterList)

	for bro in secondFilterList:
		if bro.numShifts == 2:
			temp = secondFilterList.remove(bro)
			continue
		pref2 = findEvent(events, bro.event2)
		if eventFull(pref2) == False:
			bro.numShifts += 1
			pref2.brothers.append(bro)
		else:
			temp = secondFilterList.remove(bro)
			thirdFilterlist.append()

	for bro in secondFilterList:
		thirdFilterlist.append(bro)

	for bro in thirdFilterlist:
		if bro.numShifts == 2:
			continue
		pref3 = findEvent(events, bro.event3)
		if eventFull(pref3) == False:
			bro.numShifts += 1
			pref3.brothers.append(bro)
		else:
			noPrefList.append(bro)

	return noPrefList


def assignRemainingShifts(events, brothers):
	i = 0
	for currEvent in events:
		if eventFull(currEvent) == False and len(brothers) > 0:
			currEvent.brothers.append(brothers[i])
			i += 1




def main():
	actives = buildBrotherList()
	events = buildEventList()
	assignedEvents = []

	lastElem = len(actives) - 1
	quickSort(actives, 0, lastElem)

	printBrothers(actives)
	printEvents(events)

	remaining = assignShiftsByPreferance(events, actives)
	assignRemainingShifts(events, remaining)



main()
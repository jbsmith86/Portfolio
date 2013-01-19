# This code creates a doubly linked list where an object Frob is ordered alphabetically
# by its name and given a link to the object before and after it. You can insert a new frob
# by calling the method insert and passing it a frob (newFrob) to another frob (atMe) that
# is a member of the list you wish to add it to. There is no actual object for the list
# the list is simply created by inserting frobs.

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    atmecopy = atMe
    newfrobcopy = newFrob
    if newFrob.myName() == atMe.myName():
        placeFrob(newfrobcopy, atmecopy, atMe.getAfter())
    elif newFrob.myName() > atMe.myName():
        if atMe.getAfter() == None:
            placeFrob(newfrobcopy, atmecopy, None)
        elif newFrob.myName() < atMe.getAfter().myName():
            placeFrob(newfrobcopy, atmecopy, atMe.getAfter())
        else:
            insert(atMe.getAfter(), newfrobcopy)
    else:
        if atMe.getBefore() == None:
            placeFrob(newfrobcopy, None, atmecopy)
        elif newFrob.myName() > atMe.getBefore().myName():
            placeFrob(newfrobcopy, atMe.getBefore(), atmecopy)
        else:
            insert(atMe.getBefore(), newfrobcopy)
            
def placeFrob(newFrob, before, after):
	"""
	This code places a frob once it has determined where it belongs.
	"""
    if before == None:
        newFrob.setAfter(after)
        after.setBefore(newFrob)
    elif after == None:
        newFrob.setBefore(before)
        before.setAfter(newFrob)
    else:
        newFrob.setBefore(before)
        newFrob.setAfter(after)
        before.setAfter(newFrob)
        after.setBefore(newFrob)
import colmin as cm
import rowmin as rm
import northwest as nw
import input

input.getInput()
print "\n\nEnter your choice"
ip = int(raw_input("1.Northwest corner rule\n2.Row Minima rule\n3.Column Minima\n0.To exit\nEnter your choice:"))
while ip!=0:
    if ip == 1:
        print"North West Corner Rule"
        nw.init()
        nw.allocate()
        nw.transcost()
    elif ip == 2:
        print"Row min"
        rm.init()
        rm.allocate()
        rm.transcost()
    elif ip == 3:
        print"Col Min"
        cm.init()
        cm.allocate()
        cm.transcost()
    ip = int(raw_input("\n\n1.Northwest corner rule\n2.Row Minima rule\n3.COrner Minima\n0.To exit\nEnter your choice:"))
else:
    print "Closing"
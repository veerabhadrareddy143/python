class nanna:
    def properties(self):
        total=5;
        print("nanna has 5acres of land")
class raja(nanna):
    def occupy(self):
        i=int(input("enter if veera married or not ,if married press '1' or '0'"))
        if i>0:
            print("raja will get half of the land ")
        else:
            print("raja will get whole land")
class veera(nanna):
    def occupy(self):
        i = int(input("enter if raja married or not ,if married press '1' or '0'"))
        if i>0:
            print("veera will get half of the land ")
        else:
            print("veera will get whole land")

c=veera()
c.occupy()
d=raja()
d.occupy()





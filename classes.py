class veera:

    def __init__(self):
        print("anna is also great")
        self.ra=self.raja()
    def demo(self):
        print('veera is great')

    class raja:
            def __init__(self):
                print("kavitha is great")
            def demo(self):
                print("nanna is great")

a=veera.raja()
a.demo()
z=veera()               # object creation
veera.demo(z)


class Myself():
    def info(self,name,age,city,street):
        self.name = name
        self.age = age
        self.city = city
        self.street = street
    def about(self):
            print("Your name is " + self.name + " and you are " + self.age + "years old, You come from " + self.city + " and live in " + self.street + " street")
kwame = Myself()
kwame.info("kwame","32","Accra","Spiney")
kwame.about()
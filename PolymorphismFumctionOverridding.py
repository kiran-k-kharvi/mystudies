class Birds:
    def fly(self):
        print("Bird fly very high")

class Sparrow(Birds):
    def fly(self):
        print("sparrow fly ")

class Swan(Birds):
    def fly(self):
        print("Swan dont fly")

sparrow = Sparrow()
swan = Swan()

sparrow.fly()
swan.fly()

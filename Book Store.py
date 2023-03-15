################################
# Name: Matthew Bodenstein
# Date: Feb 13, 2020
# File name: Book Store.py
##############################################

class Product():
    def __init__(self, name, UPC, weight, cost):
        self.name = name
        self.UPC = UPC
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return ("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+ "\nCost: $" + str(self.cost))
##########
class Non_Consumable(Product):
    def __init__(self,name, UPC, weight, cost, ISBN, Title):
        Product.__init__(self, name, UPC, weight, cost)
        self.ISBN = ISBN
        self.Title = Title
    def __str__(self):
        return (("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+
                "\nCost: $" + str(self.cost))+"\nISBN: "+str(self.ISBN) + "\nTitle: "+ self.Title)

class Book(Non_Consumable):
    def __init__(self,name, UPC, weight, cost, ISBN, Title,Author):
        Non_Consumable.__init__(self,name, UPC, weight, cost, ISBN, Title)
        self.Author = Author
    def __str__(self):
        return (("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+
                "\nCost: $" + str(self.cost))+"\nISBN: "+str(self.ISBN) + "\nTitle: "+ self.Title)+"\nAuthor: "+self.Author

class DVD(Non_Consumable):
    def __init__(self,name, UPC, weight, cost, ISBN, Title,Director):
        Non_Consumable.__init__(self,name, UPC, weight, cost, ISBN, Title)
        self.Director = Director
    def __str__(self):
        return (("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+
                "\nCost: $" + str(self.cost))+"\nISBN: "+str(self.ISBN) + "\nTitle: "+ self.Title)+"\nDirector: "+self.Director

class CD(Non_Consumable):
    def __init__(self, name, UPC, weight, cost, ISBN, Title, Artist):
        Non_Consumable.__init__(self, name, UPC, weight, cost, ISBN, Title)
        self.Artist = Artist
    def __str__(self):
        return (("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+
                "\nCost: $" + str(self.cost))+"\nISBN: "+str(self.ISBN) + "\nTitle: "+ self.Title)+"\nArtist: " + self.Artist

##########
class Consumable(Product):
    def __init__(self, name, UPC, weight, cost, Ex_Date):
        Product.__init__(self, name, UPC, weight, cost)
        self.Ex_Date = Ex_Date
    def __str__(self):
        return (("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+
                "\nCost: $" + str(self.cost)))+"\nExpiration Date: " + str(self.Ex_Date)

class Drink(Consumable):
    def __init__(self, name, UPC, weight, cost,Ex_Date, Cont_Type):
        Consumable.__init__(self, name, UPC, weight, cost, Ex_Date)
        self.Cont_Type = Cont_Type
    def __str__(self):
        return (("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+
                "\nCost: $" + str(self.cost)))+"\nExpiration Date: " + str(self.Ex_Date)+"\nContainer Type: " + str(self.Cont_Type)

class Food(Consumable):
    def __init__(self, name, UPC, weight, cost, Ex_Date, Package):
        Consumable.__init__(self, name, UPC, weight, cost, Ex_Date)
        self.Package = Package
    def __str__(self):
        return (("Name: "+self.name + "\nUPC: "+ str(self.UPC) + "\nWeight: "+str(self.weight)+
                "\nCost: $" + str(self.cost)))+"\nExpiration Date: " + str(self.Ex_Date)+"\nPackaging Type: " + str(self.Package)

#################
name = "Bodey"
UPC = 1234321
weight = 223
cost = 4332
ISBN = 34423143132
Title = "My Life"
print(Book(name, UPC, weight, cost, ISBN, Title,"Bodiac Killer"), "\n", "\n")
print(DVD(name, UPC, weight, cost, ISBN, Title, "Bodiac Killer"),"\n", "\n")
print(CD(name, UPC, weight, cost, ISBN, Title, "Bodiac Killer"),"\n", "\n")
print(Drink(name, UPC, weight, cost, "22/12/45", "Large"),"\n", "\n")
print(Food(name, UPC, weight, cost, "12/21/24", "Medium"))
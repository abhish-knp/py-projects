class Library():
    def __init__(self,b_name):
        self.bookname = b_name
#         self.ownername = ownername
        
    @classmethod
    def change_stu(cls,ownername):
        cls.ownername = ownername   
    
    @property
    def owner(self,ownername):
        print("Setting up owner name")
        self.ownername = self.ownername
    
    @owner.setter
    def owner(self, ownername):
            self.ownername = ownername
        
    def explain(self):
#         a = self.ownername
        return(f"Book {self.bookname} is owned by {Library.change_stu(self.ownername)}")
    
    @owner.deleter
    def owner(self):
        print("Deleting Now...")
        self.ownername = None

if __name__ == "__main__":
    book1 = Library("Maths")
    book2 = Library("Polity")
    book3 = Library("Physics")
    
    print("\n_________Testing____________")
    print("name of book owner ", book1.bookname)
    print("\n________setting up new owner_________")
    book1.owner = "abhish"
    print("explain the book1: ", book1.explain())
    print("owner of  the book1: ", book1.ownername)
    print("\n________Deleting the record_________")
    del book1.owner
    print("status of book 1: ", book1.explain())
    print("status of book 2:", book2.explain())
    book2.owner = "Shivendra"
    print(f"New owner of {book2.bookname} is {book2.ownername}.")
    print("Deleting the record")
    del book2.owner
    print(f"New owner of {book2.bookname} is {book2.ownername}.")
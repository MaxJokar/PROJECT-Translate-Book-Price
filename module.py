from abc import ABC, abstractmethod


class Text(ABC):
    def __init__(self,lang):
        self.lang=lang
        
    def getlang(self):
         return self.lang
     
    @abstractmethod
    def getFee(self):
        pass
    
class PlainText(Text): # A usual Page has these features !
    def __init__(self,lang,NumbOfWords,NumbOfLines):
        super().__init__(lang)  
        self.NumbOfWords=NumbOfWords
        self.NumbOfLines=NumbOfLines
           
    def getFee(self):
        return self.NumbOfWords*2+self.NumbOfLines*4
    
     
     
class Humourous(Text): # A usual Page has these features !
    def __init__(self, lang,NumbOfPics):
        super().__init__(lang)  
        self.NumbOfPics=NumbOfPics
        
    def getFee(self):
        return self.NumbOfPics*5
         
     
class Scientific(Text): 
    def __init__(self, lang,NumbOfWords,NumbOfSciWords):
        super().__init__(lang)  
        self.NumbOfWords=NumbOfWords
        self.NumbOfSciWords=NumbOfSciWords
    
    def getFee(self):
        return self.NumbOfWords*2 +self.NumbOfSciWords *10 
     
#-----------------------------------------------------------------------------------------------------------     
class Book(Text):
    def __init__(self,lang,bookName):
        super().__init__(lang)    
        self.bookName=bookName
        self.textlist=[]  #each book we should know what type of text it has (sci,humor,plain)
    
    def addText(self,text):
        self.textlist.append(text)  
       
    def getFee(self):
        sum=0
        for text in self.textlist:
            sum+=text.getFee()
        return sum
    
    
    
    
print("---------------------BILL FOR  TRANSLATION OF  YOUR  BOOK ------") 
a=input(" what language is your book ?\t En=English , Fr=French , Ger=German :") 
b=input(" Please Enter the Name of the book :")      
book1=Book(a,b) 
# Numberofwords=input("How many WORDS exist in this book ?\t")
# NumberofLines=input("How many LINES exist in this book ?\t") 
book1.addText(PlainText(a,2,3))
# book1.addText()
book1.addText(Humourous("En",20))  



print("--------------------------------------------------------------")
print(f" The Total Price for the book You Orderd is :{book1.getFee()}")

print("--------------------------------------------------------------")
      
        
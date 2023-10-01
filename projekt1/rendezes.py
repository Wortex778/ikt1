import re


class Rendezes:

    def Beolvas(self, allomanynev):  #Beolvassuk a ki.txt
        self.alap = []
        with open(allomanynev, "r", encoding="UTF8") as file:
           self.alap = file.read().split(";")
        del self.alap[-1]  #Alap lista, kivettem az üres sort
        

    def AlphaOrInt(self, list):  #Eldönti hogy szám vagy szöveg    
        i = 0
        I = True
        s = 0
        S = True
        barmi_mas = 0

        chars = re.compile("^[a-zA-Z]+$")

        for x in list:
            y = ''.join(x)
            try:
                if (y[0] == "-"):
                    int(y[1:])
                else:
                    int(y)
            except ValueError:
                I = False
            if (I):
                i += 1
            else:
                S = y.isalpha()
                if (S == True and chars.match(y)):  #Meg nézi van-e benne magyar ékezetes betű
                    s += 1
                else:
                    barmi_mas += 1
                    break

        if (s == len(list)):
            return "string"
        if (i == len(list)):
            return "int"
        if (barmi_mas == 1):
            return "Hiba"
    

    def Listak(self):   #Külön listát csinál ha int vagy ha string

        msg = self.AlphaOrInt(self.alap)
        self.szoveg = []
        self.szam = []

        if (msg == "string"):
            for x in self.alap:
                self.szoveg.append(x)

        if (msg == "int"):
            for x in self.alap:
                self.szam.append(int(x))

        

    def SortInt(self, lst):     #Int növekvő sorrend
        
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if (lst[i] > lst[j]):
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
    
    def ReverseSortInt(self, lst):      #Int csökkenőő sorrend
        
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if (lst[i] < lst[j]):
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
    
    def SortStr(self, lst):     #String növekvő sorrend
       
        for w in range(len(lst)):
            lst[w] = lst[w].lower()

        for n in range(len(lst)-1, 0, -1):
            for i in range(n):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
        
        return lst

    def ReverseSortStr(self, lst):     #String csökkenő sorrend
       
        for w in range(len(lst)):
            lst[w] = lst[w].lower()

        for n in range(len(lst)-1, 0, -1):
            for i in range(n):
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
        
        return lst


    def CocktailSortInt(self, lst):    #Választott algoritmus, Koktél növekvő rendezés int-re
        n = len(lst)
        swapped = True
        start = 0
        end = n-1

        while (swapped == True):
    
            swapped = False

            for i in range(start, end):
                if (lst[i] > lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True

            if (swapped == False):
                break
    
            swapped = False
            end = end-1
    
            for i in range(end-1, start-1, -1):
                if (lst[i] > lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
    
            start = start + 1

        return lst


    def ReverseCocktailSortInt(self, lst):    #Választott algoritmus, Koktél csökkenő rendezés int-re
        n = len(lst)
        swapped = True
        start = 0
        end = n-1
        while (swapped == True):
    
            swapped = False

            for i in range(start, end):
                if (lst[i] < lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True

            if (swapped == False):
                break
    
            swapped = False
            end = end-1
    
            for i in range(end-1, start-1, -1):
                if (lst[i] < lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
    
            start = start + 1

        return lst


    def CocktailSortStr(self, lst):    #Választott algoritmus, Koktél növekvő rendezés srting-re
        n = len(lst)
        swapped = True
        start = 0
        end = n-1

        while (swapped == True):
    
            swapped = False

            for i in range(start, end):
                lst[i] = lst[i].lower()
                if (lst[i] > lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True

            if (swapped == False):
                break
    
            swapped = False
            end = end-1
    
            for i in range(end-1, start-1, -1):
                lst[i] = lst[i].lower()
                if (lst[i] > lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
    
            start = start + 1

        return lst
    

    def ReverseCocktailSorStr(self, lst):    #Választott algoritmus, Koktél csökkenő rendezés string-re
        n = len(lst)
        swapped = True
        start = 0
        end = n-1
        while (swapped == True):
    
            swapped = False

            for i in range(start, end):
                lst[i] = lst[i].lower()
                if (lst[i] < lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True

            if (swapped == False):
                break
    
            swapped = False
            end = end-1
    
            for i in range(end-1, start-1, -1):
                lst[i] = lst[i].lower()
                if (lst[i] < lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
    
            start = start + 1

        return lst


    def NewWord(self, character):       #Egy új szót vagy számot beilleszt a listába

        tipus = self.AlphaOrInt(self.alap)

        if (tipus == "int"):
            self.szam.append(int(character))
            return self.szam
        if (tipus == "string"):
            self.szoveg.append(character)
            return self.szoveg

    def Input(self):    #Az input rész
        
        tipus = self.AlphaOrInt(self.alap)

        if (tipus == "Hiba"):
            return "Hiba"
        else:

            while (True):
                rendez = input("Növekvő vagy csökkenő legyen a rendezés? Írj be 'n' betűt ha növekvő vagy 'cs' betűt ha csökkenő rendezést szeretnél: ")

                if (rendez == "n" or rendez == "cs"):
                    break
                else:
                    print("\n\tHibás bevitel! ")
            

            while (True):
                print("\nA sor számának beírásával válassz a két rendezési algoritmus közül:\n\t1 Sima rendezési algotitmus\n\t2 Koktél rendezési algoritmus")

                algoritmus= input("A választott szám: ")
                print("")

                if (algoritmus == "1" or algoritmus == "2"):
                    break
                else:
                    print("\n\tHibás bevitel!")


            return rendez, int(algoritmus)


    def Output(self, x):   #A kiiratás

        tipus = self.AlphaOrInt(self.alap)
        rendez = x[0]
        algoritmus = x[1]

        if (x == "Hiba"):
            print("Hibás a fájl bemeneti karakterlánca!")
        else:

            if (tipus == "int"):


                if (rendez == "n" and algoritmus == 1):
                    print(self.SortInt(self.szam))
                if (rendez == "n" and algoritmus == 2):
                    print(self.CocktailSortInt(self.szam))
                
                if (rendez == "cs" and algoritmus == 1):
                    print(self.ReverseSortInt(self.szam))
                if (rendez == "cs" and algoritmus == 2):
                    print(self.ReverseCocktailSortInt(self.szam))
            
            if (tipus == "string"):

                if (rendez == "n" and algoritmus == 1):
                    print(self.SortStr(self.szoveg))
                if (rendez == "n" and algoritmus == 2):
                    print(self.CocktailSortStr(self.szoveg))
                
                if (rendez == "cs" and algoritmus == 1):
                    print(self.ReverseSortStr(self.szoveg))
                if (rendez == "cs" and algoritmus == 2):
                    print(self.ReverseCocktailSorStr(self.ReverseCocktailSorStr((self.szoveg))))        #Az utolsó szót kihagyta a rendzésből, de így működik

    def NewWordInput(self):

        fajl_tipus = self.AlphaOrInt(self.alap)

        if (fajl_tipus == "int"):
            while (True):
                
                print("\nA beolvasott fájl számokból áll!")
                new_character = input("Adj meg egy számot amelyet a listához szeretnél adni: ")

                I = True

                try:
                    if (new_character[0] == "-"):       #Kényszer megoldás, de működik
                        int(new_character[1:])
                    else:
                        int(new_character)
                except ValueError:
                    I = False
                if (I):
                    break
                else:
                    print("\n\tHibás bevitel!")
                
            return new_character
        

        if (fajl_tipus == "string"):
            while (True):
                
                print("\nA beolvasott fájl szavakból áll (Angol ABC)!")
                new_character = input("Adj meg egy szavat amelyet a listához szeretnél adni: ")
                
                tipus = self.AlphaOrInt(new_character)
                
                if (tipus != "string"):
                    print("\n\tHibás bevitel!")
                else:
                    break

            return new_character
        
    
    def NewWordOutput(self, x, character):

        fajl_tipus = self.AlphaOrInt(self.alap)
        rendez = x[0]
        algoritmus = x[1]

        if (x == "Hiba"):
            print("")       #Nem szeretném mégegyszer ugyanazt kiírni
        else:
            print("")   #Üres sor, hogy átlátható legyen

            if (fajl_tipus == "int"):

                if (rendez == "n" and algoritmus == 1):
                    print(self.SortInt(self.NewWord(character)))
                if (rendez == "n" and algoritmus == 2):
                    print(self.CocktailSortInt(self.NewWord(character)))
                
                if (rendez == "cs" and algoritmus == 1):
                    print(self.ReverseSortInt(self.NewWord(character)))
                if (rendez == "cs" and algoritmus == 2):
                    print(self.ReverseCocktailSortInt(self.NewWord(character)))
            
            if (fajl_tipus == "string"):

                if (rendez == "n" and algoritmus == 1):
                    print(self.SortStr(self.NewWord(character)))
                if (rendez == "n" and algoritmus == 2):
                    print(self.CocktailSortStr(self.NewWord(character)))
                
                if (rendez == "cs" and algoritmus == 1):
                    print(self.ReverseSortStr(self.NewWord(character)))
                if (rendez == "cs" and algoritmus == 2):
                    print(self.ReverseCocktailSorStr(self.NewWord(character)))


r = Rendezes()
r.Beolvas("ki.txt")
r.Listak()

x = r.Input()
r.Output(x)

y = r.NewWordInput()
r.NewWordOutput(x, y)
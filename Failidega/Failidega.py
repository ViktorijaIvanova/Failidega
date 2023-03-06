from Omamoodul import*
laused=[]
while True:
    v=int(input("1-loema failist/n2-salvestama failisse/n3-tekstist kõne/n"))
    if v==1:
        laused=loe_failist("sõna.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("lisa lause:")
        laused.append(line)
        kirjuta_failisse("sõna.txt",laused) 
    elif v==3:
        text=""
        for line in laused:
            text=text+" "+line 
        Heli(text,"et") #text: kõik elemendis jrjendis
        ind=int(input("number:")) #üks element indeksiga ind
        Heli(laused[ind],"et")

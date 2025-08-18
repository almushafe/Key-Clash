from typing import Literal,Tuple
import keyboard as k
import time
keybowrdKeys = Literal["r", "w", "a", "x", "q", "k", "l", "m","up","down"]

class key_Clash :

    def __init__(self,
                 plyer:Tuple[str,str] = ("Name1","Name2") ,
                 keys:Tuple[keybowrdKeys ,keybowrdKeys] = ('s','w'),
                 timestap=0.1
                 ):
        """
            Do players aur unke keys set karta hai.

            Parameters:
            - plyer (Tuple[str, str]) : Player 1 aur Player 2 ke names
            - keys (Tuple[str, str])  : Un ke corresponding keys
            - timestap (float)        : Time delay between key reads
        """
         
        self.plyer = plyer
        self.keys = keys
        self.timestap =timestap
    
    def __str__(self):
        """
        Game info ko readable format mein return karta hai.
        """
        return f"\n\t1. Name : {self.plyer[0]} -> Key : {self.keys[0]}\n\n\t\t -- VS -- \n\n\t2. Name : {self.plyer[1]} -> Key : {self.keys[1]}\n "


class KC(key_Clash):
    def __init__(self, plyer=('Name1', 'Name2'), keys=('w','s'),timestap=0.1):
        """
        KC (Key Clash) class init karta hai with score and keys.

        Inherits from key_Clash.
        """
        super().__init__(plyer, keys,timestap)
        self.firstScore = 0
        self.SecondScore = 0

    def __game_engine(self,oder):
            """
        Game ka main loop chalata hai jab tak 'oder' (condition) True return kare.

        Parameters:
        - oder (function): A lambda ya function jo True ya False return karta hai (e.g., timer check)
        """
            
            while oder():
                try:
                    if k.is_pressed(self.keys[0]):
                        self.firstScore +=1
                        self.SecondScore  = max(0,self.SecondScore -1)
                        print(f"\n\t{self.plyer[0]} vs {self.plyer[1]}\n\n [ {self.firstScore} ]\t<-> [ {self.SecondScore} ]")
                        time.sleep(self.timestap)

                    if k.is_pressed(self.keys[1]):
                        self.SecondScore +=1
                        self.firstScore = max(0,self.firstScore -1)
                        print(f"\n\t{self.plyer[0]}\tvs {self.plyer[1]}\n\n [ {self.firstScore} ]\t<-> [ {self.SecondScore} ]")
                        time.sleep(self.timestap)

                    if k.is_pressed("esc"):
                        if self.firstScore > self.SecondScore:
                            print(f"\n\twon :- {self.plyer[0]} \n\tdefeat -> {self.plyer[1]}")
                        elif self.firstScore < self.SecondScore:
                            print(f"\n\twon :- {self.plyer[1]} \n\tdefeat -> {self.plyer[0]}")
                        elif self.firstScore == self.SecondScore:
                            print("\n Draw ")
                        break
                    time.sleep(self.timestap)

                except KeyboardInterrupt:
                    print("\nGame interrupted.")
                    break



    def start(self,timer=0):
        """
        Game ko start karta hai. Agar timer diya gaya ho to limited time tak chalega,
        warna jab tak ESC dabaya na jaye tab tak chalta rahega.

        Parameters:
        - timer (int or float): Total duration of game in seconds (0 = endless mode)
        """
        if timer > 0:
            start = time.time()
            check = lambda: (time.time() - start) < timer
            self.__game_engine(check)
            if self.firstScore > self.SecondScore:
                print(f"\n\twon :- {self.plyer[0]} \n\tdefeat -> {self.plyer[1]}")
            elif self.firstScore < self.SecondScore:
                print(f"\n\twon :- {self.plyer[1]} \n\tdefeat -> {self.plyer[0]}")
            elif self.firstScore == self.SecondScore:
                print("\n Draw ")
        else:
            self.__game_engine(lambda:True)



if __name__ == "__main__":



    a = key_Clash(plyer=("Muhammad","Abubaker"))
    ae = KC(plyer=('Muhamad',"Abubaker"),keys=("up","w"),timestap=0.1)
    ae.start(10)

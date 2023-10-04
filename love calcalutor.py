print('''          
                        *   *  *   *   *  *    
                        *       * *       *
                         *       *       *   
                           *           *
                             *       *
                               *   *
                                * *             
                                 *''')
print("hello from love calculator where we calculate yor chances and dish out loveeee")
name1 = input("put in the human of your dreams name\n")
print("great name they got there")
name2 = input("i would luv to know your name as well\n")
pair = name1 + name2
Pair = pair.lower()
T = Pair.count("t")
R = Pair.count("r")
U = Pair.count("u")
E = Pair.count("e")
TRUE = T + R + U + E
L = Pair.count("l")
O = Pair.count("o")
V = Pair.count("v")
E = Pair.count("e")
LOVE = L + V + O + E 
combo = LOVE + TRUE
Combo = combo * 10
if Combo <= 40:
    print( f"love isn't meant for the two of you as your love percentage is {Combo}%")
elif Combo <= 60:
    print(f"love might bloom but am afraid it might not last the strong wind of life as your love percentage is {Combo}%")
elif Combo <= 80:
    print(f"oh my your love shall surely stand the test of time as your love percentage is {Combo}%")
elif Combo <= 100:
    print(f"your love is as boundless as the earth{Combo}%")   
else:
    print("you are perfect soulmate nearly like hades and presephone")
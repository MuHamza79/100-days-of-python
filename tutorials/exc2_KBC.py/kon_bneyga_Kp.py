print("Welcome to KBC. You will be asked 5 questions.\n")
print("Answer them correctly and win $10,000")
#questions
que1 = ("Which of the following is the highest mountain peak in Pakistan, famously known as the \"Savage Mountain\"?")
que2 = ("Under whose captaincy did the Pakistan national cricket team win their first-ever ICC Men's Cricket World Cup in 1992?")
que3 = ("Who composed the musical score for the National Anthem of Pakistan (Qaumi Taranah)?")
que4 = ("If you are traveling through Punjab and want to buy the most famous, authentic '''Sohan Halwa''', which city must you visit?")
que5 = ("Which iconic PTV drama from the 1980s gave us unforgettable characters like Kabacha, Zain, and Sanya?")

#answers
ans1 = ["A) Nanga Parbat" , "B) Tirich" , "C) K2" ,"D) Broad Peak"]
ans2 = ["A) Javed Miandad", "B) Imran Khan" , "C) Wasim Akram" , "D) Inzamam-ul-Haq"]
ans3 = ["A) Hafeez Jalandhari" , "B) Mehdi Hassan" , "C) Noor Jehan" , "D) Ahmed Ghulam Ali Chagla"]
ans4 = ["A) Multan" , "B) Lahore" , "C) Faisalabad" , "D) Gujranwala"]
ans5 = ["A) Dhoop Kinare" , "B) Tanhaiyaan" , "C) Alpha Bravo Charlie" , "D) Waris"]

# running the game
Con = True
while Con == True:
    print("Question 1:" , que1)
    print("Options:", ans1)
    print("Choose an option A , B , C , D")
    opt = input("Option: ")
    match opt :
        case 'A' :
            print("Wrong answer") 
            Con = False
        case 'B' : 
            print("Wrong answer")
            Con = False
        case 'C' : 
            print("Correct answer")
            Con = True
        case 'D' : 
            print("Wrong answer")
            Con = False
    if Con == False:
        print("You lose")
        break
    elif Con == True:
        print("Moving on to the next question")
        print("Question 2:" , que2)
        print("Options:", ans2)
        print("Choose an option A , B , C , D")
        opt = input("Option: ")
        match opt :
                case 'A' :
                    print("Wrong answer") 
                    Con = False
                case 'B' : 
                    print("Correct answer")
                    Con = True
                case 'C' : 
                    print("Wrong answer")
                    Con = False
                case 'D' : 
                    print("Wrong answer")
                    Con = False
        if Con == False:
                print("You lose")
                break       
        elif Con == True:
         print("Moving on to the next question")
         print("Question 3:" , que3)
         print("Options:", ans3)
         print("Choose an option A , B , C , D")
         opt = input("Option: ")
         match opt :
                case 'A' :
                    print("Wrong answer") 
                    Con = False
                case 'B' : 
                    print("Wrong answer")
                    Con = False
                case 'C' : 
                    print("Wrong answer")
                    Con = False
                case 'D' : 
                    print("Correct answer")
                    Con = True
        if Con == False:
                print("You lose")
                break 
        elif Con == True:
         print("Moving on to the next question")
         print("Question 4:" , que4)
         print("Options:", ans4)
         print("Choose an option A , B , C , D")
         opt = input("Option: ")
         match opt :
                case 'A' :
                    print("Correct answer") 
                    Con = True
                case 'B' : 
                    print("Wrong answer")
                    Con = False
                case 'C' : 
                    print("Wrong answer")
                    Con = False
                case 'D' : 
                    print("Wrong answer")
                    Con = False
        if Con == False:
                print("You lose")
                break 
        elif Con == True:
         print("Moving on to the next question")
         print("Question 5:" , que5)
         print("Options:", ans5)
         print("Choose an option A , B , C , D")
         opt = input("Option: ")
         match opt :
                case 'A' :
                    print("Wrong answer") 
                    Con = False
                case 'B' : 
                    print("Correct answer")
                    Con = True
                case 'C' : 
                    print("Wrong answer")
                    Con = False
                case 'D' : 
                    print("Wrong answer")
                    Con = False
        if Con == False:
                print("You lose")
                break 
        else: 
            print("Congratulations on winning 10 bands.")
            break
      
  
             
        
        

print("\t\t\t\t \tKaun Banega Crorepati Qize")
print("  \t\t\t\t","\t You Want to start Quize")
print("\t\t\t\t  START",  "\t\t\t", "WAIT")

#in1=input("Enter Opetion:")
QDict={
    "1":"B",
    "2":"C",
    "3":"D",
    "4":"C",
    "5":"D",
}

AR = ["1) CALL TO FRIEND", "2) ASK TO EXPERT", "3) JANTA POLL", "4) PROBABILITY 50-50", "5) Quit", "6) Continue"]

# Function to display friend's contact numbers
def CF():
    print("Friend 1: 7764846389")
    print("Friend 2: 8766847389")
    print("Friend 3: 7964448389")
    print("Friend 4: 9364849389")

# Expert answers and explanations
EXP1 = ["1", "Correct Ans is: B", "Explanation: The pH range of the human body under favorable conditions is 7.0-7.8. Usually, it depends on the part of the body. Saliva is usually about 7.1 to 7.5, blood needs to be 7.35 to 7.45, stomach acid is 1.5 to 3.5, and urine can range from 4.6 to 8.0, depending on what you have been eating or drinking, and how much water you have been drinking. pH is maintained in the body through three important mechanisms; respiratory control, renal control, and buffer systems."]
EXP2 = ["2", "Correct Ans is: C", "Explanation: According to Elton (1939), the term 'Key Industrial animals' for primary consumers as they convert the plant material into animal material. Primary consumers, which is more or less synonymous with 'herbivores,' eat the things that turn sunlight into energy. Secondary consumers are carnivores who eat the primary consumers."]
EXP3 = ["3", "Correct Ans is: D", "Forming of Association is a fundamental right given in the Constitution of India under Article 19(1)(c)"]
EXP4 = ["4", "Correct Ans is: C", "Election to panchayats in the state are regulated by the State Election Commission. State Election Commissioner is the leader of the State Election Commission. He controls Local elections like Panchayats. He's appointed by the governor of that state. State Election Commissioner is nominated by the Governor."]
EXP5 = ["5", "Correct Ans is: D", "The Samkhya School of Philosophy was founded by Kapila. There are six schools of Indian philosophy named Samkhya, Vedanta, Mimansa, Vaisheshik, Nyaya, and Yoga. Samkhya philosophy school doesn't consider God."]



def QN():
    print("1) What is the pH value of the human body?")
    print("A"")","9.2 to 9.8\n"
          "B"")","7.0 to 7.8\n"
          "C"")","6.1 to 6.3\n"
          "D"")","5.4 to 5.6\n")
    # Function to handle lifeline choice
    def lifeline():
        print("Name of lifeline")
        for i in AR:
            print(i)
        Life2 = input("Enter your choice: ")
        L = Life2.strip().lower()
    
        if L == "2" or L == "2) ask to expert" or L == "ask to expert":
            print(EXP1)
        elif L == "3" or L == "3) janta poll" or L == "janta poll":
            print("You have selected Janta Poll")
        elif L == "4" or L == "4) probability 50-50" or L == "probability 50-50":
            print("A, B")
        elif L == "5" or L == "5) quit" or L == "quit":
            print("Thank you...!")
        elif L == "1" or L == "1) call to friend" or L == "call to friend":
            CF()
# Main program
    print("\t\t\t\tDo You Want Lifeline")
    print("\t\t\t\tYES\t\t\tNO")
    Life1 = input("Enter choice: ").strip().lower()
    if Life1 == "yes":
        lifeline()
    Q1=(input("enter option"))
    print("")
    if Q1!=QDict['1']:
        return print("Incorrect Ans","Congratulations you have wone Rs.1,000/-","Correct Ans is:",QDict['1'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.10,00,000/-")
        
        
    
    print("2)Which of the following are called \"Key Industrial animals\"?")
    print("A"")","Producers\n"
          "B"")","Tertiary consumers\n"
          "C"")","Primary consumers\n"
          "D"")","None of these\n")
    # Function to handle lifeline choice
    def lifeline():
        print("Name of lifeline")
        for i in AR:
            print(i)
        Life2 = input("Enter your choice: ")
        L = Life2.strip().lower()
    
        if L == "2" or L == "2) ask to expert" or L == "ask to expert":
            print(EXP2)
        elif L == "3" or L == "3) janta poll" or L == "janta poll":
            print("You have selected Janta Poll")
        elif L == "4" or L == "4) probability 50-50" or L == "probability 50-50":
            print("A, C")
        elif L == "5" or L == "5) quit" or L == "quit":
            print("Thank you...!")
        elif L == "1" or L == "1) call to friend" or L == "call to friend":
            CF()

        # Main program
    print("\t\t\t\tDo You Want Lifeline")
    print("\t\t\t\tYES\t\t\tNO")
    Life1 = input("Enter choice: ").strip().lower()
    if Life1 == "yes":
        lifeline()
    Q2=(input("enter option"))
    if Q2!=QDict['2']:
        return print("Incorrect Ans","Congratulations you have wone Rs.50,000/-","Correct Ans is:",QDict['2'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.25,00,000/-")
        
        
        
    print("3) Forming of Association in India is?")
    print("A"")","Legal Right\n"
          "B"")","Illegal Right\n"
          "C"")","Natural Right\n"
          "D"")","Fundamental Right\n")
    # Function to handle lifeline choice
    def lifeline():
        print("Name of lifeline")
        for i in AR:
            print(i)
        Life2 = input("Enter your choice: ")
        L = Life2.strip().lower()
    
        if L == "2" or L == "2) ask to expert" or L == "ask to expert":
            print(EXP3)
        elif L == "3" or L == "3) janta poll" or L == "janta poll":
            print("You have selected Janta Poll")
        elif L == "4" or L == "4) probability 50-50" or L == "probability 50-50":
            print("B, D")
        elif L == "5" or L == "5) quit" or L == "quit":
            print("Thank you...!")
        elif L == "1" or L == "1) call to friend" or L == "call to friend":
            CF()

# Main program
    print("\t\t\t\tDo You Want Lifeline")
    print("\t\t\t\tYES\t\t\tNO")
    Life1 = input("Enter choice: ").strip().lower()
    if Life1 == "yes":
        lifeline()
    Q3=(input("enter option"))
    if Q3!=QDict['3']:
        return print("Incorrect Ans","Congratulations you have wone Rs.25,00,000/-","Correct Ans is:",QDict['3'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.50,00,000/-")
        
        
    
    print("4)Elections to panchayats in state are regulated by?")
    print("A"")","Gram panchayat\n"
          "B"")","Nagar Nigam\n"
          "C"")","Election Commission of India\n"
          "D"")","State Election Commission\n")
    # Function to handle lifeline choice
    def lifeline():
        print("Name of lifeline")
        for i in AR:
            print(i)
        Life2 = input("Enter your choice: ")
        L = Life2.strip().lower()
    
        if L == "2" or L == "2) ask to expert" or L == "ask to expert":
            print(EXP4)
        elif L == "3" or L == "3) janta poll" or L == "janta poll":
            print("You have selected Janta Poll")
        elif L == "4" or L == "4) probability 50-50" or L == "probability 50-50":
            print("B, C")
        elif L == "5" or L == "5) quit" or L == "quit":
            print("Thank you...!")
        elif L == "1" or L == "1) call to friend" or L == "call to friend":
            CF()

    # Main program
    print("\t\t\t\tDo You Want Lifeline")
    print("\t\t\t\tYES\t\t\tNO")
    Life1 = input("Enter choice: ").strip().lower()
    if Life1 == "yes":
        lifeline()
    Q4=(input("enter option"))
    if Q4!=QDict['2']:
        return print("Incorrect Ans","Congratulations you have wone Rs.50,00,000/-","Correct Ans is:",QDict['4'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.75,00,000/-")
        
        
        
   
    print("5)The Samkhya School of Philosophy was founded by?")
    print("A"")","Gautam Buddha\n"
          "B"")","Mahipala\n"
          "C"")","Gopala\n"
          "D"")","Kapila\n")
    # Function to handle lifeline choice
    def lifeline():
        print("Name of lifeline")
        for i in AR:
            print(i)
        Life2 = input("Enter your choice: ")
        L = Life2.strip().lower()
    
        if L == "2" or L == "2) ask to expert" or L == "ask to expert":
            print(EXP5)
        elif L == "3" or L == "3) janta poll" or L == "janta poll":
            print("You have selected Janta Poll")
        elif L == "4" or L == "4) probability 50-50" or L == "probability 50-50":
            print("A, D")
        elif L == "5" or L == "5) quit" or L == "quit":
            print("Thank you...!")
        elif L == "1" or L == "1) call to friend" or L == "call to friend":
            CF()

# Main program
    print("\t\t\t\tDo You Want Lifeline")
    print("\t\t\t\tYES\t\t\tNO")
    Life1 = input("Enter choice: ").strip().lower()
    if Life1 == "yes":
        lifeline()
    Q5=(input("enter option")) 
    if Q5!=QDict['5']:
        return print("Incorrect Ans","Congratulations you have wone Rs.1,000/-","Correct Ans is:",QDict['5'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.1,00,00,000/-")
        print("\t\t\t\t\tYOU ARE A CROREPATI")
        
        
#u_in=str(input("Enter Option:"))
def men():
      u_in=str(input("Enter Option:"))
      #X=u_in.lower()
      if u_in.lower()=="start":
            QN()
      else:
            print("Thank You.......!")
 
 
men()
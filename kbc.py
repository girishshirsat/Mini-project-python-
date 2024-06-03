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

def QN():
    print("1) What is the pH value of the human body?")
    print("A"")","9.2 to 9.8\n"
          "B"")","7.0 to 7.8\n"
          "C"")","6.1 to 6.3\n"
          "D"")","5.4 to 5.6\n")
    Q1=(input("enter option"))
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
    Q2=(input("enter option"))
    if Q2!=QDict['2']:
        return print("Incorrect Ans","Congratulations you have wone Rs.1,000/-","Correct Ans is:",QDict['2'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.25,00,000/-")
    
    print("3) Forming of Association in India is?")
    print("A"")","Legal Right\n"
          "B"")","Illegal Right\n"
          "C"")","Natural Right\n"
          "D"")","Fundamental Right\n")
    Q3=(input("enter option"))
    if Q3!=QDict['3']:
        return print("Incorrect Ans","Congratulations you have wone Rs.1,000/-","Correct Ans is:",QDict['3'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.50,00,000/-")
    
    print("4)Elections to panchayats in state are regulated by?")
    print("A"")","Gram panchayat\n"
          "B"")","Nagar Nigam\n"
          "C"")","Election Commission of India\n"
          "D"")","State Election Commission\n")
    Q4=(input("enter option"))
    if Q4!=QDict['2']:
        return print("Incorrect Ans","Congratulations you have wone Rs.1,000/-","Correct Ans is:",QDict['4'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.75,00,000/-")
    
    print("5)he Samkhya School of Philosophy was founded by?")
    print("A"")","Gautam Buddha\n"
          "B"")","Mahipala\n"
          "C"")","Gopala\n"
          "D"")","Kapila\n")
    Q5=(input("enter option")) 
    if Q5!=QDict['5']:
        return print("Incorrect Ans","Congratulations you have wone Rs.1,000/-","Correct Ans is:",QDict['5'])
    else:
        print("Correct")
        print("Cong ratulations you have wone Rs.1,00,00,000/-")
        print("YOU ARE A CROREPATI")
        
'''print("\t\t\t\t \tKaun Banega Crorepati Qize")
print("  \t\t\t\t","\t You Want to start Quize")
print("\t\t\t\t  START",  "\t\t\t", "WAIT")'''

#u_in=str(input("Enter Option:"))
def men():
      u_in=(input("Enter Option:"))
      #X=u_in.lower()
      if u_in=="START":
            QN()
      else:
            print("Thank You.......!")
 
 
men()
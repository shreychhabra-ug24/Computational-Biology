#assignment2
def cmb3():
    total_students = 13

    # Initial number of bored and attentive students
    bored_students = total_students #start by assuming that every student is bored, but this also provides the same answer if we start with a different number. 
    attentive_students = 0
    for _ in range(45): #given time is 90 minutes
        #number of students becoming bored and attentive every 2 minutes
        new_attentive_students = float(bored_students * 0.25)
        new_bored_students = float(attentive_students * 0.20)
        #this updates the values in every loop (every 2 minutes)
        bored_students -= new_attentive_students    #students who were bored and became attentive
        attentive_students += new_attentive_students    #students who were attentive and remained attentive
        attentive_students -= new_bored_students    #students who were attentive and became bored
        bored_students += new_bored_students    #students who were bored and remained bored

    # condition to check if all students are attentive at the end of the class
    all_attentive = bored_students == 0  #for a booleon condition, provides a true/false value
    
    # Print the number of bored and attentive students and whether all students are attentive
    print("The number of bored students is: ", bored_students)
    print("The number of attentive students is: ", attentive_students)
    print("Are all students attentive? ", all_attentive)

if __name__ == "__main__":
    cmb3()



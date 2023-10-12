
# IDEA
"""
- Create a collection of Hogwart students with their details in a dictionary
- Details inlcude- name, house, patronus_charm, favourite_spell, O.W.L
- User provides the name and all details of that particular student are provided
"""

# PSEUDO-CODE
"""
- Create `Student` class with above listed properties
- Define method `save_student_info()`
- Define method `get_student_info()`
"""


class Student:  
    def __init__(self, name, house, owl):
        
        self.name = name
        self.house = house
        # self.patronus_charm = patronus_charm
        # self.favourite_spell = favourite_spell
        # patronus_charm, favourite_spell,
        self.owl = owl

        self.register = {
            "name": self.name,
            "house": self.house,
            # "patronus_charm": self.patronus_charm,
            # "favourite_spell": self.favourite_spell,
            "O.W.L": self.owl
            }

        return None


    def get_student_info(self, name):
        if name in self.register:
            for key, val in self.register.items():
                print(f"{key} : {val}")
                return None
        return self.register

    def save_student_info(self):
        
        print("Successfully saved student data.")
        return None



def main():

    exit = False

    while(exit == False):

        user_request = input("\nWhat would you like to do : \nAdd student data - press 'a'\nExit - press 'Enter'\n")
                          
        if user_request == "a":
            # user enters student data
            print("---Welcome to Hogwarts Student Register---\n")
            name = input("Name : ")
            house = input ("House : ")
            # patronus_charm = input("Patronus Charm : ")
            # favourite_spell = input("Favourite Spell : ")
            # patronus_charm=patronus_charm, favourite_spell=favourite_spell,
            owl = input ("O.W.L : ")
            
            # save student data
            student = Student(name=name, house=house, owl=owl)
            student.save_student_info()
        
            name = input("\nEnter student's name for specific data or press 'Enter' to exit : ")
            if type(student.get_student_info(name=name)) == dict:
                student.register = student.get_student_info(name=name)
                for key, val in student.register.items():
                    print(f"{key} : {val}")
            else:
                student.get_student_info(name=name)

        else:
            exit = True
            print("Well have a good day, then! See you!")

    return None




if __name__ == "__main__":
    main()
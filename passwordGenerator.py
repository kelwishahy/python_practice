# PASSWORD GENERATOR ALGORITHM
# Author: Kareem El-Wishahy
# GithubID: kelwishahy

#Imports
import string
from secrets import randbelow

def main():
    #Create the lists that contain all possible characters
    alphabet = list(string.ascii_letters)
    alpha_lower = list(string.ascii_lowercase)
    alpha_upper = list(string.ascii_uppercase)
    characters = ['!', '@', '#', '$', '%', '&', '*', '_']
    randomWords = ['dog', 'cat', 'xylephone', 'computer', 'monday', 'elephant',
                  'telephone','python', 'communicate', 'june', 'porsche',
                   'friendly', 'internet', 'year', 'notebook', 'macaroni',
                   'metric', 'telekinesis', 'genie', 'disney', 'buzz', 'front',
                  'park', 'electric']

    
    #Prompt the user for their input
    strengthPrompt = "\n\nSelect 's' for a strong password"
    strengthPrompt += "\nor 'w' for a weak password: "
    
    selectedStrength = input(strengthPrompt)
    selectedStrength = selectedStrength.lower()

    while (selectedStrength != 'w' and selectedStrength != 's'):
        print("\n\nERROR: Please select 's' or 'w'\n")
        selectedStrength = input(strengthPrompt)
        selectedStrength = selectedStrength.lower()

    if (selectedStrength == 's'):
        lengthPrompt = "\n\nSelect a password length between 8 and 16: "

        selectedLength = input(lengthPrompt)
        selectedLength = int(selectedLength)

        while (selectedLength < 8 or selectedLength > 16):
            print("\n\nERROR: Please select a valid password length: ")
            selectedLength = input(lengthPrompt)
            selectedLength = int(selectedLength)

        password_parameters = {
            'STRENGTH' : selectedStrength,
            'LENGTH': selectedLength
        }
        print(password_parameters)

    else:
        password_parameters = {
            "STRENGTH" : selectedStrength
        }
        print(password_parameters)



    #Begin generating password
    if (password_parameters.get("STRENGTH") == 'w'):
        password = randomWords[randbelow(len(randomWords))] 
        password += str(randbelow(10))
        password += str(randbelow(10))
        
        resultMessage = "\n\nYour new password is: "
        resultMessage += password
        print(resultMessage)

    else:
        password = ""
        for i in range(0, password_parameters.get("LENGTH")):
            randomNum = randbelow(10000)
            if (randomNum % 5 == 0):
                password += alphabet[randbelow(len(alphabet))]
            elif (randomNum % 5 == 1):
                password += characters[randbelow(len(characters))]
            elif (randomNum % 5 == 2):
                password += str(randbelow(10))
            elif (randomNum % 5 == 3):
                password += alpha_lower[randbelow(len(alpha_lower))]
            else:
                password += alpha_upper[randbelow(len(alpha_upper))]

        resultMessage = "\n\nYour new password is: "
        resultMessage += password
        print(resultMessage)
    

    #Write the newly generated password to an external text file
    pw = password
    pw += "\n"
    file = open("passwords.txt", "a+")
    file.write(pw)
    file.close()


if __name__ == "__main__":
    main()

#TODO: Create a letter using starting_letter.txt
def personalize_letter(name):
    new_string = ""
    with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
        new_letter = letter.readlines()
        greeting = new_letter[0].split(" ")
        greeting[1] = f" {name},\n"
        new_letter[0] = new_string.join(greeting)
        with open(f"ReadyToSend/{name}_letter", "w") as file:
            for line in new_letter:
                file.write(line)



with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as people:
    all_people = people.readlines()
    for person in all_people:
        personalize_letter(person.strip())
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
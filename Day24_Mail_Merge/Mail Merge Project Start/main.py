
def personalize_letter(name):
    new_string = ""
    with open("Input/Letters/starting_letter.txt") as letter:
        new_letter = letter.readlines()
        greeting = new_letter[0].split(" ")
        greeting[1] = f" {name},\n"
        new_letter[0] = new_string.join(greeting)
        with open(f"Output/ReadyToSend/{name}_letter", "w") as file:
            for line in new_letter:
                file.write(line)



with open("Input/Names/invited_names.txt") as people:
    all_people = people.readlines()
    for person in all_people:
        personalize_letter(person.strip())
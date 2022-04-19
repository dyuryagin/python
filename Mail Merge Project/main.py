#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

is_working = True
output_file_path = "./Output/ReadyToSend/"

with open("./Input/Names/invited_names.txt") as names_file:
    while is_working:
        name = names_file.readline().rstrip()
        if name != "":
            output_file_name = output_file_path \
                               + f"letter_for_{name if len(name.split(' ')) == 1 else '_'.join(name.split(' ')) }.txt"
            with open("./Input/Letters/starting_letter.txt") as template_file:
                template = template_file.read()
                with open(output_file_name, mode="w") as letter_file:
                    letter_file.write(template.replace("[name]", name))
        else:
            is_working = False

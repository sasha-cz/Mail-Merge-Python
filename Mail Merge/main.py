PLACEHOLDER = "[name]"

# Get hold of the content in your 'sample_letter.txt'.
with open("./Input/Letters/sample_letter.txt") as letter:
    content = letter.read()

# Make a list from the lines of a second txt.file (e.g. 'names.txt').
# Each line in 'names.txt' should contain your replacement text for each letter.
with open("./Input/Replacements/names.txt") as names_file:
    name_list = names_file.readlines()

# Get hold of the replacement text from the list (here 'name_list'), reformat that text, create a letter for each text,
# save the letters in a directory of your choice and write the new content with the replaced sections to each letter.
    for name in range(len(name_list)):
        formatted_name = name_list[name].strip()
        personalized_content = content.replace(PLACEHOLDER, formatted_name)
        with open(f"./Output/ReadyToSend/{formatted_name}.txt", mode="w") as new_letter:
            new_letter.write(personalized_content)

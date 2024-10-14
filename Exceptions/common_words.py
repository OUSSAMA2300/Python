def common_word(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        common = contents.lower().count('the')
        print(f"The word 'the' apppeared {common} times in {filename}")

filenames = ['collection_of_Hawaiian_antiquities_and folk-lore.txt',
             'presidential_addresses_and_State_papers.txt',
             'the_story_of_the_universe.txt']


for filename in filenames:
    common_word(filename)
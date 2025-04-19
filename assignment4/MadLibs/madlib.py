def mad_libs():
    print("Lets play madlib!")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_obj = input("Give me a funny objective: ")
    random_object = input("Give me a random object: ")
    animal = input("Give me a animal: ")
    action_verb = input("Give me a action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")

    story = f'''
    Once upon a time, there was a person named {name}.
    They went to {place} carrying a {funny_obj} and a {random_object}. 
    Suddenly, a {animal} appeared and started to {action_verb}. 
    {name} yelled, "{funny_exclamation}!" and ran away, leaving the {animal} confused but impressed.'''

    print("\n Here is your Mad Libs story: " )
    print(story)
if __name__ == '__main__':
    mad_libs()
    
# Invite some people to dinner
# guest list
letters_to_words = {
    'a': "Alpha", 'b': "Bravo", 'c': "Charlie", 'd': "Delta",
    'e': "Echo", 'f': "Foxtrot", 'g': "Golf", 'h': "Hotel",
    'i': "India", 'j': "Juliet", 'k': "Kilo", 'l': "Lima",
    'm': "Mike", 'n': "November", 'o': "Oscar", 'p': "Papa",
    'q': "Quebec", 'r': "Romeo", 's': "Sierra", 't': "Tango",
    'u': "Uniform", 'v': "Victor", 'w': "Whiskey", 'x': "X-Ray",
    'y': "Yankee", 'z': "Zulu"
}

# print message to each guest
print("\n\tInvitations!")
guests = []
guests.append(letters_to_words['a'])
guests.append(letters_to_words['b'])
guests.append(letters_to_words['c'])
print(guests)
msg = f"Hello, {letters_to_words['a'].title()}!"
print(msg)
msg = f"Hello, {letters_to_words['b'].title()}!"
print(msg)
msg = f"Hello, {letters_to_words['c'].title()}!"
print(msg)

# list of people who cannot attend
print("\n\tDeclined!")

# Remove the last item (JavaScript)
removed_language = guests.pop()
print(removed_language,"declined")
print("\n\tAttending")
print(guests)

# alpha and bravo can't make it! Let's invite 
print("\n\tUpdated guest list!")
guests.append(letters_to_words['d'])
guests.append(letters_to_words['e'])
print(guests)

# print message to new guest list
print("\n\tUpdated Invitations")
msg = f"Hello, {guests[0].title()}!"
print(msg)
msg = f"Hello, {guests[1].title()}!"
print(msg)
msg = f"Hello, {guests[2].title()}!"
print(msg)
msg = f"Hello, {guests[3].title()}!"
print(msg)

# we got a bigger table
print("\n\tWe got a bigger table!")
print("\n\tNew guest list!")

guests.insert(0, letters_to_words['z'])
guests.insert(3, letters_to_words['y'])
guests.append(letters_to_words['x'])
print(guests)
# letters_to_words['z'] = "arnold"
msg = f"Hello, {guests[0].title()} we have room"
print(msg)
msg = f"Hello, {guests[1].title()} we have room"
print(msg)
msg = f"Hello, {guests[2].title()} we have room"
print(msg)
msg = f"Hello, {guests[3].title()} we have room"
print(msg)
msg = f"Hello, {guests[4].title()} we have room"
print(msg)
msg = f"Hello, {guests[5].title()} we have room"
print(msg)
msg = f"Hello, {guests[6].title()} we have room"
print(msg)

print("\n\tWe can only invite two")
removed_language = guests.pop()
print(removed_language,"is uninvited")
removed_language = guests.pop()
print(removed_language,"is uninvited")
removed_language = guests.pop()
print(removed_language,"is uninvited")
removed_language = guests.pop()
print(removed_language,"is uninvited")
removed_language = guests.pop()
print(removed_language,"is uninvited")
print(guests)
del(guests[0])

del(guests[0])
print(guests)

def convert_to_phonetic(word):
    phonetic_word = ' '.join(letters_to_words.get(letter.lower(), letter) for letter in word)
    return phonetic_word

if __name__ == '__main__':
    user_word = input("Enter a word: ")
    phonetic_result = convert_to_phonetic(user_word)
    print(f"Phonetic code for '{user_word}': {phonetic_result}")
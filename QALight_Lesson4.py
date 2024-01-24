s = "Hello World!"
print(s[0], s[1], s[2], s[3], s[4])

s = "Hello World!"
for elem in s:
    print(elem)

n = "Anastasiia Ovcharenko"
#    0123456789
print(n[11], n[12], n[17], n[16]) #over
print(n[3], n[4], n[5], n[16]) #star
print(n[3], n[14], n[2], n[16], n[19]) #shark


print(s[0:5]) #Hello
print(s[6:11]) #World
print(s[:5]) #Hello
print(s[6:]) #World!
print(s[::-1]) #!dlroW olleH

new_word = s[6:9] + s[10]
print(new_word)

print(len(s))

s = "Hello World!"
count = 0
letter = "l"
for elem in s:
    if elem == letter:
        count = count+1
print(count)

print(s.count(letter))


q = 'dfdffg12345'


digits = "0123456789"
letters = "qwertyuiopasdfghjklzxcvbnm"
digit_count = 0
letter_count = 0

for element in q:
    if element in digits:
        digit_count = digit_count+1
    elif element in letters:
        letter_count = letter_count + 1
print(f"Digits: {digit_count}, letters: {letter_count}")



#task3
# text = "The original Star Wars film was a huge success for 20th Century Fox and was credited with reinvigorating the company! Within three weeks of the film's release, the studio's stock price doubled to a record high! Prior to 1977, 20th Century Fox's greatest annual profits were $37 million, while in 1977, the company broke that record by posting a profit of $79 million! The franchise helped Fox change from an almost bankrupt production company to a thriving media conglomerate; with over $10.3 billion in worldwide box office receipts, Star Wars is the second-highest-grossing film franchise of all time. Star Wars fundamentally changed the aesthetics and narratives of Hollywood films, switching the focus of Hollywood-made films from deep, meaningful stories based on dramatic conflict, themes, and irony to sprawling special-effects-laden blockbusters! This also changed the Hollywood film industry in fundamental ways! Before Star Wars, special effects in films had not appreciably advanced since the 1950s! The commercial success of Star Wars created a boom in state-of-the-art special effects in the late 1970s; along with Jaws, Star Wars started the tradition of the summer blockbuster film in the entertainment industry, where films open on many screens at the same time, and profitable franchises are important. It created the model for the major film trilogy and showed that merchandising rights on a film could generate more money than the film itself did. Film critic Roger Ebert wrote in his book \"The Great Movies\" \"Like The Birth of a Nation and Citizen Kane, Star Wars was a technical watershed that influenced many of the movies that came after! \"It began a new generation of special effects and high-energy motion pictures; the film was one of the first films to link genres together to invent a new, high-concept genre for filmmakers to build upon. Finally, along with Steven Spielberg's Jaws, it shifted the film industry's focus away from personal filmmaking of the 1970s and towards fast-paced, big-budget blockbusters for younger audiences. Some critics have blamed Star Wars and Jaws for \"ruining\" Hollywood by shifting its focus from \"sophisticated\" films such as The Godfather, Taxi Driver, and Annie Hall to films about spectacle and juvenile fantasy; also, for the industry shift from stand-alone, one and done films, towards blockbuster franchises with multiple sequels and prequels! One such critic, Peter Biskind, complained; \"When all was said and done, Lucas and Spielberg returned the 1970s audience, grown sophisticated on a diet of European and New Hollywood films, to the simplicities of the pre-1960s Golden Age of movies... They marched backward through the looking-glass.\"In an opposing view, Tom Shone wrote that through Star Wars and Jaws, Lucas and Spielberg \"didn't betray cinema at all: they plugged it back into the grid, returning the medium to its roots as a carnival sideshow, a magic act, one big special effect\"; which was \"a kind of rebirth.\" The original Star Wars trilogy is widely considered one of the best film trilogies in history! Numerous filmmakers have been influenced by Star Wars, including Damon Lindelof, Dean Devlin, Roland Emmerich, John Lasseter, David Fincher, Joss Whedon, John Singleton, Kevin Smith, and later Star Wars directors J. J. Abrams and Gareth Edwards. Lucas's concept of a \"used universe\" particularly influenced Ridley Scott's Blade Runner (1982) and Alien (1979), James Cameron's Aliens (1986) as well as The Terminator (1984), George Miller's Mad Max 2 (1981), and Peter Jackson's The Lord of the Rings trilogy (2001–2003). Christopher Nolan cited Star Wars as an influence when making the 2010 blockbuster film Inception!"
# end_symb = "!.?"
# sentence_count = 0
# for symbols in text:
#     if symbols in end_symb:
#         sentence_count = sentence_count + 1
# print(f"Quantity of sentences is {sentence_count}")

#task1
# users_text = input(str("Please enter your string: "))
# users_text_without_gap = users_text.replace(' ', '')
# users_text_low = users_text_without_gap.lower()
# users_text_without_symbols = (users_text_low
#                               .replace(',', '')
#                               .replace('!', '')
#                               .replace('?', '')
#                               .replace('\'', ''))
# rev_users_text = users_text_without_symbols[::-1]
# if rev_users_text == users_text_without_symbols:
#     print(f"True")
# else:
#     print(f"False")


#task2
user_text = input(str("Please enter a text: "))
res_words = input(str("Please enter reserved words: "))

# word_in_text = user_text.find(res_words)
text_without_delimiters = user_text.split()

for text_without_delimiters in user_text:
    print(text_without_delimiters)
    if text_without_delimiters in res_words:
        updated_text = text_without_delimiters.upper()
        print(updated_text)
        # update_word = user_text.replace(res_words, updated_text)
        # print(update_word)


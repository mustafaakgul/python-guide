

name = input("Enter name:  ")
print("welcome " + name)

lives = 10
secret_word = "metallica"
guess_string_global = ""

while lives > 0:

	character_left = 0

	for character in secret_word:

		if character in guess_string_global:
			print(character)
		else:
			print("-")
			character_left += 1

	if character_left ==0:
		print("u won")
		break

	guess = input("Guess a word")
	guess_string_global = guess

	if guess in secret_word:
		continue
	else:
		lives = lives - 1
		print("Wrong guess!")
		print(f"U have {lives} left")

		if lives == 0:
			print("u died!")
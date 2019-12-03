from lesson_if import discounted   


#for number in range(3):
#    print(f"Привет мир {number}!")

#example_string = "Я изучаю язык python"

#for word in example_string.split():
#    print(f'Длина слова"{word}":{len(word)}')

#for letter in "python":
#    print(letter.upper())

#students_scores = [1, 21, 19, 6, 5]
#print(f"Средняя оценка: {sum(students_scores)/len(students_scores)}")

#scores_sum = 0
#for score in students_scores:
#    scores_sum += score
#    print(scores_sum)

#print(f"Средняя оценка: {scores_sum/len(students_scores)}")

stock = [
		{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

for phone in stock:
    phone["final price"] = discounted(phone ["price"], phone ["discount"], name=phone["name"])

print(stock)
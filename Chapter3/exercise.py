person = {"name": "Jack", "age": 26}
person_summary = [
	f"The person's {key} is {value}"
	for key, value in person.items()
]
# print(type(person_summary))
# print(person_summary)


# Dict comprehension 
numbers = [-1, 7, 3, 111, 11]
inverted_numbers_in_a_dict = {
	number: 1/number
	for number in numbers
	if number != 0
}
#print(inverted_numbers_in_a_dict)
#print(inverted_numbers_in_a_dict[11])

# Set comprehension
inverted_numbers_in_a_set = {
	1/number
	for number in numbers
	if number != 0
}
print(inverted_numbers_in_a_set)
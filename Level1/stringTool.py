string_input = input("Enter a sentence:")

print(f"""
Uppercase : {string_input.upper()}
Lowercase : {string_input.lower()}
Titlecase : {string_input.title()}

Total cahrs: {len(string_input)}
Total words: {len(string_input.split(" "))}
Reversed : {string_input[::-1]}
""")


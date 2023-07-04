name = input("Enter your name: ")
lang = input("Greeting language (es, fr, en): ")

def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print(greet(lang), name)

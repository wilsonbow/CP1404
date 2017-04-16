
from Prac07.programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)

my_languages = [ruby, python, vb]
print("The dynamically typed languages are:")
for language in my_languages:
    if language.typing == "Dynamic":
        print(language.name)


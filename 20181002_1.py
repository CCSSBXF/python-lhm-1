languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
for name,language in languages.items():
    print(name.title()+"'s favorite language is "+language.title()+'.')
print('\n')
for name in languages.keys():
    print(name.title())
print('\n')
for name in sorted(languages.keys(),reverse=True):
    print(name.title())
print('\n')
for language in languages.values():
    print(language.title())
print('\n')
for language in set(languages.values()):
    print(language.title())
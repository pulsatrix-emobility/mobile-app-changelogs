import json

newVersion = {
    'version': '',
    'de': {
        'releaseDate': '',
        'changeLog': ''
    },
    'en': {
        'releaseDate': '',
        'changeLog': ''
    }
}

changeLogs = {}
with open("./changeLogs.json", "r") as outfile:
    changeLogs = json.load(outfile)

OS = ''
while not OS in ['iOS','android']:    
    print()
    print()
    print('1. iOS')
    print('2. Android')
    print()
    OS = ['iOS','android'][int(input('Für welche Platform ist dieses Update? ')) - 1]
print()
version = ''
while version == '':
    version = str(input('Welche Version hat das Update? '))
    print()
releaseDate = ''
while len(releaseDate.split('.')) != 3:
    releaseDate = str(input('Wann kommt das update raus? (dd.mm.yyyy)\n'))
    print()
de = ''
while de == '':
    de = str(input('Was ändert sich in diesem Update? (DE)\n\n'))
    print()
en = ''
while en == '':
    en = str(input('Was ändert sich in diesem Update? (EN)\n\n'))
    print()

print()
print()
print()
print('Stimmen die folgenden Angeben?')
print()
print(f'Platform: {OS}')
print(f'Version: {version}')
print(f'Erscheinungsdatum: {releaseDate}')
print(f'Änderungen: (DE)')
print()
print(de)
print()
print()
print(f'Änderungen: (EN)')
print()
print(en)
print()
print('(y/n)')
ok = 'y' in str(input('')).lower()

if ok == False:
    exit()

newVersion = {
    'version': version,
    'de': {
        'releaseDate': releaseDate,
        'changeLog': de
    },
    'en': {
        'releaseDate': f'{releaseDate.split(".")[1]}/{releaseDate.split(".")[0]}/{releaseDate.split(".")[2]}',
        'changeLog': en
    }
}

newOS = {
    changeLogs['current'][OS]['version']: {
        'de': changeLogs['current'][OS]['de'],
        'en': changeLogs['current'][OS]['en'],
    }
}

for changeLog in changeLogs[OS]:
    newOS[changeLog] = changeLogs[OS][changeLog]

changeLogs['current'][OS] = newVersion

changeLogs[OS] = newOS

print(json.dumps(changeLogs, indent=4))


with open("./changeLogs.json", "w") as outfile:
    outfile.write(json.dumps(changeLogs, indent=4))
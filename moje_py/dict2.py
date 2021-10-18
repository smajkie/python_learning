current_users = ['Admin', 'root', 'Master', 'joPh', 'MIni']
new_users = ['ala', 'bob', 'Joph', 'MINI', 'alice']
pusta = ['a']

if pusta:
    print('Cos tu jest')
else:
    print('Nie ma nic')

lower_current_users = [user.lower() for user in current_users]

for nowy in new_users:
    if nowy.lower() in lower_current_users:
        print(f'Ej kolego {nowy} ty to juz masz swojego usera')
    else:
        print(f'Spoko {nowy} dodajemy Cie!')

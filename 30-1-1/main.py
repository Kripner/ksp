database = [
    ('a', '1'),
    ('c', '1'),
    ('c', '3'),
    ('d', '3'),
    ('d', '8'),
    ('e', '4')
]
names, emails = {}, {}

for name, email in database:
    name_entry = names.setdefault(name, [[], False])
    email_entry = emails.setdefault(email, [[], False])

    name_entry[0].append(email_entry)
    email_entry[0].append(name_entry)


def count(start_name):
    start_name[1] = True
    return len(start_name[0]) + sum([count(n)
                                     for e in start_name[0]
                                     for n in e[0] if not n[1]])


for name in names:
    if not names[name][1]:
        print(f'{name}: {count(names[name])}')

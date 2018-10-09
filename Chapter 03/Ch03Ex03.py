from collections import namedtuple

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = namedtuple("User", "username forename middlename surname id")


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-". "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count+=1
    usernames.add(username)
    return username


def process_line(line, usernames):
    fields = line.split(':')
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0])
        sys.exit()

        usernames = set()
        users = {}
        for filename in sys.argv[1:]:
            for line in open(filename, encoding="utf8"):
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(), user.id)] = user
        print_users(users)


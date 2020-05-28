n = int(input())
s = set(map(int, input().split()))
number_of_commands = int(input())
for _ in range(number_of_commands):
    command = list(input().split())
    string = ''
    string = "s." + command[0] + \
        "(" + (command[1] if len(command) > 1 else '') + ")"
    exec(string)
print(sum(s))

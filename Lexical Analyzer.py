N = int(input())
variables = []
for _ in range(N):
    stmt = input()
    assignmentIndex = stmt.index('=')
    variables.append(stmt[0:assignmentIndex])
print(len(set(variables)))
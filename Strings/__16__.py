# All permutations of a string in a lexicographic order, without recursion

def generate_perms(s, l, r, result):
    if l == r:
        perm = ''.join(s)
        if perm not in result:
            result.append(perm)
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]  # swap
            generate_perms(s, l+1, r, result)
            s[l], s[i] = s[i], s[l]  # backtrack


string = input("Enter A String: ")
str_list = []
generate_perms(list(string), 0, len(string)-1, str_list)

print("\nAll unique permutations:")
for perm in str_list:
    print(perm)


# GPT Generated!!!
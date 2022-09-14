#player 1
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#points=[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p,  q, r, s, t, u, v, w, x, y, z]
points=[1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
count = []

for x in range (2):
    user_input = input(": ")
    list_input = list(user_input)
    index = 0
    tally = 0

    for letters in letters:
        index += 1
        for i in range(len(list_input)):
            if list_input[i] == letters:
                act_index = index -1
                points_index = points[act_index]
                tally = points_index + tally
    print(tally)
    count.append(tally)
    print(count)

if count[0] > count[1]:
    print("Player 1 is the winner!")
elif count[0] < count[1]:
    print("Player 2 is the winner!")
else:
    print("It's a tie!")
def movie_ticket(q):
    initial_amount = 0
    for each in q:
        change = each - 25
        if change == 0:
            initial_amount += each
            continue
        elif change <= initial_amount:
            initial_amount -= change
        else:
            return "NO"
    return "YES"

if __name__ == '__main__':
    queue = input("Enter the ammount as space separated: ").split()
    queue = map(lambda x:int(x),queue)
    ans = movie_ticket(queue)
    print(ans)
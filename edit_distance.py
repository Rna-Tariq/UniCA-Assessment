def edit_distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    
    cost = 0 if s[-1] == t[-1] else 1

    d1 = edit_distance(s[:-1], t) + 1
    d2 = edit_distance(s, t[:-1]) + 1
    d3 = edit_distance(s[:-1], t[:-1]) + cost 

    return min(d1, d2, d3)

def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    
    distance = edit_distance(s1, s2)
    print(f"The edit distance between '{s1}' and '{s2}' is {distance}")

if __name__ == "__main__":
    main()

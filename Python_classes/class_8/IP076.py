def find_all(keyword, text):
    positions = []
    start = 0
    while start < len(text):
        pos = text.find(keyword, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions


print(find_all("stark", "robb stark and sansa stark are stark brothers"))
print(find_all("snow", "winter is coming"))
print(find_all("ana", "banana ananas"))
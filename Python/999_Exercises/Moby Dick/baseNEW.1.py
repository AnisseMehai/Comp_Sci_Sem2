sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
cout = 0

for i in range(0, len(sentence)):
    if sentence[i:i+5] == "whale":
        count = count + 1





with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        ##YOUR CODE GOES HERE

f.close()

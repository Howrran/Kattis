'''
hi this is price for today
today is a good day
hi cem this is schedule for today
biggest sale today
lowest price for today
good day cem
price for today
biggest price
'''

# H = ['hi this is price for today', 'today is a good day', 'hi cem this is schedule for today']
# S = ['biggest sale today', 'lowest price for today']

H = []
S = []
N, M, K = map(int, input().split())

for _ in range(N):
    H.append(input())

for _ in range(M):
    S.append(input())

words = dict()

for sentence in H:
    for word in sentence.split():
        if word in words:
            words[word][0] += 1
        else:
            words[word] = [1,0]

for sentence in S:
    for word in sentence.split():
        if word in words:
            words[word][1] += 1
        else:
            words[word] = [0,1]

c1, c2 = 0, 0
for i in words:
    c1 += words[i][0]
    c2 += words[i][1]

answers = []

if M + N == 0:
    for _ in range(K):
        print(0)
else:
    for _ in range(K):

        new_word = input()
        chiselnyk, znamenik =  1, 1
        chiselnyk = 1 if c2 != 0 else 0

        for word in new_word.split():
            if word in words:
                if c2 != 0: chiselnyk *= words[word][1] / c2
                if c1 != 0: znamenik *= words[word][0] / c1

        chiselnyk *= M / (M + N)
        znamenik *=  N / (M + N)

        znamenik += chiselnyk

        answers.append(chiselnyk/znamenik)

    for i in answers:
        print(i)
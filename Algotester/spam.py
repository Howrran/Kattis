N, M, K = map(int, input().split())
spam_imov = M / (N+M)
nespam_imov = N / (N+M)
notspam = list()
spam = list()
email = list()
notspam_words = {}
spam_words = {}
notspam_count = 0
spam_count= 0
for _ in range(N):
    notspam.append(input())
for _ in range(M):
    spam.append(input())
for _ in range(K):
    email.append(input())
for j in notspam:
    for i in j.split():
        if i in notspam_words:
            notspam_words[i] += 1
        else:
            notspam_words[i] = 1
        notspam_count += 1
for j in spam:
    for i in j.split():
        if i in spam_words:
            spam_words[i] += 1
        else:
            spam_words[i] = 1
        spam_count += 1
print(notspam_words)
print(spam_words)

for j in email:
    counter1 = 1
    counter2 = 1
    for i in j.split():
        if i in spam_words:
            a = spam_words[i] / spam_count

        else:
            a = 0

        counter1 *= a
        if i in notspam_words:
            b = notspam_words[i] / notspam_count

        else:
            b = 0
        counter2 *= b
        #x = a/b

    counter1 *= spam_imov
    counter2 *= nespam_imov
    counter2 += counter1
    print( counter1/counter2)
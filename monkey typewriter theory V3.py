import random

characters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
typed_letters = ''
typed_words = []
ITER = 1000000


file = open('shakespear.txt', 'r')
script = file.read()
shakespear_words = script.split('\n')

file.close()

input("press enter to begin: ")

for x in range(ITER + 1):

    typed_letters += characters[random.randint(0, len(characters) - 1)]

    if x % (ITER / 10) == 0:
        print(f"Iteration {x}")

count = 0

for x in shakespear_words:
    if x in typed_letters:
        count += 1
        shakespear_words.remove(x)
        typed_words.append(x)
        if count % 100 == 0:
            print(f"found {count} words!")

print(f"found {len(typed_words)} words in {ITER} random letters")
input('press enter to load all detected words: ')

for x in sorted(typed_words):
    print(x,end=' ')
from CatCounter import CatCounter
from CatParser import CatParser
from Answer import Answer

print('Scanning Wikipedia categories...')
counter = CatCounter('/wiki/Manokana:Sokajy')
while counter.next is not None:
    counter = CatCounter(counter.next)
cats = CatCounter.categories
print(str(len(cats)) + ' categories counted.')
print('Scanning Wikipedia articles. Progress:')
print('-' * 50 + '>')
for i in range(len(cats)):
    CatParser(cats[i])
    if int((i + 1) * 50 / len(cats)) > int(i * 50 / len(cats)):
        print('#', end='', flush=True)
Answer()
input('\nPress enter to continue...')
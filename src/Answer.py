class Answer:
    result = {}

    def __init__(self):
        result = [(x[0], x[1], Answer.result[x]) for x in Answer.result]
        result = sorted(result, key=lambda x: x[2], reverse=True)[:100]
        f = [x[2] for x in result]
        page = open("../results/page.html", 'w', encoding='utf-8')
        page.write(open("../templates/pageBegin.txt", 'r').read())
        for x in result:
            page.write(' ' * 16 + '<tr>\n')
            left = f.index(x[2]) + 1
            right = left + f.count(x[2]) - 1
            num = str(left) if left == right else '{}-{}'.format(left, right)
            page.write(' ' * 20 + '<td>{}</td>\n'.format(num))
            link = 'http://mg.wikipedia.org' + x[1]
            page.write(' ' * 20 + '<td><a href="{}">{}</a></td>\n'.format(link, x[0]))
            page.write(' ' * 20 + '<td>{}</td>\n'.format(x[2]))
            page.write(' ' * 16 + '</tr>\n')
        page.write(open("../templates/pageEnd.txt", 'r').read())
        page.close()
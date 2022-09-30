with open('Opgaven.csv', 'r', encoding="utf-8") as input:
    data = input.read()
    print(data)

result = ''
# output moet string zijn, converteren met str(integer), met int(string) naar int

with open('Result.csv', 'w', encoding="utf-8") as output:
    output.write(result)
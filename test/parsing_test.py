import nyanko.parsing


"""
1. Load the downloaded HTML document
2. Parse it into a list of rows
3. List properties of the first row
"""
if __name__ == "__main__":
    with open("test_results.html") as fp:
        document = fp.read()

    table = nyanko.parsing.Table(document)
    for row in table.rows:
        print(row)

    r = table.rows[0]
    for k, v in r.properties.items():
        print(k, ':', v)

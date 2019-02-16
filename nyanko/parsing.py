import string

from bs4 import BeautifulSoup


"""
Properties used while parsing table rows.
They must be in this exact order.
"""
item_props = (
    "title",
    "size",
    "date",
    "seeders",
    "leechers",
    "downloads",
)


class TableItem:
    """
    A parsed table row.
    Contains item's properties.
    """
    properties = {}

    def __init__(self, tr):
        """
        Construct a single table item for Table
        :param tr: Beautiful Soup object of a single table row (tr)
        """
        row_props = [
            s for s in tr.strings if s not in string.whitespace
        ]

        # remove comment count
        # this may not work sometimes :(
        if row_props[0].isdigit():
            row_props = row_props[1:]

        self.properties = dict(zip(item_props, row_props))

    def __str__(self):
        """
        Object's string representation
        :return: self.properties["title"]
        """
        return self.properties["title"]


class Table:
    """
    Class intended for storing TableItem objects.
    """
    rows = []

    def __init__(self, html_document):
        """
        Parse a nyaa page into a Table structure.
        :param html_document: HTML document text, as it reads from a file
        """
        soup = BeautifulSoup(html_document, "html.parser")
        table_rows = soup.table.tbody.find_all('tr')

        if table_rows is None:
            raise ValueError("Invalid document")

        self.rows = [TableItem(tr) for tr in table_rows]

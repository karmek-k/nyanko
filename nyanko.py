#!/bin/env python
import nyanko


if __name__ == "__main__":
    query = input("Please specify your query: ")
    
    for host in nyanko.hosts:
        page = nyanko.connection.get_page_search(host, query)

    results_table = nyanko.parsing.Table(page)

    print()
    for item in results_table.rows:
        for key, value in item.properties.items():
            print(key, ":\t", value)
        print()

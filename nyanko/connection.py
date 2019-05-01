from urllib import request, error


def get_page(url, **kwargs):
    """
    Get a web page by HTTP GET request
    :param url: nyaa page URL
    :param kwargs: GET arguments
    :return: bytes object with page content
    """
    # make http get arguments
    if kwargs is not None:
        arguments = '?' + '&'.join(
            key + '=' + value for key, value in kwargs.items())
    else:
        arguments = ""

    try:
        with request.urlopen("http://{0}/{1}".format(url, arguments)) as page:
            return page.read()
    except error.HTTPError:
        print("Error: HTTP failure. Can't connect to the server.")
    except error.URLError:
        print("Error: URL failure. The URL may be incorrect.")

    return ""


def get_page_search(url, query, page=1):
    """
    Get a nyaa search page
    :param url: nyaa page URL
    :param query: search query
    :param page: search page number
    :return: bytes object with page content
    """
    query = query.replace(' ', '+')
    page = str(page)

    return get_page(url, q=query, p=page)

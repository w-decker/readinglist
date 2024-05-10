from pyzotero import zotero

def get_items(library_id:str, n_items:int, library_type:str='group', api_key:str=None) -> dict:
    """
    Retrieve dictionary from user's library ID.
    
    Parameters
    ----------
    library_id: str
        Public, Open Membership, group library ID
        
    n_items: int
        How many recent items do you want?

    Return
    ------
    items: dict
    """
    zot = zotero.Zotero(library_id, library_type, api_key)
    items = zot.top(limit=n_items)

    return items

def get_year(items:dict) -> list:
    """Get publication years"""

    # hold
    years = []

    # loop over each citation in dict
    for i in range(len(items)):

        # point to that item's date
        year = items[i]['data']['date']

        # append 
        years.append([year])

    return years

def get_author(items:dict) -> list:
    """Get authors"""

    # hold
    authors = []

    # loop over each citation in dict
    for i in range(len(items)):

        # point to that item's author-specific dict
        point = items[i]['data']['creators']

        # loop over all authors and add first and last name to empty list
        _authors = []
        n_auth = len(point)
        for j, _ in enumerate(range(n_auth)):
            first = point[j]['firstName']
            last = point[j]['lastName']
            _authors.append([f'{first} {last}'])

        # add to global
        authors.append(_authors)

    return authors
    
def get_title(items:dict) -> list:
    """Get titles"""

    # hold
    titles = []

    # loop over each citation in dict
    for i in range(len(items)):

        # point to that item's title
        title = items[i]['data']['title']

        # append 
        titles.append([title])

    return titles

def get_doi(items:dict) -> list:
    """Get digital object identifier (DOI)"""

    # hold
    dois = []

    # loop over each citation in dict
    for i in range(len(items)):

        # point to that item's DOI
        try:
            doi = items[i]['data']['DOI']
        except: # if DOI not present: replace with empty string
            KeyError
            doi = ''

        # append 
        dois.append([doi])

    return dois

def get_journal(items:dict) -> list:
    """Get journals"""

    # hold
    journals = []

    # loop over each citation in dict
    for i in range(len(items)):

        # point to that item's journal
        try:
            journal = items[i]['data']['publicationTitle']
        except: # if journal not present: replace with empty string
            KeyError
            journal = ''

        # append 
        journals.append([journal])

    return journals

def make_readinglist(items:dict):
    """Create reading list"""

    # constant structure
    READINGLIST = {"Title":get_title(items), "Year":get_year(items), 
                   "Authors":get_author(items), "DOI":get_doi(items)}
    
    return READINGLIST

def write_readinglist():
    pass
    
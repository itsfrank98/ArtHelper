from PrologInterface import PrologInterface


def find_artwork_requirements(artwork, kb_path):
    interface = PrologInterface(kb_path)
    query_aw_info = "backward(rule(retrieve_information_artwork, ({}, Title, Year, City_name, Type, StyleNames, ArtistName, MainSubjectsNames, SecondarySubjectsNames, MuseumName, Desc)))".format(artwork)
    query_related_artworks = "backward(rule(retrieve_related_artworks, ({}, Artworks)))".format(artwork)
    info = interface.query(query_aw_info)
    related_artworks = interface.query(query_related_artworks)
    return info, related_artworks


def find_artist_requirements(artist, kb_path):
    interface = PrologInterface(kb_path)
    query_artist_info = "backward(fact(artist, ({}, Name, Yb, Yd)))".format(artist)
    query_related_artists = "backward(fact(influenced_by, ({}, Artists)))".format(artist)
    query_related_styles = "backward(rule(is_exponent, ({}, Style)))".format(artist)
    query_operas = "backward(fact(author, (Opera, {})))".format(artist)
    query_places = "backward(rule(retrieve_artist_places, ({}, Opera)))".format(artist)
    info = interface.query(query_artist_info)
    related_artists = interface.query(query_related_artists)
    related_styles = interface.query(query_related_styles)
    styles = []
    for s in related_styles['query_results']:
        styles.append(s['Style'].replace("_", " ").title())
    operas = interface.query(query_operas)
    places = interface.query(query_places)
    return info, related_artists, styles, operas, places


def find_style_requirements(style, kb_path):
    interface = PrologInterface(kb_path)
    query_style_info = "backward(fact(style, ({}, Name, Yb, Ye, Field)))".format(style)
    query_related_styles = "backward(rule(related_style, ({}, Styles)))".format(style)
    query_related_artists = "backward(rule(is_exponent, (Artist, {})))".format(style)
    info = interface.query(query_style_info)
    related_styles = interface.query(query_related_styles)
    related_artists = interface.query(query_related_artists)
    return info, related_styles, related_artists


def find_church_requirements(church, kb_path):
    interface = PrologInterface(kb_path)
    query_church_info = "backward(rule(retrieve_church_information, ({}, CName, CityName, Yb, Ye, ArchitectsNames, StylesNames)))".format(church)
    query_same_construction_years = "backward(rule(churches_same_construction_years, ({}, Churches, City)))".format(church)
    query_same_style_and_city = "backward(rule(churches_same_style_and_city, ({}, Churches, City, Styles)))".format(church)
    query_artworks = "backward(fact(owns, ({}, Artworks)))".format(church)
    info = interface.query(query_church_info)
    same_construction_years = interface.query(query_same_construction_years)
    same_style_and_city = interface.query(query_same_style_and_city)
    artworks = interface.query(query_artworks)
    return info, same_construction_years, same_style_and_city, artworks


def find_artworks_names(kb_path):
    interface = PrologInterface(kb_path)
    query = "backward(fact(artwork, (ID, Name, _, _, _, _)))"
    results = interface.query(query)
    unique_dict = {}
    for d in results['query_results']:
        for _, _ in d.items():
            unique_dict[d["ID"]] = d["Name"]
    return unique_dict

def find_names(query, kb_path):
    """
    Function that will be used to create the interface. It only retrieves the ID and the name of an item
    :param path: Path of the KB
    :param query: Query to run
    :return:
    """
    interface = PrologInterface(kb_path)
    results = interface.query(query)
    unique_dict = {}
    for d in results['query_results']:
        for _, _ in d.items():
            unique_dict[d["ID"]] = d["Name"]
    return unique_dict

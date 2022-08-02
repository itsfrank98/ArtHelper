:- dynamic rule/2.
:- multifile rule/3.

rule(retrieve_artist_influencers,
    (A, InfluencerName),
    [
        fact(artist, (A, _, _, _)),
        fact(influenced_by(A, L)),
        call(convert_list_elements_to_names(L, InfluencerName))
    ]    
).
rule(retrieve_artist_operas,
    (A, OperaName),
    [
        fact(artist, (A, _, _, _)),
        fact(author, (Artwork, A)),
        fact(artwork, (Artwork, OperaName, _, _, _, _))
    ]
).
rule(retrieve_artist_operas,
    (A, PlaceName),
    [
        fact(artist, (A, _, _, _)),
        call(!),
        fact(designed, (Place, L)),
        call(member(A, L)),
        fact(church, (Place, PlaceName, _, _, _))
    ]
).
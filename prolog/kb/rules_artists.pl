:- dynamic rule/2.
:- multifile rule/3.

rule(retrieve_artist_places,
    (A, Place),
    [
        fact(artist, (A, _, _, _)),
        call(!),
        fact(designed_by, (Place, L)),
        call(member(A, L))
    ]
).
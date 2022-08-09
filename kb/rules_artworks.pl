:- dynamic rule/2.
:- multifile rule/3.
/*
[styles].
[inference].
[art].
[museums].
[rules_artworks].
[utils].
[cities].
[people].
*/

%If the artwork is part of a composition, return the other artworks that are part of that composition
rule(other_elements_composition,
    (A, Other_elements),
    [
        fact(artwork, (A, _, _, _, _, _)),
        fact(composition, (C)),
        call(member(A, C)),
        call(remove_element_from_list(A, C, Other_elements))
    ]
).

/*Given an artwork, find those which portray the same main subjects. For instance, if the argument of this rule is the 'Nascita di Venere' from Botticelli,
whose main subject is the Venere goddess, we would like this rule to match the artworks "Venere e Marte" and "Primavera", which also portray Venere. We 
are interested only in artworks that depict the same subjects and follow the same style*/
rule(artwork_same_subject,
    (A, B),
    [
        fact(artwork, (A, _, _, _, _, _)),
        fact(main_subject, (A, AMain)),
        call(AMain \= []),
        fact(follows, (A, S)),
        call(!),
        fact(artwork, (B, _, _, _, _, _)),
        call(B \= A),
        fact(follows, (B, S)),
        fact(main_subject, (B, BMain)),
        fact(secondary_subject, (B, BSecondary)),
        call(list_concat(BMain, BSecondary, BPortrays)),     %Put all the subjects of the artwork B into a unique list
        call(BPortrays \= []),
        (
            call(subset(AMain, BPortrays));
            call(subset(BPortrays, AMain))
        )
    ]
).

/*Frescos are closely related to the place where they were made. So in order to understand a fresco it could be useful to know the story behind the other 
frescos in the same place made by the same author, if there are any*/
rule(fresco_same_place,
    (A, B),
    [
        fact(artwork, (A, _, _, _, fresco, _)),
        fact(author, (A, Artist)),
        call(!),
        fact(owns, (_, L)),
        call(member(A, L)),
        fact(artwork, (B, _, _, _, fresco, _)),
        call(B \= A),
        fact(author, (B, Artist)),
        call(member(B, L))
    ]
).

rule(retrieve_information_artwork, 
    (A, Title, Year, City_name, Type, StyleNames, Artist, MainSubjectsNames, SecondarySubjectsNames, MuseumName, Desc),
    [
        fact(artwork, (A, Title, Year, C, Type, Desc)),
        fact(city, (C, City_name)),
        fact(follows, (A, Styles)),
        call(convert_list_elements_to_names(Styles, StyleNames)),
        fact(author, (A, Artist)),
        fact(main_subject, (A, MainSubjects)),
        call(convert_list_elements_to_names(MainSubjects, MainSubjectsNames)),
        fact(secondary_subject, (A, SecondarySubjects)),
        call(convert_list_elements_to_names(SecondarySubjects, SecondarySubjectsNames)),
        call(!),
        fact(owns, (Place, L)),
        call(member(A, L)),
        (
            fact(museum, (Place, MuseumName, _));
            fact(church, (Place, MuseumName, _, _, _))
        )
    ]
).

rule(retrieve_related_artworks, 
    (A, Artworks),
    [
        rule(artwork_same_subject, (A, Artworks))
    ]
).
rule(retrieve_related_artworks, 
    (A, Artworks),
    [
        rule(other_elements_composition, (A, Artworks))
    ]
).
rule(retrieve_related_artworks, 
    (A, Artworks),
    [
        rule(fresco_same_place, (A, Artworks))
    ]
).
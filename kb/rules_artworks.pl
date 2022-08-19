:- dynamic rule/2.
:- multifile rule/3.
/*
[styles].
[inference].
[art].
[museums].
[rules_artworks].
[utils].
[people].
*/

/*If the artwork is part of a polyptych, return the other artworks that are part of that polyptych*/
rule(other_elements_polyptych,
    (A, Artwork),
    [
        fact(artwork, (A, _, _, _, _, _)),
        fact(artwork, (Artwork, _, _, _, _, _)),
        call(A \= Artwork),
        fact(polyptych, (C)),
        call(member(A, C)),
        call(member(Artwork, C))
    ]
).

/*Given an artwork, find those which portray the same main subjects. For instance, if the argument of this rule is the 'Nascita di Venere' from Botticelli,
whose main subject is the Venere goddess, we would like this rule to match the artworks "Venere e Marte" and "Primavera", which also portray Venere. We 
are interested only in artworks that depict the same subjects and follow the same style*/
rule(artwork_same_subject,
    (A, B, Characters, S),
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
        call(list_intersect(AMain, BPortrays, Intersection)),
        call(Intersection \= []),
        call(convert_list_elements_to_names(Intersection, Characters))
    ]
).

/*Frescos are closely related to the place where they were made. So in order to understand a fresco it could be useful to know the story behind the other 
frescos in the same place made by the same author, if there are any*/
rule(fresco_same_place,
    (A, B, Place, Artist),
    [
        fact(artwork, (A, _, _, _, fresco, _)),
        fact(author, (A, Artist)),
        call(!),
        fact(owns, (Place, L)),
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
        fact(artwork, (A, Title, Year, City_name, Type, Desc)),
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
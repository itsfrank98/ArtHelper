:- dynamic rule/2.
:- multifile rule/3.
%Rule to determine whether an artist is exponent of a style

rule(is_exponent,
    (Artist, S),
    [
        fact(artist, (Artist, _, _, _)),
        fact(author, (Work, Artist)),
        fact(follows, (Work, LS)),
        call(!),
        fact(style, (S, _, _, _, _)),
        call(member(S, LS))
    ]
).
rule(is_exponent,
    (Architect, S),
    [
        fact(artist, (Architect, _, Yb, Yd)),
        call(!),
        fact(designed, (Place, Architects)),
        call(member(Architect, Architects)),
        fact(style, (S, _, Ys, Ye, _)),
        /*Many architects can design a monument through the years. So we make these checks to avoid having an architect following styles that were 
        followed by people who worked at the realization of a church before or after him*/
        call(Yd >= Ys),   %An architect cannot follow a style that started after his death
        call(Ye >= Yb),   %An architect cannot follow a style that ended before his birth
        fact(follows, (Place, LS)),
        call(member(S, LS))
    ]
).

/*THE FOLLOWING RULES ARE USED TO FIND STYLES NEEDED TO UNDERSTAND A STYLE*/

/*Two styles can be related only if they cover the same field. A style that is exclusively architectural cannot be related to a style involving only 
visual arts. The fields for a style can be architectural, art, both*/
rule(potentially_related_fields, (X, X),
    [
        call(!),
        true
    ]
).
rule(potentially_related_fields, (X, Y),
    [
        call(!),
        (call(X = both); call(Y = both))
    ]
).
rule(potentially_related_fields, (X, Y),
    [
        call(X \= Y),
        false
    ]
).


%Determine whether two styles co-existed. 
rule(co_existing_styles, (S1, S2),
    [
        fact(style, (S1, _, Yb1, Ye1, F1)),
        call(!),
        fact(style, (S2, _, Yb2, Ye2, F2)),
        call(S1 \= S2),
        %We are interested only in co-existing styles that covered the same field
        rule(potentially_related_fields, (F1, F2)),
        %If The second style was born after the first, in order for them to have coexisted the first must end after the starting of the second
        (
            (
                call((Yb1 < Yb2, Ye1 > Yb2))
            );
            (
                call((Yb1 > Yb2, Ye2 > Yb1))
            )
        )
    ]
).

/*We have two rules to determine if a style A influenced a style B.
The first is: if they belong to the same main current (ie proto renaissance, early renaissance and high renaissance), 
then the youngest was influenced by the oldest.*/
rule(influenced_same_current, (S1, S2),
    [
        fact(style, (S1, _, Yb1, _, _)),
        call(!),
        fact(style, (S2, _, Yb2, _, _)),
        call(S1 \= S2),
        % If two styles belong to the same main current, style B can be influenced by style A only if the latter was born before the former
        call(Yb1 > Yb2),
        fact(same_main_current, (C)),
        call(member(S1, C)),
        call(member(S2, C))
    ]
).
/*
The second rule is: if there is a monument or an artwork that follows more than one style, then the oldest influenced the youngest.
*/
rule(influenced_same_art, (S1, S2, A),
    [
        fact(style, (S1, _, Yb1, _, _)),
        call(!),
        fact(style, (S2, _, Yb2, _, _)),
        call(Yb1 > Yb2),
        fact(follows, (A, S)),
        call(member(S1, S)),
        call(member(S2, S))
    ]
).

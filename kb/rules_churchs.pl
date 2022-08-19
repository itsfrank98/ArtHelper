:- dynamic rule/2.
:- multifile rule/3.

rule(churches_same_style_and_city,
    (C1, C2, City, StyleNames),
    [
        fact(church, (C1, _, City, _, _)),
        fact(follows, (C1, S1)),
        call(!),
        fact(church, (C2, _, City, _, _)),
        call(C1 \= C2),
        fact(follows, (C2, S2)),
        call(list_intersect(S1, S2, Intersection)),
        call(Intersection \= []),
        call(convert_list_elements_to_names(Intersection, StyleNames))
    ]
).

/*Given a church, this rule will find the churches that were built during the same years in the same city*/
rule(churches_same_construction_years,
    (C1, C2, City),
    [
        fact(church, (C1, _, City, Yb1, Ye1)),
        call(!),
        fact(church, (C2, _, City, Yb2, Ye2)),
        call(C1 \= C2),
        (
            call((Yb1 < Yb2, Ye1 > Yb2));
            call((Yb2 < Yb1, Ye2 > Yb1))
        )
    ]
).

rule(retrieve_church_information, 
    (C, CName, CityName, Yb, Ye, Architects, StylesNames),
    [
        fact(church, (C, CName, CityName, Yb, Ye)),
        fact(designed_by, (C, Architects)),
        fact(follows, (C, Styles)),
        call(convert_list_elements_to_names(Styles, StylesNames))
    ]
).
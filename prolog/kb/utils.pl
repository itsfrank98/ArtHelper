list_concat([],L,L).
list_concat([X1|L1],L2,[X1|L3]) :- list_concat(L1,L2,L3).


list_intersect([X|Y],Z,[X|W]) :-
   member(X,Z), list_intersect(Y,Z,W).
list_intersect([X|Y],Z,W) :-
   \+ member(X,Z), list_intersect(Y,Z,W).
list_intersect([],_,[]).


convert_list_elements_to_names([], []).
convert_list_elements_to_names([S|Tail], [N|Y]) :-
    fact(style, (S, N, _, _, _)),
    !,
    convert_list_elements_to_names(Tail, Y).
convert_list_elements_to_names([A|Tail], [N|Y]) :-
    fact(artist, (A, N, _, _)),
    !,
    convert_list_elements_to_names(Tail, Y).
convert_list_elements_to_names([P|Tail], [N|Y]) :-
    fact(portrayable, (P, N)),
    !,
    convert_list_elements_to_names(Tail, Y).
convert_list_elements_to_names([AW|Tail], [N|Y]) :-
    fact(artwork, (AW, N, _, _, _, _)),
    !,
    convert_list_elements_to_names(Tail, Y).
convert_list_elements_to_names([M|Tail], [N|Y]) :-
    fact(museum, (M, N, _)),
    !,
    convert_list_elements_to_names(Tail, Y).
convert_list_elements_to_names([C|Tail], [N|Y]) :-
    fact(church, (C, N, _, _, _)),
    !,
    convert_list_elements_to_names(Tail, Y).

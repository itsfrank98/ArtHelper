%fact/1
:- dynamic fact/1.
fact(person, (elizabeth, 1926)).
fact(person, (charles, 1948)).
fact(person, (william, 1982)).
fact(person, (kate, 1982)).
fact(person, (diana, 1961)).
fact(person, (philip, 1921)).

fact(mother, (charles, elizabeth)).
fact(mother, (william, diana)).
fact(father, (charles, philip)).
fact(father, (william, charles)).

%rule/2
:- dynamic rule/3.
:- multifile rule/3.
rule(married, (W, H), [fact(mother, (S, W)), fact(father, (S, H))]).

rule(parent, (S, P), [(fact(mother, (S, P)))]).
rule(parent, (S, P), [(fact(father, (S, P)))]).

rule(grandparent, (Nephew, Granny), [rule(parent, (Nephew, P)), rule(parent, (P, Granny))]).

rule(older, (A, B), [fact(person, (A, X)), fact(person, (B, Y)), call(X > Y)]).

backward(fact(Z, P)) :-
    !,
    fact(Z, P).
backward(rule(RName, Params)) :-
    !,
    rule(RName, Params, Body),
    bw(rule(RName, Params, Body), [], L),
    asserta(used(L)).
bw(rule(RName, Params, RBody), L, L2) :-
    !,
    prove(RBody, L, L1),
    append([(RName, Params)], L1, L2).
bw(rule(RName, Params), L1, L2) :-
    !,
    rule(RName, Params, RBody),
    bw(rule(RName, Params, RBody), L1, L2).
bw(fact(Z, P), L, L1) :-
    !,
    backward(fact(Z, P)),
    append([(Z, P)], L, L1).
bw((FR1; FR2), L, L1) :-
    !,
    (bw(FR1, L, L1);
    bw(FR2, L, L1)).
bw(call(F), L, L) :-
    !,
    call(F).


prove([], L, L) :- !, true.
prove([true], L, L) :- !, true.
prove([false], L, L) :- !, false.
prove([H|T], L, L3) :-
    !,
    bw(H, L, L2), 
    prove(T, L2, L3).

    

forward :- done.
forward :- 
    fact(F), 
    not(pursuit(F)),
    assertz(usedfact(F)),
    retract(fact(F)),
    forward.

done :- not(fact(_)).

pursuit(F) :-
    rule(L, R),
    rule_pursuit(F, L, R),
    fail.
rule_pursuit(F, L, R) :-
    member(F, R),
    delete(F, R, NewR),
    new_rule(L, NewR).

new_rule(L, []) :-
    not(fact(L)),
    asserta(fact(L)).
new_rule(L, R) :-
    R \= [],
    asserta(rule(L, R)).

/*
:- dynamic member/2.
member(X,[X|L]).
member(X,[Y|L]) :- member(X,L).

:- dynamic delete/3.
delete(X,[],[]).
delete(X,[X|L],M) :- delete(X,L,M).
delete(X,[Y|L],[Y|M]) :- not(X=Y), delete(X,L,M).
*/



    



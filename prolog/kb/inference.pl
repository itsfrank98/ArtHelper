/********************* THE FOLLOWING IS A DUMMY KB FOR TESTING THE BACKWARD INFERENCE MECHANISM **************************/
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

/******************************************************************************************************************************/

backward(fact(FName, Arguments)) :-
    !,
    fact(FName, Arguments).
backward(rule(RName, Arguments)) :-
    !,
    rule(RName, Arguments, Body),
    bw(rule(RName, Arguments, Body), [], L),
    asserta(used(L)).
bw(rule(RName, Arguments, RBody), L, L2) :-
    !,
    prove(RBody, L, L1),
    append([(RName, Arguments)], L1, L2).
bw(rule(RName, Arguments), L1, L2) :-
    !,
    rule(RName, Arguments, RBody),
    bw(rule(RName, Arguments, RBody), L1, L2).
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

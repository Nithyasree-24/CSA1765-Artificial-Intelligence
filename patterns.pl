match([], []).

match([_ | PatternTail], [_ | ListTail]) :-
    match(PatternTail, ListTail).

match([Head | PatternTail], [Head | ListTail]) :-
    match(PatternTail, ListTail).

vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel(A) :- char_type(A, upper), char_type(A, to_lower(L)), vowel(L).
count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, RestCount),
    Count is RestCount + 1.

count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).

vowels_in_string(String, Count) :-
    string_chars(String, CharList),
    count_vowels(CharList, Count).

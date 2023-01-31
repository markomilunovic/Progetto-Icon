:- dynamic(casa/3).
:- dynamic(citta/3).
:- dynamic(zona/3).

%---REGOLE---

% casa(id, vendita, zona).
% citta(nomeCitta, paese, regione).
% zona(codiceZona, nomeCitta, disponibilita).

%---DATI---

%---LISTA CASE---
casa(10045, si, 'smm').
casa(10046, si, 'isk').
casa(10047, no, null).
casa(10048, si, 'gjk').
casa(10049, no, null).
casa(10050, no, null).
casa(10051, si, 'sdd').
casa(10052, si, 'smm').

%---LISTA CITTA---
citta('milano', 'italia', 'lombardia').
citta('roma', 'italia',  'lazio').
citta('new york city', 'usa', 'new york state').
citta('toronto', 'canada', 'ontario').
citta('caen', 'francia', 'normandia').
citta('munich', 'germania', 'baviera').

%---LISTA ZONA---
zona('smm', 'milano', 2).
zona('isk', 'milano', 1).
zona('gjk', 'new york', 1).
zona('sdd', 'toronto', 1).
zona('qwe', 'berlino', 0).
zona('azx', 'londra', 0).

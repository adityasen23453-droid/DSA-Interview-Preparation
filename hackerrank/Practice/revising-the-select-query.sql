// Problem: Revising the Select Query I
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
// Solved on: 2026-11-12T16:30:45.039Z


SELECT *
FROM CITY
WHERE CountryCode = 'USA'
AND Population > 100000;

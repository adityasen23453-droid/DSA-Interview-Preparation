// Problem: Japan Population
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/population-density-difference?isFullScreen=true
// Solved on: 2026-11-16T10:11:53.796Z

SELECT SUM(Population)
FROM CITY
WHERE COUNTRYCODE = 'JPN';

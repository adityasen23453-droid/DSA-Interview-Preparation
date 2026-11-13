// Problem: Weather Observation Station 6
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true
// Solved on: 2026-11-13T08:45:56.721Z

SELECT DISTINCT CITY
FROM STATION
WHERE CITY LIKE 'A%'
OR CITY LIKE 'E%'
OR CITY LIKE 'I%'
OR CITY LIKE 'O%'
OR CITY LIKE 'U%' ;

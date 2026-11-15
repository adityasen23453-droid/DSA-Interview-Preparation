// Problem: Weather Observation Station 8
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
// Solved on: 2026-11-15T16:35:21.404Z

SELECT DISTINCT CITY
FROM STATION
WHERE (CITY LIKE 'A%'
OR CITY LIKE 'E%'
OR CITY LIKE 'I%'
OR CITY LIKE 'O%'
OR CITY LIKE 'U%')
AND (CITY LIKE '%A'
OR CITY LIKE '%E'
OR CITY LIKE '%I'
OR CITY LIKE '%O'
OR CITY LIKE '%U') ;

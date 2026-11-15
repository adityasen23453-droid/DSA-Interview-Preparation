// Problem: Weather Observation Station 9
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/weather-observation-station-10?isFullScreen=true
// Solved on: 2026-11-15T16:38:34.458Z

SELECT DISTINCT CITY
FROM STATION
WHERE (CITY NOT LIKE 'A%'
AND CITY NOT LIKE 'E%'
AND CITY NOT LIKE 'I%'
AND CITY NOT LIKE 'O%'
AND CITY NOT LIKE 'U%');

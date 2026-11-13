// Problem: Weather Observation Station 5
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
// Solved on: 2026-11-13T08:34:49.053Z

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) ASC, CITY ASC
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY ASC
LIMIT 1;

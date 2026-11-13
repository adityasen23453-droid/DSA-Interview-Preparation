// Problem: Weather Observation Station 4
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
// Solved on: 2026-11-13T07:05:04.522Z

SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;

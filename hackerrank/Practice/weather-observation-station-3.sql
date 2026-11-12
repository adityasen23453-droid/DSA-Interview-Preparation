// Problem: Weather Observation Station 3
// Platform: hackerrank
// Language: mysql
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true
// Solved on: 2026-11-12T17:13:35.332Z

SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0;

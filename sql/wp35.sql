SELECT COUNT(victim_name) as kill_count
FROM match_frag
WHERE victim_name IS NOT NULL
SELECT count(killer_name) as suicide_count
FROM match_frag
WHERE victim_name IS NULL
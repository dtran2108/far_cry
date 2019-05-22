SELECT match_id,
       COUNT(victim_name) as sucide_count
FROM match_frag
WHERE victim_name IS NULL
ORDER BY sucide_count
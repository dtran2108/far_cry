SELECT match.match_id, start_time, end_time, count(distinct match_frag.killer_name) as player_count, count(match_frag.killer_name) as kill_sucide_count
from match
inner join match_frag on match.match_id = match_frag.match_id
chat_count_by_user_sql = """
SELECT
    user_id,
    COUNT(*) as cnt
FROM
	kakaotalk_chat
WHERE
    user_id not in ("", "Q0x8G-a_9cz3", "GHQ8EU5wYekr")
GROUP BY
	1
""".strip()

chat_per_date_sql = """
SELECT
	DATE(CONVERT_TZ(created_at, '+00:00', 'Asia/Seoul')) as date,
    COUNT(*) as cnt
FROM
	kakaotalk_chat
WHERE
    user_id not in ("", "Q0x8G-a_9cz3", "GHQ7hwxwYekr")
GROUP BY
	1
ORDER BY
	1;
""".strip()

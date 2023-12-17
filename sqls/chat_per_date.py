chat_per_date_sql = """
SELECT
	DATE(created_at) as date,
    COUNT(*) as cnt
FROM
	kakaotalk_chat
GROUP BY
	1
ORDER BY
	1;
""".strip()

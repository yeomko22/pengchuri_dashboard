chat_sql = """
SELECT
    id,
    created_at,
    user_id,
    question,
    answer
FROM
    kakaotalk_chat 
ORDER BY
    created_at DESC
LIMIT
    {pagesize}
OFFSET
    {offset}
""".strip()

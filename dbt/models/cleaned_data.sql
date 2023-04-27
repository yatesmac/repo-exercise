-- cleaned_data.sql

{{
    config(materialized='table')
}}

WITH raw_data AS (
    SELECT * FROM {{ ref('gpappdata') }}
),
cleaned_data AS (
    SELECT DISTINCT
        "App" AS app,
        "Category" AS category,
        CAST("Rating" AS FLOAT) AS rating,
        CAST("Reviews" AS iNT) AS reviews,
        CAST("Size" AS FLOAT) AS size,
        CAST("Installs" AS INT) AS installs,
        "Type" AS type,
        CAST("Price" AS FLOAT) AS price,
        "Content Rating" AS content_rating,
        "Genres" AS genres,
        "Last Updated" AS last_updated,
        "Current Ver" AS current_ver,
        "Android Ver" AS android_ver
        CASE
            WHEN price = '0' THEN 'Free'
            ELSE 'Paid'
        END AS price_category
    FROM raw_data
    WHERE
        app IS NOT NULL AND
        category IS NOT NULL AND
        Rrating IS NOT NULL AND
        reviews IS NOT NULL AND
        size IS NOT NULL AND
        installs IS NOT NULL AND
        type IS NOT NULL AND
        price IS NOT NULL AND
        content_rating IS NOT NULL AND
        genres IS NOT NULL AND
        last_updated IS NOT NULL AND
        current_ver IS NOT NULL AND
        android_ver IS NOT NULL
        price_category IS NOT NULL
)

SELECT *
FROM cleaned_data
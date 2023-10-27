{{ config(materialized='table') }}

with reviews_source as (
    select * from {{ source('Fonte_AIRBNB', 'Reviews_Silver') }}
),

aggregate as (
    select
        listing_id,
        date_trunc('month', date) as month,
        count(id) as number_of_reviews
    from reviews_source
    group by listing_id, date_trunc('month', date)
)

select * from aggregate
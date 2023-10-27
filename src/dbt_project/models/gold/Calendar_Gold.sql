{{ config(materialized='table') }}

with calendar_source as (
    select * from {{ source('Fonte_AIRBNB', 'Calendar_Silver') }}
),

aggregate as (
    select
        listing_id,
        date,
        avg(price) as avg_price, 
        avg(adjusted_price) as avg_adjusted_price
    from calendar_source
    group by listing_id, date
)

select * from aggregate
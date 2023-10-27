{{ config(materialized='table') }}

with listing_source as (
    select * from {{ source('Fonte_AIRBNB', 'Listing_Silver') }} 
),

aggregate as (
    select
        id,
        avg(CASE WHEN review_scores_rating = 'no_info' 
              OR  review_scores_rating = NULL
            THEN NULL ELSE review_scores_rating::numeric END) as avg_review_scores_rating,
        min(CASE WHEN review_scores_rating = 'no_info' 
              OR  review_scores_rating = NULL
            THEN NULL ELSE review_scores_rating::numeric END) as min_review_scores_rating,
        max(CASE WHEN review_scores_rating = 'no_info' 
              OR  review_scores_rating = NULL
            THEN NULL ELSE review_scores_rating::numeric END) as max_review_scores_rating,
        avg(CASE WHEN review_scores_accuracy = 'no_info' 
              OR  review_scores_accuracy = NULL
            THEN NULL ELSE review_scores_accuracy::numeric END) as avg_review_scores_accuracy
    from listing_source
    group by id
)

select * from aggregate
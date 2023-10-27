{% test test_check_unique_values(model, column_name) %}
  SELECT {{ column_name }}, count(*) 
  FROM {{ model }} 
  GROUP BY {{ column_name }}
  HAVING count(*) > 1
{% endtest %}
SELECT w.id AS warehouse_id,
       w.city AS warehouse_city,
       COUNT(r.id) AS route_count,
       AVG(r.delivery_days) AS avg_delivery_days
FROM warehouses w
LEFT JOIN routes r ON w.id = r.warehouse_id
WHERE r.is_active = 1
GROUP BY w.id;
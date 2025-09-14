-- CREATE TABLE shipments (matching your SQLAlchemy model)
CREATE TABLE shipments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    warehouse_id INT,
    route_id INT,
    driver_id INT,
    vehicle_id INT,
    status VARCHAR(50) DEFAULT 'pending',
    total_amount FLOAT,
    created_at DATETIME,
    updated_at DATETIME,
    estimated_delivery DATETIME,
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT fk_warehouse FOREIGN KEY (warehouse_id) REFERENCES warehouses(id),
    CONSTRAINT fk_route FOREIGN KEY (route_id) REFERENCES routes(id),
    CONSTRAINT fk_driver FOREIGN KEY (driver_id) REFERENCES drivers(id),
    CONSTRAINT fk_vehicle FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);

-- Insert test data into categories table
INSERT INTO categories (name, parent_id) VALUES
  ('Electronics', NULL),
  ('Computers', 1),
  ('Laptops', 2),
  ('Desktops', 2),
  ('Smartphones', 1),
  ('Accessories', 1),
  ('Chargers', 6),
  ('Cables', 6);

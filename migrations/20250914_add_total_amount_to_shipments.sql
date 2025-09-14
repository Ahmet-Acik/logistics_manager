-- Migration: Add total_amount column to shipments table
ALTER TABLE shipments ADD COLUMN total_amount FLOAT;

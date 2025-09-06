# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    shipments = relationship('Shipment', back_populates='customer')

class Warehouse(Base):
    __tablename__ = 'warehouses'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)
    shipments = relationship('Shipment', back_populates='warehouse')

class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    origin = Column(String(200), nullable=False)
    destination = Column(String(200), nullable=False)
    distance_km = Column(Float)
    shipments = relationship('Shipment', back_populates='route')

class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    license_number = Column(String(50), unique=True)
    shipments = relationship('Shipment', back_populates='driver')

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    plate_number = Column(String(20), unique=True, nullable=False)
    type = Column(String(50))
    capacity = Column(Integer)
    shipments = relationship('Shipment', back_populates='vehicle')

class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    warehouse_id = Column(Integer, ForeignKey('warehouses.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    status = Column(String(50), default='pending')
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    estimated_delivery = Column(DateTime)
    customer = relationship('Customer', back_populates='shipments')
    warehouse = relationship('Warehouse', back_populates='shipments')
    route = relationship('Route', back_populates='shipments')
    trackings = relationship('Tracking', back_populates='shipment')
    driver = relationship('Driver', back_populates='shipments')
    vehicle = relationship('Vehicle', back_populates='shipments')

class Tracking(Base):
    __tablename__ = 'trackings'
    id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipments.id'))
    status = Column(String(50))
    location = Column(String(200))
    timestamp = Column(DateTime)
    shipment = relationship('Shipment', back_populates='trackings')


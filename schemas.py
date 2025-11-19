"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Luxury Real Estate Lead schema
class Lead(BaseModel):
    """
    Leads generated from the website/chatbot
    Collection name: "lead"
    """
    name: str = Field(..., description="Customer full name")
    email: str = Field(..., description="Customer email")
    phone: Optional[str] = Field(None, description="Customer phone number")
    message: Optional[str] = Field(None, description="Customer message or requirements")
    preferred_datetime: Optional[datetime] = Field(None, description="Requested meeting datetime (ISO)")
    property_type: Optional[str] = Field(None, description="Buy/Sell/Rent and type (penthouse, villa, etc.)")
    budget_min: Optional[float] = Field(None, description="Minimum budget")
    budget_max: Optional[float] = Field(None, description="Maximum budget")
    source: str = Field("website", description="Where the lead originated (website/chatbot/form)")
    status: str = Field("new", description="Lead status")

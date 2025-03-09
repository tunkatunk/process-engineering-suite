"""
Base data models shared across modules.
"""
from datetime import datetime
from typing import Optional, List

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from core.data.database import Base

class User(Base):
    """Base user model for authentication."""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    role = Column(String)  # e.g., "engineer", "admin"
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    projects = relationship("Project", back_populates="owner")
    
    def __repr__(self) -> str:
        return f"<User {self.name}>"

class Project(Base):
    """Project container for organizing work."""
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    owner = relationship("User", back_populates="projects")
    
    def __repr__(self) -> str:
        return f"<Project {self.name}>"

# Association table for tagging
tags_association = Table(
    'tags_association',
    Base.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)

class Tag(Base):
    """Tags for organizing and filtering projects."""
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
    # Relationships
    projects = relationship("Project", secondary=tags_association)
    
    def __repr__(self) -> str:
        return f"<Tag {self.name}>"

class Audit(Base):
    """Audit trail for tracking changes."""
    __tablename__ = "audit_log"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    action = Column(String, nullable=False)  # e.g., "create", "update", "delete"
    entity_type = Column(String, nullable=False)  # e.g., "Project", "User"
    entity_id = Column(Integer)
    changes = Column(String)  # JSON string of changes
    
    # Relationships
    user = relationship("User")
    
    def __repr__(self) -> str:
        return f"<Audit {self.action} {self.entity_type} {self.entity_id}>"
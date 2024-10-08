from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from enum import Enum as PyEnum

Base = declarative_base()


# Choices equivalent in SQLAlchemy using Enum
class StatusEnum(PyEnum):
    pending = "pending"
    verified = "verified"


class Block(Base):
    __tablename__ = 'block'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(String(200), nullable=False)
    prev_block_hash = Column(String(200), nullable=False)


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, nullable=False)
    trxn_uuid = Column(String(200), nullable=False)
    sender_pub_key = Column(String(200), nullable=False)
    receiver_pub_key = Column(String(200), nullable=False)
    amount = Column(Integer, nullable=False)
    trxn_hash = Column(String(200), nullable=False)
    trxn_signature = Column(String(200), nullable=False)
    parent_block_id = Column(Integer, ForeignKey('block.id'), nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.pending)

    parent_block = relationship("Block", back_populates="transactions")


Block.transactions = relationship("Transaction", order_by=Transaction.id, back_populates="parent_block")


class Wallet(Base):
    __tablename__ = 'wallet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    private_key = Column(String(200), nullable=False)
    public_key = Column(String(200), nullable=False)
    balance = Column(Integer, nullable=False)



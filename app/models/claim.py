import enum
from sqlalchemy.dialects import postgresql
from app.extensions import db
from app.models.receipt import Receipt


class ClaimStatus(enum.Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    DENIED = "Denied"


class Claim(db.Model):
    __tablename__ = 'claim'
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String(255))
    status = db.Column(postgresql.ENUM(ClaimStatus))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receipts = db.relationship("Receipt", backref="claim", lazy=True)

    def __repr__(self):
        return f"Claim ID: {self.id}"

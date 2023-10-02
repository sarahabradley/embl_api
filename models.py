from config import db, ma
from sqlalchemy import ForeignKey
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields

class Gene(db.Model):
    __tablename__ = "gene"
    gene_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50))
    stable_id = db.Column(db.String(50))
    transcripts = db.relationship('Transcript', backref='gene', lazy='dynamic')

class Transcript(db.Model):
    __tablename__ = "transcript"
    transcript_id = db.Column(db.Integer, primary_key=True)
    stable_id = db.Column(db.String(50))
    gene_id = db.Column(db.Integer, ForeignKey('gene.gene_id'))

class TranscriptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Transcript
        load_instance = True
        sqla_session = db.session

class GeneSchema(SQLAlchemyAutoSchema):
    transcripts = fields.Nested(TranscriptSchema, many=True)
    class Meta:
        model = Gene
        load_instance = True
        sqla_session = db.session

genes_schema = GeneSchema(many=True)
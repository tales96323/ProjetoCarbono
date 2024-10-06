from sqlalchemy import create_engine, Column, Float, String, DateTime, Integer  # Adicione Integer aqui
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco de dados
DATABASE_URL = "sqlite:///emissions.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definição do modelo
class EmissionRecord(Base):
    __tablename__ = 'emission_records'
    
    id = Column(Integer, primary_key=True)
    company = Column(String)
    energy_emissions = Column(Float)
    transport_emissions = Column(Float)
    waste_emissions = Column(Float)
    total_emissions = Column(Float)
    date_recorded = Column(DateTime)

# Criação das tabelas no banco de dados (caso não existam)
Base.metadata.create_all(engine)

# Função para salvar um registro de emissões
def save_emission_record(emission_report, date_recorded):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_record = EmissionRecord(
        company=emission_report['company'],
        energy_emissions=emission_report['energy_emissions'],
        transport_emissions=emission_report['transport_emissions'],
        waste_emissions=emission_report['waste_emissions'],
        total_emissions=emission_report['total_emissions'],
        date_recorded=date_recorded
    )

    session.add(new_record)
    session.commit()
    session.close()

# Função para obter todos os registros
def get_all_records():
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(EmissionRecord).all()
    session.close()
    return records

# Função para obter registros por data
def get_records_by_date():
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(EmissionRecord).all()
    session.close()
    return records
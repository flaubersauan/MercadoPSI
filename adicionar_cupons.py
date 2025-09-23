from app import app, db
from datetime import datetime

with app.app_context():
    cupom1 = Cupom(codigo='SAVE10', desconto=10.0, data_expiracao=datetime(2025, 12, 31))
    cupom2 = Cupom(codigo='DESCONTO25', desconto=25.0, data_expiracao=datetime(2025, 11, 30))
    cupom3 = Cupom(codigo='FRETEGRATIS', desconto=10.0, data_expiracao=datetime(2025, 10, 15))

    db.session.add(cupom1)
    db.session.add(cupom2)
    db.session.add(cupom3)
    
    db.session.commit()
    print("Cupons adicionados com sucesso!")

from models import db, Person


class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, db.ForeignKey(Person.id), primary_key = True)
    created_at = db.Column(db.Date)

    def save_client(name,cpf,email,senha,birth_date,created_at):
        person = Person(name = name,
                        cpf = cpf,
                        email = email,
                        senha = senha,
                        birth_date = birth_date)

        client = Client(id = person.id,
                        created_at = created_at)

        person.clients.append(client)

        db.session.add(person)
        db.session.commit()

    def get_clients():
        clients = Client.query.join(Person, Person.id == Client.id)\
                        .add_columns(Person.id,Person.name,Person.cpf, Person.email, 
                                     Person.senha , Person.birth_date, Client.created_at).all()
        
        return clients
    
    def delete_client(id):
        client = Client.query.filter(Client.id == id).first()
        db.session.delete(client)
        db.session.commit()

    def update_client(id, name,cpf,email,senha,birth_date,created_at):
        Person.query.filter_by(id=id)\
                .update(dict(name=name,cpf=cpf,email=email,senha=senha,
                             birth_date=birth_date))
        Client.query.filter_by(id=id)\
                        .update(dict(created_at=created_at))

        db.session.commit()
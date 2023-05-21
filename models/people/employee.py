from models import db, Person

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, db.ForeignKey(Person.id), primary_key = True)

    def save_employee(name,cpf,email,senha,birth_date):
        person = Person(name = name,
                        cpf = cpf,
                        email = email,
                        senha = senha,
                        birth_date = birth_date)

        employee = Employee(id = person.id)

        person.employees.append(employee)

        db.session.add(person)
        db.session.commit()

    def get_employees():
        employees = Employee.query.join(Person, Person.id == Employee.id)\
                        .add_columns(Person.id,Person.name,Person.cpf, Person.email, 
                                     Person.senha, Person.birth_date).all()
        
        return employees
    
    def delete_employee(id):
        employee = Employee.query.filter(Employee.id == id).first()
        db.session.delete(employee)
        db.session.commit()

    def update_employee(id, name,cpf,email,senha,birth_date):
        Person.query.filter_by(id=id)\
                .update(dict(name=name,cpf=cpf,email=email,senha=senha,
                             birth_date=birth_date))

        db.session.commit()



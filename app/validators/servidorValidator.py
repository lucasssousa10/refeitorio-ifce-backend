from app import FormValidator, Messages
from app import User


class ServidorValidator(FormValidator):
    def __init__(self, formData):
        super().__init__(formData)
        self.addFields()
        self.addConstraints()

    # --------------------------------------------------------------------------------------------------#

    def addFields(self):
        super().addField("cpf", "CPF", "cpf", required=True)
        super().addField("siape", "Siape", "text", required=False)
        super().addField("nome", "Nome", "text", required=True)
        super().addField("users_id", "Usuário", "number", required=True)

    # --------------------------------------------------------------------------------------------------#

    def addConstraints(self):
        super().addLengthConstraint("nome", 2, 255)

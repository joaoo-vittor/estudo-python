from blocklist import BLOCKLIST
from flask_restful import Resource, reqparse
from models.usuario import UserModel

from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp


atributos = reqparse.RequestParser()
atributos.add_argument(
    'login', type=str, required=True, help="O campo 'login' não pode ficar vazio")
atributos.add_argument(
    'senha', type=str, required=True, help="O campo 'senha' não pode ficar vazio")


class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()

        # status: not found
        return {'msg': f'User {user_id} não encontrado!'}, 404

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)

        if user:
            try:
                user.delete_user()
            except:
                return {'msg': 'Erro inesperado.'}, 500

            return {'msg': f'Hotel {user_id} deleted.'}

        return {'msg': f'Hotel {user_id} not found.'}, 404


class UserRegister(Resource):
    # cadastro
    def post(self):
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados['login']):
            return {'msg': f'O usuario \'{dados["login"]}\' já existe.'}

        user = UserModel(**dados)
        user.save_user()
        return {'msg': 'Usuario criado com sucesso!'}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200

        return {'msg': 'Usuario ou senha esta incorreto.'}, 401


class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']  # JWT Token Identifier
        BLOCKLIST.add(jwt_id)
        return {'msg': 'Desconectado com sucesso!'}, 200

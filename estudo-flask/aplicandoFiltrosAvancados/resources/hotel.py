from flask_restful import Resource, reqparse
import jwt
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3


def normalize_path_params(cidade=None, estrelas_min=0, estrelas_max=5,
                          diaria_min=0, diaria_max=10000, limit=50,
                          offset=0, **dados):
    if cidade:
        return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade': cidade,
            'limit': limit,
            'offset': offset
        }

    return {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit': limit,
        'offset': offset
    }


# path /hoteis?cidade=Rio de Janeiro&estrelas_min=4&diaria_max=400
path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)


class Hoteis(Resource):

    # method GET
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        dados = path_params.parse_args()
        dados_validos = {key: dados[key]
                         for key in dados.keys() if dados[key] is not None}
        paramentros = normalize_path_params(**dados_validos)

        if not paramentros.get('cidade'):
            consulta = 'SELECT * FROM hoteis \
                        WHERE (estrelas > ? and estrelas < ?) \
                        and (diaria > ? and diaria < ?) \
                        LIMIT ? OFFSET ?'
            tp = tuple([paramentros[k] for k in paramentros])
            resultado = cursor.execute(consulta, tp)
        else:
            consulta = 'SELECT * FROM hoteis \
                        WHERE (estrelas > ? and estrelas < ?) \
                        and (diaria > ? and diaria < ?) \
                        and cidade = ? LIMIT ? OFFSET ?'

            tp = tuple([paramentros[k] for k in paramentros])
            print(tp)
            resultado = cursor.execute(consulta, tp)

        hoteis = []
        for linha in resultado:
            hoteis.append({
                'hotel_id': linha[0],
                'nome': linha[1],
                'estrelas': linha[2],
                'diaria': linha[3],
                'cidade': linha[4]
            })

        return {'hoteis': hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True,
                            help="O campo 'nome' não pode ficar vazio.")
    argumentos.add_argument('estrelas', type=float, required=True,
                            help="O campo 'estrelas' não pode ficar vazio.")
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()

        # status: not found
        return {'msg': f'Hotel {hotel_id} não encontrado!'}, 404

    @ jwt_required()
    def post(self, hotel_id):

        if HotelModel.find_hotel(hotel_id):
            # BadRequest
            return {'msg': f'Hotel id {hotel_id} already exists.'}, 400

        dados = self.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)

        try:
            hotel.save_hotel()
        except:
            return {'msg': 'Erro inesperado.'}, 500

        return hotel.json(), 200  # status: success

    @ jwt_required()
    def put(self, hotel_id):
        dados = self.argumentos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200  # success

        hotel = HotelModel(hotel_id, **dados)

        try:
            hotel.save_hotel()
        except:
            return {'msg': 'Erro inesperado.'}, 500

        return hotel.json(), 201  # created

    @ jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'msg': 'Erro inesperado.'}, 500

            return {'msg': f'Hotel {hotel_id} deleted.'}

        return {'msg': f'Hotel {hotel_id} not found.'}, 404

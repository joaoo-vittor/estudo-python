from flask_restful import Resource, reqparse
import jwt
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required


class Hoteis(Resource):
    # method GET
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


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

    @jwt_required()
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

    @jwt_required()
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

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'msg': 'Erro inesperado.'}, 500

            return {'msg': f'Hotel {hotel_id} deleted.'}

        return {'msg': f'Hotel {hotel_id} not found.'}, 404

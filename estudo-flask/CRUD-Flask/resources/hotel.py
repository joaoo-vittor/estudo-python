from flask_restful import Resource, reqparse
from models.hotel import HotelModel


hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.45,
        'cidade': 'Campina Grande'
    },
    {
        'hotel_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 4.3,
        'diaria': 911.25,
        'cidade': 'São paulo'
    },
    {
        'hotel_id': 'teta',
        'nome': 'Teta Hotel',
        'estrelas': 4.3,
        'diaria': 129.85,
        'cidade': 'João Pessoa'
    },
]


class Hoteis(Resource):
    # method GET
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return hotel

        # status: not found
        return {'msg': f'Hotel {hotel_id} não encontrado!'}, 404

    def post(self, hotel_id):
        dados = self.argumentos.parse_args()
        obj_hotel = HotelModel(hotel_id, **dados)
        novo_hotel = obj_hotel.json()
        hoteis.append(novo_hotel)

        return novo_hotel, 200  # status: success

    def put(self, hotel_id):
        dados = self.argumentos.parse_args()
        obj_hotel = HotelModel(hotel_id, **dados)
        novo_hotel = obj_hotel.json()
        # novo_hotel = {'hotel_id': hotel_id, **dados}

        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200  # success

        hoteis.append(novo_hotel)
        return novo_hotel, 201  # created

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'msg': f'Hotel {hotel_id} deleted'}

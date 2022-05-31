from modelos.banda import Banda
import json

class Bandas:
    bandas = []

    @classmethod
    def agregarBanda(self, banda:Banda):
        self.bandas.append(banda)

    @classmethod
    def obtenerBandas(self):
        self.bandas.sort(key=lambda b: b.nombre)
        return self.to_json(self.bandas)
    
    @classmethod
    def eliminarBanda(self, id:str):
        noCriterio = filter(lambda l: l.id != id, self.bandas)
        self.bandas = list(noCriterio)
        print(self.to_json(self.bandas))
    
    @classmethod
    def votarPorBanda(self, id:str):
        for b in self.bandas:
            if b.id == id:
                b.votos += 1
        print(self.to_json(self.bandas))

    def to_json(obj):
        return json.dumps(obj, default=lambda o: o.__dict__)

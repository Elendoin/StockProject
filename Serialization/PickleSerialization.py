import pickle
from Serialization import ISerialization


class PickleSerialization(ISerialization.Serialization):
    def Serialize(self, data, name):
        try:
            with open(name+'.pickle', 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print('Error! - ' + e)
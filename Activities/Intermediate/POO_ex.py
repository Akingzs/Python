class Carro:
    def __init__(self,nome):
        self._nome = nome
        self._nome_motor = None
        self._fabricante = None
    
    # Fazendo um getter e setter para o motor
    @property
    def motor(self):
        return self._nome_motor
    
    @motor.setter
    def motor(self, nome_motor):
        self._nome_motor = nome_motor
    
    # Fazendo um getter e setter para fabricante
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,nome_fab):
        self._fabricante = nome_fab
    
    def show_vehicle_specs(self):
        # Ao chamar a funcao em uma instancia da Classe, cada atributo recebe uma instancia de outra Classe 
        # que por sua vez possui as funcoes de "Mostrar". menos o nome que ja foi passado como str ao iniciar a instancia
        print(f'Nome: {self._nome}\n{self._nome_motor.show_motor()}\n{self._fabricante.show_fab()}')

class Motor:
    def __init__(self,nome_motor):
        self._nome_motor = nome_motor
    
    def show_motor(self):
        return f'Motor: {self._nome_motor}'
        

class Fabricante:
    def __init__(self,nome_fab):
        self._fabricante = nome_fab
    
    def show_fab(self):
        return f'Fabricante: {self._fabricante}'
    
def main():
    # Celta
    celta = Carro('Celta')
    motor_celta = Motor('Motor XXX 1.0')
    fab_celta = Fabricante('Chevrolet')
    celta.motor = motor_celta
    celta.fabricante = fab_celta

    celta.show_vehicle_specs()
    print()
    # Argo
    argo = Carro('Argo')
    motor_argo = Motor('Motor XXX 1.6')
    fab_argo = Fabricante('Fiat')
    argo.motor = motor_argo
    argo.fabricante = fab_argo

    argo.show_vehicle_specs()
    print()

    # toro
    toro = Carro('toro')
    motor_toro = Motor('Motor XXX 1.0')
    fab_toro = Fabricante('Chevrolet')
    toro.motor = motor_toro
    toro.fabricante = fab_toro

    toro.show_vehicle_specs()

if __name__ == '__main__':
    main()
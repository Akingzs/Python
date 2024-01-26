from Composicao import Dono

def main():
    arthur = Dono('Arthur',24)
    carlos = Dono('Carlos',52)

    arthur.buy_car('Chevrolet','Celta',2010)
    arthur.buy_car('Fiat','Argo',2020)
    arthur.show_cars()
    print('######')
    
    arthur.sell_cars('celta')
    print('######')
    
    arthur.show_cars() 

if __name__ == "__main__":
    main()
import pandas as pd



def main():

    path = pd.read_excel('C:/Users/victi/Documents/Emails.xlsx')

    datos = path['Email']
    print(datos)





if __name__ == '__main__':
    main()



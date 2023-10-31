import func as dbHandler
from flask import Flask, render_template, redirect, request


class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def editar_item():
        if(request.form['name'] != '' and request.form['quantity'] != ''):
            quantity = request.form['quantity']
            name = request.form['name']
            for product in dbHandler.retrieveProduct():
                if product[0]==name:
                    dbHandler.editProduct(quantity, name)
                    return print("Quantidade atualizada com sucesso")
        return print('Produto não encontrado no estoque. Nome não existe')


    def remover_estoque():
        if(request.form['name'] != ''):
            name = request.form['name']
            for product in dbHandler.retrieveProduct():
                if product[0]==name:
                    dbHandler.removeProduct(name)
                    return print("Produto removido com sucesso")

        else:
            return print("Produto não existe. Nome inválido")

    def adicionar_item():
        if(request.form['name'] != '' and request.form['quantity'] != ''):
            name = request.form['name']
            quantity = request.form['quantity']
            products = dbHandler.retrieveProduct()

            if products:
                for product in products:
                    if product[0]==name and product[1]==quantity:
                        return print("Produto inválido. Nome já existe!")
                    dbHandler.insertProduct(name, quantity)
                    print(f"{name} foi adicionado ao estoque com uma quantidade de {quantity}.")
                    return redirect('/dashboard')
                    
            
product = ('name', 'quantity')



def signup():
    if request.method=='POST':
        if(request.form['username']!='' and request.form['password']!=''): #se as áreas do form não forem vazias, username receber o input do form com nome username
            username = request.form['username']
            password = request.form['password']
            users = dbHandler.retrieveUsers()		
            
            if users:
                for user in users:
                      if user[0]==username and user[1]==password:
                            return redirect('/signup')
                dbHandler.insertUser(username, password)
                return redirect('/login') #render_template('/teste.html', users = users)
			
    #elif request.method=='GET':
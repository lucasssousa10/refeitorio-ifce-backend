# refeitorio-ifce-backend
Sistema para gerenciamento do refeitório IFCE Campus Umirim

Cada um deverá fazer uma **Tarefa** especificada na aba **Projetos > IFCE Meu Cardápio**.

O objetivo é fazer um CRUD em Flask de cada tabela do Banco de Dados. Isto é, 
deverá ser feito os seguintes métodos: criar, selecionar, atualizar e deletar.

***

Por exemplo, para uma tabela Compras:
- métodos a serem feitos: 
criar_compra
selecionar_compra
atualizar_compra
deletar_compra

exemplo do método criar_compra:
(image que a tabela Compras tem os atributos data e valor)
`
@app.route('/api/compras/criar', methods=['POST'])

def criar_compra():

    if not request.json or not 'data' in request.json:
    
        abort(400)
        
    if not request.json or not 'valor' in request.json:
    
        abort(400)

    compra = {
        'data': request.json['data'],
        'valor': request.json['valor'],
        'done': False
    }

    # SALVAR os dados na compra no Banco de Dados POSTGRESQL

    # se deu certo, retornar o objeto salvo, no caso o objeto que representa a compra
    return jsonify({'compra': compra}), 201
    # ou retornar:
    return jsonify({'result': True})

    # se não deu certo, retornar
    return jsonify({'result': False})
`

Link de referência: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

dados = ["id","nome","horo_sazonal_id","tipo_alimentacao","modalidade_tarifaria","periodosConsumo","periodosDemanda"]
controller = "SubgruposTarifarios"

print("rowsPerPage = app.config['ROWS_PER_PAGE']")
print("page = request.args.get('page', 1, type=int)")
for dado in dados:
    print("{}Filter = request.args.get('{}', None)".format(str(dado), str(dado)))


print("\nquery = {}.query.order_by({}.id)\n".format(controller, controller))
for dado in dados:
    print(
        "if ({}Filter != None):\n\tquery = query.filter(\n\t{}.{} == {}Filter)\n".format(
            str(dado), controller, str(dado), str(dado)
        )
    )


print("\n\n")


controller1 = controller
controller1 = controller1[0].lower() + controller1[1:]
print("for {} in {}s:\n\tdata = {{}}\n\n".format(controller1, controller1))

print("View")
for dado in dados:
    print("\tdata['{}'] = {}.{}".format(dado, controller1, dado))


print("{} = {}(".format(controller1, controller))
for dado in dados:
    if dado != "id":
        if dados.index(dado) != len(dados) - 1:
            print("{}=data['{}'],".format(dado, dado))
        else:
            print("{}=data['{}']".format(dado, dado))

print(")\n\n\n")

print("EDIT")
for dado in dados:
    if dado != "id":
        print("\t{}.{} = data['{}']".format(controller1, dado, dado))

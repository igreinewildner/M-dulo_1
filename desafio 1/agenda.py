contatos = []


def adicionar_contato(nome_contato, telefone_contato, email_contato):
  contato_completo = {"Nome:": nome_contato, "Telefone:": telefone_contato, "Email:": email_contato, "Favorito": False}
  contatos.append(contato_completo)
  print(f"Seu contato {nome_contato}, {telefone_contato}, {email_contato} foi adicionado com sucesso!")
  return contatos

def visualizar_lista(contatos):
    print("\nLista de contatos:")
    if not contatos:
      print("A lista de contatos está vazia.")
    else:
     for indice, contato in enumerate(contatos, start=1):
      print(f"{indice}. {contato['Nome:']}, {contato['Telefone:']}, {contato['Email:']}")
    

def editar_contato(contatos, indice_contato, novo_contato):
  indice_contato_ajustado = int(indice_contato) -1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado] = novo_contato
    print(f"Contato {indice_contato} atualizado.")
  else:
    print("Índice do contato inválido.")
  return contatos

def marcar_favoritos(contatos, indice_contato_favorito):
  indice_contato_favorito_ajustado = int(indice_contato_favorito) -1
  if indice_contato_favorito_ajustado >= 0 and indice_contato_favorito_ajustado < len(contatos):
    contatos[indice_contato_favorito_ajustado]['Favorito'] = True
    print(f"Contato {indice_contato_favorito} favoritado.")
  return contatos 

def lista_favoritos(contatos, indice_contato_favorito):
  indice_contato_favorito_ajustado = int(indice_contato_favorito)-1
  if indice_contato_favorito_ajustado in contatos:
    print("Contatos favoritos:", contatos)

def deletar_contato (contatos, indice_contato):
  indice_contato_deletado = int(indice_contato) -1
  for indice_contato_deletado in contatos:
   contatos.remove(indice_contato_deletado)
   print(f"Contato {indice_contato} deletado.")
  return
  

while True:
    print("\nAgenda de contatos:")
    print("1. Adcionar um contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar contato")
    
    escolha = input("Digite a sua escolha:")

    if escolha == "1": 
     nome_contato = input("Digite o nome do contato que deseja adicionar:")
     telefone_contato = input("Digite o telefone do contato que deseja adicionar:")
     email_contato =input("Digite o email do contato que deseja adicionar:")
     contato_completo = nome_contato, telefone_contato, email_contato
     adicionar_contato(nome_contato, telefone_contato, email_contato)

    elif escolha == "2":
      visualizar_lista(contatos)
 

    elif escolha == "3":
     visualizar_lista(contatos)
     indice_contato = input("Digite o número do contato que deseja editar:")
     print("Preencha os dados abaixo")
     novo_nome_contato = input("Digite o nome do contato:")
     novo_telefone_contato = input("Digite o telefone do contato:")
     novo_email_contato =input("Digite o email do contato:")
     novo_contato = {"Nome:": novo_nome_contato, "Telefone:": novo_telefone_contato, "Email:": novo_email_contato, "Favorito": False}
     contatos = editar_contato(contatos, indice_contato, novo_contato)
     
    elif escolha == "4":
      visualizar_lista(contatos)
      indice_contato_favorito = input("Digite o número do contato que deseja favoritar:")
      contatos = marcar_favoritos(contatos, indice_contato_favorito)

    elif escolha == "5":
     marcar_favoritos(contatos, indice_contato_favorito)
     print("Lista de contatos favoritos: contato", indice_contato_favorito)

    elif escolha == "6":
     visualizar_lista(contatos)
     indice_contato_deletado = input("Digite o indice do contato que deseja deletar:")
     deletar_contato(contatos, indice_contato_deletado)
     
     
 

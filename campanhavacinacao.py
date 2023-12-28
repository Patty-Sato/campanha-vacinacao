print("Petshop PuppyBel: Campanha de Vacinação de Cães e Gatos")
respostas = ['SIM', 'S', 'YES', 'Y']
animal_seguro = input("Seu animalzinho está com coleira ou em uma gaiola? ").upper()
if animal_seguro in respostas:
    total = 1
    check = "SIM"
    while check in respostas:
        especie = input("Informe a espécie do animal - Gato ou Cachorro: ").upper()
        nome = input("Informe o nome do animal: ").upper()
        print("Espécie", especie, "Animal", nome, "Número ", total)
        for i in range(3):
            print("Vacina {} - OK".format(i + 1))
        total += 1
        check = input("Há mais algum pet a ser cadastrado? ").upper()
    print("Total de animais que participaram da campanha: ", total - 1)
else:
    print("Por favor, para a segurança do seu pet, coloque uma coleira ou prenda seu "
          "animalzinho em uma gaiola")






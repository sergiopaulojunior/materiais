import Banco_de_dados as bd  # IMPORTA ARQUIVO Banco_de_dados DA PASTA Archives
import os
import sys

sys.path

class Materiais():
    def __init__(self, codigo, nome, quantidade):
        self.id = codigo
        self.nome = nome
        self.quantidade = quantidade


def inserir(cod, nome, qtd):
    try:
        bd.conectar()  # CONECTA NO BD
        bd.cur.execute('insert into materiais values (?, ?, ?)', (cod, nome, qtd))  # EXECUTAR COMANDO SQL
        print('\nMaterial inserido com sucesso. ')
    except bd.sqlite3.IntegrityError:  # ERRO CASO HAJA CODIGO CADASTRADO
        print('Erro ao inserir material: Ja existe um produto cadastrado com o codigo inserido')
    except ValueError: # ERRO CASO INSIRA STRING EM CAMPO NUMERICO
        print('Código precisa ser um valor numerico. ')
    finally:
        bd.con.commit()  # SALVA ALTERAÇÕES NA TABELA


def exibirtodos():
    bd.conectar()
    bd.cur.execute('SELECT * FROM materiais')
    dadoss = bd.cur.fetchall()

    for linha in dadoss:
        print('Código: %s, Nome: %s, Quantidade:%s' % linha)


def exibir(codprod):
    try:
        bd.conectar() # CONECTAR NO BD
        bd.cur.execute('SELECT * FROM materiais WHERE codigo = %s' % codprod)  # EXECUTAR COMANDO SQL
        dadoss = bd.cur.fetchall()

        for linha in dadoss:
            print('Código: %s, Nome: %s, Quantidade:%s' % linha)
    except:
        print('Falha ao consultar')


def excluir(codprod):
    try:
        bd.conectar()
        bd.cur.execute('DELETE FROM materiais WHERE codigo = %s' % codprod)
        print('Material excluido com sucesso. ')
    except:
        print('Não existe material com o codigo informado. ')
    finally:
        bd.con.commit()  #SALVA ALTERAÇÕES NA TABELA


def alterar(codprod):
    try:
        bd.conectar()
        exibir(codprod)
        nnome = input('Entre com o novo nome: ')
        nqtd = int(input('Entre com a nova quantidade: '))
        bd.cur.execute('UPDATE materiais set nome = ?, quantidade = ? WHERE codigo = ?', (nnome, nqtd, codprod))
        print('Material alterado com sucesso. ')
    except:
        print('Erro ao alterar material. ')
    finally:
        bd.con.commit()  #SALVA ALTERAÇÕES NA TABELA


def limparbd():
    try:
        bd.conectar()
        bd.cur.execute('DELETE FROM materiais')  #sqlite (DELETE FROM) mysql(TRUNCATE TABLE)
    except:
        print('Erro ao limpar dados')
    finally:
        bd.con.commit()


def menu():
    opc = 99  # INICIALIZA VARIAVEL OPC
    while opc != 0:
        os.system('cls')
        print('             MENU            ')
        print('1 - INSERIR MATERIAL')
        print('2 - EXIBIR TODOS MATERIAIS')
        print('3 - EXIBIR MATERIAL')
        print('4 - ALTERAR DADOS DE MATERIAIS')
        print('5 - EXCLUIR MATERIAL')
        print('6 - EXCLUIR TODOS OS REGISTROS')
        print('0 - SAIR \n' )
        try:
            opc = int(input('Entre com a opção desejada: '))
            if opc == 1:
                os.system('cls')
                print('Inserção de material. \n' )
                cod = int(input('Entre com o codigo: '))
                nome = input('Entre com o nome: ')
                qtd = int(input('Entre com a quantidade: '))
                inserir(cod, nome, qtd)
                x = int(input('\nPressione [2] para retornar ao menu. \n'))
                if x == 2:
                    menu()
                else:
                    print('Opção invalida, saindo do programa')
                    break
            elif opc == 2:
                os.system('cls')
                print('     Produtos cadastrados \n')
                exibirtodos()
                x = int(input('\nPressione [2] para retornar ao menu. \n'))
                if x == 2:
                    menu()
                else:
                    print('Opção invalida, saindo do programa')
                    break
            elif opc == 3:
                os.system('cls')
                x = int(input('Digite o codigo do produto que deseja consultar: '))
                exibir(x)
                x = int(input('\nPressione [2] para retornar ao menu. \n'))
                if x == 2:
                    menu()
                else:
                    print('Opção invalida, saindo do programa')
                    break
            elif opc == 4:
                os.system('cls')
                x = int(input('Entre com o codigo do produto que deseja alterar: '))
                alterar(x)
                x = int(input('\nPressione [2] para retornar ao menu. \n'))
                if x == 2:
                    menu()
                else:
                    print('Opção invalida, saindo do programa')
                    break
            elif opc == 5:
                os.system('cls')
                print('      Excluir produto  \n')
                x = int(input('Entre com o código do produto que deseja excluir: '))
                excluir(x)
                x = int(input('\nPressione [2] para retornar ao menu. \n'))
                if x == 2:
                    menu()
                else:
                    print('Opção invalida, saindo do programa')
                    break
            elif opc == 6:
                os.system('cls')
                print('Metodo de exclusão de dados\n ')
                print('Ao executar esse comando todos os registros serão apagados e não sera possivel reverter\n')
                x = int(input('Digite [1] para excluir todos os regisros: '))
                if x == 1:
                    y = input('Tem certeza ? [s] [n]: ')
                    if y == 's':
                        limparbd()
                        print('Registros apagados com sucesso')
                        z = int(input('\nPressione [2] para retornar ao menu. \n'))
                        if z == 2:
                            menu()
                        else:
                            print('Opção invalida, saindo do programa')
                            break
                    elif y == 'n':
                        print('Registros não serao exluidos')
                        z = int(input('\nPressione [2] para retornar ao menu. \n'))
                        if z == 2:
                            menu()
                        else:
                            print('Opção invalida, saindo do programa')
                else:
                    print('Opção invalida, retornando ao menu')
            elif opc == 0:
                print('saindo do programa. ')
                break
            else:
                print('Opcao invalida \n. ')
                menu()
        except ValueError:
            print('Entre com um valor numerico. \n')


bd.criartabela()  # EXECUTA FUNCAO PARA CRIAR TABELA NO BD
menu()  # EXECUTA FUNCAO MENU

def loginUsuario(cini):
    if cini.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else: print('Bem-vindo, ' + cini)

loginUsuario('Admin')
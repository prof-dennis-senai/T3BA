def verificar_permissao(func):
    print("Verificando acesso...")
    def wrapper(*args, **kwargs):
        print("Antes da chamada")
        user = args[1] if len(args) > 1 else kwargs.get("user", "visitante")
        permissao = {}
        if user == "admin":
            permissao["add"] = True
            permissao["edit"] = True
            permissao["delete"] = True
            permissao["view"] = True
        
        elif user == "editor":
            permissao["add"] = False
            permissao["edit"] = True
            permissao["delete"] = False
            permissao["view"] = True

        else:
            permissao["add"] = False
            permissao["edit"] = False
            permissao["delete"] = False
            permissao["view"] = False

        chamada = func(*args, **kwargs, permissao=permissao)
        print("Depois da chamada")
        return chamada

    return wrapper



def limitar_acesso(tipo_acesso):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Tipo da permissão: {tipo_acesso}")
            permissao = kwargs.get("permissao", {})
            if permissao.get(tipo_acesso, False):
                return func(*args, **kwargs)
            usuario = args[1] if len(args) > 1 else kwargs.get("user", "visitante")
            print(f"Acesso negado para: {usuario}")
        return wrapper
    return decorator


@verificar_permissao
@limitar_acesso("view")
def executar_query(sql,**kwargs):
    print(f"Executando: {sql}")

print("----")
executar_query("SELECT * FROM alunos")

print("----")
executar_query("SELECT * FROM alunos", user="admin")

print("----")
executar_query("SELECT * FROM alunos", user="editor")
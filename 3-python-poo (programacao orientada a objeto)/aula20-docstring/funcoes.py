""" Descrição rápida e simples

Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad tempore voluptatibus impedit dicta dolor in dignissimos iure facere quia quo, laudantium distinctio! Voluptatum veniam cumque velit, mollitia exercitationem porro quos.
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque facilis, sint est illum accusantium eveniet eos modi, odio asperiores corporis harum! Repellendus similique nemo ex recusandae. Voluptatum vel nulla fugit!
Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos aperiam, nostrum quaerat vel eius, voluptate non voluptatibus cupiditate harum velit labore magni exercitationem iste deleniti rem fugit, delectus unde corporis?

"""

variavel_1 = 'valor 1'

def soma(x, y):
    """Soma x e y"""
    return x + y

def multiplica(x, y, z = None):
    """Soma x, y, z

    Multiplica x, y, e z. O programador por omitir a variável z caso não tenha necessidade de usá-la
    """
    if not z:
        return x * y
    else:
        return x * y * z

variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'
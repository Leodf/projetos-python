""" Descrição rápida e simples

Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad tempore voluptatibus impedit dicta dolor in dignissimos iure facere quia quo, laudantium distinctio! Voluptatum veniam cumque velit, mollitia exercitationem porro quos.
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque facilis, sint est illum accusantium eveniet eos modi, odio asperiores corporis harum! Repellendus similique nemo ex recusandae. Voluptatum vel nulla fugit!
Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos aperiam, nostrum quaerat vel eius, voluptate non voluptatibus cupiditate harum velit labore magni exercitationem iste deleniti rem fugit, delectus unde corporis?

"""

class MinhaClasse:
    """Documento Normal"""

    atributo = 1
    atributo2 = 'valor'

    def __init__(self, texto):
        """Inicializa os dados
        
        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de 100 caracteres na tela

        :param texto: um texto de 100 caracteres
        :type texto: str

        :return: O texto de 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for uma string
        """
        if not isinstance(texto, str):
            raise TypeError('texto precisa ser uma string.')
        if len(texto) > 100:
            raise ValueError('texto precisa ter 100 caracteres ou menos')

        return texto


   
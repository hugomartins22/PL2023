import ply.lex as lex
from sys import argv

class MyLexer():
    states = (
        ('comment', 'exclusive'),
    )
    tokens = (
        "FUNCAO",
        "WHILE",
        "INT",
        "MANY_LINE_I",
        "MANY_LINE_F",
        "COMMENTS",
        "SINGLE_COMMENT_LINE",
        "SEMI_COLON",
        "COMMA",
        "MULTIPLY",
        "DIVIDE",
        "MINUS",
        "GREATER",
        "PAROPEN",
        "PARCLOSE",
        "COPEN",
        "CCLOSE",
        "EQUAL",
        "NOME",
        "FOR",
        "IN",
        "PROGRAM",
        "RANGE_POINTS",
        "NUMBER",
        "BRACKETOPEN",
        "BRACKETCLOSE",
        "IF",
        "MINOR",
    )

    def __init__(self):
        self.lexer: lex.Lexer = lex.lex(module=self)

        self.pars = 0
        self.cbrackets = 0
        self.brackets = 0

        self.reserved_words = {
            "function": "FUNCAO",
            "while": "WHILE",
            "int": "INT",
            "for": "FOR",
            "in": "IN",
            "program": "PROGRAM",
            "if": "IF",
            "else": "ELSE",
                }

    t_ANY_ignore = ' \t\n'

    t_MINOR = "<"
    t_SINGLE_COMMENT_LINE = "//.*"
    t_SEMI_COLON = ";"
    t_COMMA = ","
    t_comment_COMMENTS = r"[^(\/\*)]+"
    t_RANGE_POINTS = r'\.\.'
    t_NUMBER = r'\d+'
    t_MULTIPLY = r'\*'
    t_DIVIDE = r'\/'
    t_MINUS = r'\-'
    t_GREATER = r'\>'
    t_EQUAL = r'\='

    def t_BRACKETOPEN(self, t):
        r"\["
        self.brackets += 1
        return t

    def t_BRACKETCLOSE(self, t):
        r"\]"
        if self.brackets == 0:
            print("Unexpected ]")
            return t
        self.brackets -= 1
        return t

    def t_PAROPEN(self, t):
        r"\("
        self.pars += 1
        return t

    def t_PARCLOSE(self, t):
        r"\)"
        if self.pars == 0:
            print("Unexpected )")
            return t
        self.pars -= 1
        return t

    def t_COPEN(self, t):
        r"\{"
        self.cbrackets += 1
        return t

    def t_CCLOSE(self, t):
        r"\}"
        if self.cbrackets == 0:
            print("Unexpected }")
            return t
        self.cbrackets -= 1
        return t

    def t_MANY_LINE_I(self, t):
        r"\/\*"
        t.lexer.begin('comment')
        return t

    def t_comment_MANY_LINE_F(self, t):
        r"\*\/"
        t.lexer.begin('INITIAL')
        return t

    def t_NOME(self, t):
        r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"
        t.type = self.reserved_words.get(t.value, "NOME")
        return t

    def t_ANY_error(self, t):
        print("Illegal character", t.value[0])
        t.lexer.skip(1)
        return t

    def dalhe(self, data):
        self.lexer.input(data)

data="""
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""
def main():
    lexer=MyLexer()
    lexer.dalhe(data)

    while tok := lexer.lexer.token():
        print(tok)

if __name__ == "__main__":
    main()
import re


def lexer(code):
  tokens = []
  keywords = {'int', 'float', 'if', 'else', 'return'}
  operators = {'+', '-', '*', '/'}
  separators = {'(', ')', '{', '}', ';'}

  lines = code.split('\n')

  for line_number, line in enumerate(lines, start=1):
    line = line.strip()
    if not line or line.startswith('#'):
      continue


    for token in re.findall(r'\b\w+\b|[+\-*/();{}]', line):
      if token in keywords:
        tokens.append((token.upper(), token, line_number))
      elif token in operators or token in separators:
        tokens.append((token, None, line_number))
      else:
        tokens.append(('IDENTIFIER', token, line_number))

  return tokens


def simple_semantic_analyzer(tokens):
  declared_variables = set()

  for token_type, value, line_number in tokens:
    if token_type == 'IDENTIFIER':
      if value.isdigit():
        print(
            f"Error semántico en la línea {line_number}: La variable '{value}' no puede ser un número."
        )
      elif value in declared_variables:
        print(
            f"Error semántico en la línea {line_number}: La variable '{value}' ya ha sido declarada."
        )
      else:
        declared_variables.add(value)



codigo = """
int main() {
    int x = 10;
    float y = 3.14;

    if (x > 5) {
        int z = 20;
        y = y * z;
    } else {
        int x = 5;  
        y = y / x;
    }

    return 0;
}
"""

tokens = lexer(codigo)
simple_semantic_analyzer(tokens)

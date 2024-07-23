import sys
import math
from typing import Any

PROMPT = '>>> '

def run_calc(context: dict[str, Any] | None = None) -> None:
    """Run interactive calculator session in specified namespace"""
    if context is None:
        context = {}
    
    # Ensure no access to builtins
    context['__builtins__'] = None
    
    while True:
        try:
            user_input = input(PROMPT)
            result = eval(user_input, context)

            print(result)
        except EOFError:
            break
        except Exception as e:
            print(e)

if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)

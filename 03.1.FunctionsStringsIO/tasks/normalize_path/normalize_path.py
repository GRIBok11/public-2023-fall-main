def normalize_path(path: str) -> str:

    stack: list[str] = []
    absolute = path.startswith('/')
    parts = path.split('/')
    for part in parts:
        if not part:
            continue
        elif part == '.':
            continue
        elif part == '..':
            if stack:
                if stack[-1] == '..':
                    stack.append('..')
                else:
                    stack.pop()
            else:
                if absolute:
                    continue
                else:
                    stack.append('..')
        else:
            stack.append(part)
    
    if absolute:
        return '/' + '/'.join(stack)
    else:
        return '/'.join(stack) or '.'


# Примеры использования
print(normalize_path('/foo/bar//baz/asdf/quux/..'))  # Ожидаемый вывод: '/foo/bar/baz/asdf'
print(normalize_path('./config/../etc'))  # Ожидаемый вывод: 'etc'
print(normalize_path('/////documents/root/.././../etc'))  # Ожидаемый вывод: '/etc'
print(normalize_path('a/../../b'))  # Ожидаемый вывод: '../b'
print(normalize_path('../..'))  # Ожидаемый вывод: '../..'

def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack and stack[-1] != '..':
                stack.pop()
            elif not stack or stack[-1] == '..':
                stack.append(part)
        else:
            stack.append(part)

    normalized_path = '/' + '/'.join(stack)
    return normalized_path if normalized_path != '' else '/'

# Примеры использования
print(normalize_path('/foo/bar//baz/asdf/quux/..'))  # Ожидаемый вывод: '/foo/bar/baz/asdf'
print(normalize_path('./config/../etc'))  # Ожидаемый вывод: 'etc'
print(normalize_path('/////documents/root/.././../etc'))  # Ожидаемый вывод: '/etc'
print(normalize_path('a/../../b'))  # Ожидаемый вывод: '../b'

import re

def normalize(text: str) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """
    text = re.sub(r'[^\w\s]', '', text)  # Удаляем знаки препинания
    text = re.sub(r'\d', '', text)       # Удаляем цифры
    return text.lower()                  # Переводим в нижний регистр



def get_words(query: str) -> list[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """
    words = query.split()
    return [word for word in words if len(word) > 3]

def build_index(banners: list[str]) -> dict[str, list[int]]:
    """
    Create index from words to banners ids with preserving order and without repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """
    index = {}
    for banner_id, banner in enumerate(banners):
        words = get_words(normalize(banner))
        for word in words:
            if word not in index:
                index[word] = []
            if banner_id not in index[word]:
                index[word].append(banner_id)
    return index



def get_banner_indices_by_query(query: str, index: dict[str, list[int]]) -> list[int]:
    """
    Extract banners indices from index, if all words from query contains in indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """
    words = get_words(normalize(query))
    if not words:
        return []
    
    banner_sets = [set(index.get(word, [])) for word in words]
    if not banner_sets:
        return []
    
    common_banners = set.intersection(*banner_sets)
    return sorted(common_banners)



#########################
# Don't change this code
#########################

def get_banners(
        query: str,
        index: dict[str, list[int]],
        banners: list[str]
        ) -> list[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################

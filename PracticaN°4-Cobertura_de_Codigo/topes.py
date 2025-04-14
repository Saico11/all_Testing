#Actividad_3

def stats(lst):
    min_val = None  
    max_val = None  
    freq = {}
    
    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        freq[i] = freq.get(i, 0) + 1  

    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    
    if n == 0:
        median = None
    elif n % 2 == 0:
        middle = n // 2
        median = (lst_sorted[middle - 1] + lst_sorted[middle]) / 2
    else:
        median = lst_sorted[n // 2]

    max_freq = max(freq.values(), default=None)
    mode = [k for k, v in freq.items() if v == max_freq] if max_freq else []

    return {
        "list": lst,
        "min": min_val,
        "max": max_val,
        "median": median,
        "mode": mode
    }

def test_stats():
    # Caso 1: Lista vacia
    result = stats([])
    assert result["min"] is None
    assert result["max"] is None
    assert result["median"] is None
    assert result["mode"] == []

    # Caso 2: Lista con un elemento
    result = stats([5])
    assert result["min"] == 5
    assert result["max"] == 5
    assert result["median"] == 5
    assert result["mode"] == [5]

    # Caso 3: Lista con longitud par y repeticiones
    result = stats([1, 3, 3, 7])
    assert result["min"] == 1
    assert result["max"] == 7
    assert result["median"] == 3.0
    assert result["mode"] == [3]  # Aqui estaba el problema

    # Caso 4: Lista con todos elementos iguales
    result = stats([2, 2, 2])
    assert result["min"] == 2
    assert result["max"] == 2
    assert result["median"] == 2
    assert result["mode"] == [2]

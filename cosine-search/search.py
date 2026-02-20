import math
from collections import Counter
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def text_to_vector(text):
    words = text.lower().split()
    return Counter(words)


def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([v**2 for v in vec1.values()])
    sum2 = sum([v**2 for v in vec2.values()])
    
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return numerator / denominator

if __name__ == "__main__":
    
    numbers = [2, 4, 6, 8, 10, 12, 14]
    target = 8

    print("Linear Search Result:", linear_search(numbers, target))
    print("Binary Search Result:", binary_search(numbers, target))

    with open("documents.txt", "r") as file:
        documents = file.readlines()

    query = "machine learning and python"
    query_vector = text_to_vector(query)

    print("\nCosine Similarity Search Results:\n")

    for i, doc in enumerate(documents):
        doc_vector = text_to_vector(doc)
        score = cosine_similarity(query_vector, doc_vector)
        print(f"Document {i+1} Similarity Score: {score:.4f}")

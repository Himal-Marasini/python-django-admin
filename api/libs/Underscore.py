class U:
    @staticmethod
    def groupBy(collection, iteratee):
        result = {}
        for item in collection:
            key = item if isinstance(item, str) else iteratee(item)
            result.setdefault(key, []).append(item)
        return result
    
    @staticmethod
    def map(collection, iteratee):
        result = []
        if isinstance(collection, dict):
            for key, value in collection.items():
                result.append(iteratee(value, key, collection))
        else:
            for index, item in enumerate(collection):
                result.append(iteratee(item, index, collection))
        return result
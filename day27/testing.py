def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
import random    
    
class TestDataEmptyArray:
    
    @classmethod
    def get_array(cls):
        return []
    
class TestDataUniqueValues:
    
    curr=None
    
    @classmethod
    def get_array(cls):
        size=random.randint(2,10)
        cls.curr=random.sample(range(100),size)
        return cls.curr
    
    @classmethod
    def get_expected_result(cls):
        l=cls.curr
        return l.index(min(l))
    
class TestDataExactlyTwoDifferentMinimums:
    
    curr=None
    
    @classmethod
    def get_array(cls):
        size=random.randint(2,10)
        cls.curr=random.sample(range(100),size)
        cls.curr.insert(random.randint(0,9),min(cls.curr))
        
        return cls.curr
    
    @classmethod
    def get_expected_result(cls):
        l=cls.curr
        return l.index(min(l))

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
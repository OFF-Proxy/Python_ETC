def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data #←ここでdataが一度、返却される
def main():
    g = (i for i in (1,2,3,4,5))
    for data in g:
        print(data)
        if data > 2:
            break

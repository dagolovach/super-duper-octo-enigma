import pprint

def testing_type(var) -> bool:
    return isinstance(var, (int, float))

def printing(text: str) -> None:
    pprint.pprint(text)

def new_feature():
    pass

if __name__ == "__main__":
    printing('Hello World!')
    if testing_type('str'):
        print('Int or Float')
    else:
        print('Other')

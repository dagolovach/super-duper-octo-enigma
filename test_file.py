
def testing_type(var) -> bool:
    return isinstance(var, (int, float))


if __name__ == "__main__":
    if testing_type('str'):
        print('Int or Float')
    else:
        print('Other')

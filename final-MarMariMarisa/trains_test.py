"""
This file has been provided to you to help verify that your implementation of
the product class is working correctly. It is strongly recommended that you
uncomment the tests below one at a time so that you can focus on getting a
single test to pass before moving on to the next test.
"""
from trains import *

def test_create_product():
    # setup
    product_code = "ABCD-1234"
    name = "Washing Machine"

    # invoke
    product = Product(product_code, name)

    # analyze
    assert product_code == product.get_product_code()
    assert name == product.get_name()
    assert "ABCD-1234 (Washing Machine)" == repr(product)

def test_products_equal():
    # setup
    product_code = "ZQXG-5422"
    name = "Microwave Oven"
    product1 = Product(product_code, name)
    product2 = Product(product_code, name)
    expected = True

    # invoke
    actual = product1 == product2

    # analyze
    assert expected == actual

def test_products_hashable():
    # setup
    product1 = Product("RJSJ-0375", "Product 1")
    product2 = Product("RJSJ-0375", "Product 2")
    product3 = Product("KDSJ-0475", "Product 3")
    a_set = set()

    # invoke
    try:
        a_set.add(product1)
        a_set.add(product2)
        a_set.add(product3)

        # analyze
        assert 2 == len(a_set)
        assert product1 in a_set
        assert product2 in a_set
        assert product3 in a_set
    except TypeError:
        assert False, "Unhashable type error"

def test_products_sortable():
    # setup
    product1 = Product("TAFS-1197", "Product 1")
    product2 = Product("MSSJ-0799", "Product 2")
    product3 = Product("PBSJ-0711", "Product 3")
    a_list = [product1, product2, product3]

    # invoke
    a_list.sort()

    # analyze
    assert product2 == a_list[0]
    assert product3 == a_list[1]
    assert product1 == a_list[2]

def test_create_train_car():
    # setup
    capacity = 10

    # invoke
    train_car = TrainCar(capacity)

    # analyze
    assert capacity == train_car.get_capacity()
    assert train_car.is_empty()
    assert not train_car.is_full()
    assert "[]" == str(train_car)

def test_load_not_full():
    # setup
    capacity = 2
    train_car = TrainCar(capacity)
    product = Product("12345", "Product 1")

    # invoke
    train_car.load(product)

    # analyze
    assert not train_car.is_empty()
    assert not train_car.is_full()
    assert "[" + str(product) + "]" == str(train_car)

def test_load_full():
    # setup
    capacity = 2
    train_car = TrainCar(capacity)
    product1 = Product("12345", "Product 1")
    product2 = Product("09876", "Product 2")

    # invoke
    train_car.load(product1)
    train_car.load(product2)

    # analyze
    assert not train_car.is_empty()
    assert train_car.is_full()
    assert "[" + str(product2) + ", " + str(product1) + "]" == str(train_car)

def test_load_error():
    # setup
    capacity = 1
    train_car = TrainCar(capacity)
    train_car.load(Product("09876", "Product 1"))

    try:
        # invoke
        train_car.load(Product("12345", "Product 2"))
        assert False, "Loaded product onto a full train car"
    except ValueError:
        pass

def test_unload_empty():
    # setup
    capacity = 1
    train_car = TrainCar(capacity)
    product = Product("ABCD-1234", "Washing Machine")
    train_car.load(product)

    # invoke
    actual = train_car.unload()

    # analyze
    assert product is actual
    assert train_car.is_empty()
    assert not train_car.is_full()
    assert "[]" == str(train_car)

def test_unload_not_empty():
    # setup
    capacity = 2
    train_car = TrainCar(capacity)

    product1 = Product("ABCD-1234", "Washing Machine")
    product2 = Product("XYZQ-9822", "Microwave Oven")
    train_car.load(product1)
    train_car.load(product2)

    # invoke
    actual = train_car.unload()

    # analyze
    assert product2 is actual
    assert not train_car.is_empty()
    assert not train_car.is_full()
    assert "[" + str(product1) + "]" == str(train_car)

def test_unload_error():
    # setup
    capacity = 1
    train_car = TrainCar(capacity)

    # invoke
    try:
        train_car.unload()
        assert False, "Unloaded from an empty train car"
    except ValueError:
        pass

def test_load_train():
    # setup
    product1 = Product("A1", "P1")
    product2 = Product("B2", "P2")
    product3 = Product("C3", "P3")
    product4 = Product("D4", "P4")
    shipment = [product1, product2, product3, product4]
    capacity = 2
    expected = "[[" + str(product2) + ", " + str(product1) + "], " \
        + "[" + str(product4) + ", " + str(product3) + "]]"

    # invoke
    train = load_train(shipment, capacity)

    # analyze
    assert expected == str(train)

def test_unload_train():
    # setup
    product1 = Product("A1", "P1")
    product2 = Product("B2", "P2")
    product3 = Product("C3", "P3")
    product4 = Product("D4", "P4")
    shipment = [product1, product2, product3, product4]
    expected = [product2, product1, product4, product3]
    capacity = 2
    train = load_train(shipment, capacity)

    # invoke
    actual = unload_train(train)

    # analyze
    assert expected == actual


    

"""
Additional tests below not provided to students.
"""
def test_create_product_again():
    # setup
    product_code = "XYZQ-9990"
    name = "Robby the Robot"

    # invoke
    product = Product(product_code, name)

    # analyze
    assert product_code == product.get_product_code()
    assert name == product.get_name()
    assert "XYZQ-9990 (Robby the Robot)" == repr(product)

def test_products_not_equal():
    # setup
    product1 = Product("54321", "Washer")
    product2 = Product("54322", "Washer")
    expected = False

    # invoke
    actual = product1 == product2

    # analyze
    assert expected == actual

def test_product_not_equal_type():
    # setup
    product1 = Product("54321", "Washer")
    a_string = "this is a test"
    expected = False

    try:
        # invoke
        actual = product1 == a_string

        # analyze
        assert expected == actual
    except AttributeError:
        assert False, "strings do not have a serial number"

def test_product_hash():
    # setup
    product_code = "ABCD-4567"
    product = Product(product_code, "Dryer")
    expected = hash(product_code)

    # invoke
    actual = hash(product)

    # analyze
    assert expected == actual

def test_create_train_car_again():
    # setup
    capacity = 20

    # invoke
    train_car = TrainCar(capacity)

    # analyze
    assert capacity == train_car.get_capacity()
    assert train_car.is_empty()
    assert not train_car.is_full()
    assert "[]" == str(train_car)

def test_load_train_uneven():
    # setup
    product1 = Product("A1", "P1")
    product2 = Product("B2", "P2")
    product3 = Product("C3", "P3")
    product4 = Product("D4", "P4")
    shipment = [product1, product2, product3, product4]
    capacity = 3
    expected = "[[" + str(product3) + ", " + str(product2) + \
        ", " + str(product1) + "], " + "[" + str(product4) + "]]"

    # invoke
    train = load_train(shipment, capacity)

    # analyze
    assert expected == str(train)

def test_unload_train_uneven():
    # setup
    product1 = Product("A1", "P1")
    product2 = Product("B2", "P2")
    product3 = Product("C3", "P3")
    product4 = Product("D4", "P4")
    shipment = [product1, product2, product3, product4]
    capacity = 3
    train = load_train(shipment, capacity)
    expected = [product3, product2, product1, product4]


    # invoke
    actual = unload_train(train)

    # analyze
    assert expected == actual
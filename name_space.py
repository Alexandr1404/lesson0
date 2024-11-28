def test_function():
    def inner_function():
            print("Я в области видимости функции test_function")

    inner_function()

test_function()

# inner_function()  -- данная функция находится в локальном пространстве функции test_function()
# поэтому вызов inner_function() не выполняется
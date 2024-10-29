def test_function():
    def inner_function():
        print("Я в области видимости функции", test_function.__name__)
    inner_function()
inner_function()

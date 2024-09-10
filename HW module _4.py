def test_function():
    def inner_function():
        print("Я в облости видимости ")
    inner_function()
test_function()
inner_function()
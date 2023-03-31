# Python
PyTest Decorators:

@pytest.mark.skip: Bir testi daha sonradan işlemler yapmak için ve diğer testlerin çalışılabilirliğini kontrol etmek için belirlenen testin atlanılmasını sağlamak için kullanılır.

@pytest.mark.xfail: Testin başarısız olmasını istediğimizde kullanırız. Ama bu durum bizim kontrolümüz altında gerçekleşecektir.

@pytest.mark.timeout: Testin belirli bir süre içerisinde yapılmasını eğer süre aşılırsa da testin sonlandırılması için kullanılır.

@pytest.fixture: Aynı şeylerin tekrar tekrar çalışmasını önlemek için kullanılır.

@pytest.mark.order: Hangi testin önce hangi testin sonra yapılacağını belirlemek için kullanılır.

@pytest.mark.dependency: Testler arasındaki bağımlılıkları belirlemek için kullanılır. Testler arasında birbirlerine bağımlı bir sıra ile çalıştırma yapılabilir.

@pytest.mark.parametrize: Testleri parametreleştirmek için kullanılır. Böylelikle bir sınıfta birden fazla veri seti tanımlanabilmektedir.

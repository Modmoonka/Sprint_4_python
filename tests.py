from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize('book', ['Властелин колец', 'Книга теней'])
    def test_add_new_book_add_book(self, book):
        
        collector = BooksCollector()

        collector.add_new_book(book)
        assert collector.get_book_genre(book) == ''

    #1 Проверка добавления двух книг в список
    def test_add_new_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_new_book('Книга теней')
        assert len(collector.get_book_genre()) == 2

    #2 Проверка назначения книгам жанра
    def test_set_book_genre(self):
        
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        
        collector.add_new_book('Книга теней')
        collector.set_book_genre('Книга теней', 'Ужасы')

        assert collector.get_book_genre()['Властелин колец'] ==  'Фантастика'
        assert collector.get_book_genre()['Книга теней'] ==  'Ужасы'

    #3 Проверка возвращения жанра книги
    def test_get_book_genre(self):
        
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.get_book_genre()['Властелин колец'] == 'Фантастика'

    #4 Проверка поулчения жанра, если жанр не существует
    def test_get_book_genre_if_genre_false(self):

        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', "Драма")
        assert collector.get_book_genre('Властелин колец') != "Драма"


    #5 Книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_get_books_for_children(self):
        
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Книга теней', 'Ужасы')

        assert collector.get_books_for_children() == ['Властелин колец']

    #6 Провекра на добавление книг в избранное
    def test_add_book_in_favorites(self):

        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')

        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    #7 Провекра на удаление книг из избранного
    def test_delete_book_from_favorites_and_delete(self):

        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == []

    #8 Проверка на отсутствие возможности добавления в избранное при отсутвие книги в коллекции
    def test_get_list_of_favorites_books(self):

        collector = BooksCollector()
        collector.add_book_in_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == []

    #9 Проверка попытки добавления уже имеющейся книги в избранное

    def test_add_book_in_favorite_same_book(self):

        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        
        assert len(collector.get_list_of_favorites_books()) == 1

    #10 Проверка метода get_book_genre
    def test_get_book_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Ужасы')
        collector.set_book_genre('Ужасы')
        collector.get_book_genre('Ужасы')

        assert collector.get_book_genre() == ''
   
    # 11 Проверка метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_returns_correct_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('Ворон')
        collector.set_book_genre('Ворон', 'Ужасы')
        books = collector.get_books_with_specific_genre("Фантастика")
        assert 'Властелин колец' in books
        assert 'Ворон' not in books
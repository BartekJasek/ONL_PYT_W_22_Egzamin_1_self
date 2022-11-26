from exam_lib import Book


class EBook(Book):
    def __init__(self, title, author, pages, size):
        super().__init__(title, title)
        super().__init__(author, author)
        super().__init__(pages, pages)
        self.size = size

    def _set_registration_code(self, registration_code):
        if registration_code is str and len(registration_code) == 16:
            self._registration_code = registration_code
        else:
            self._registration_code = None

    @staticmethod
    def check_code():
        if self._registration_code is str and len(self.registration_code) == 16:
            return True
        else:
            return False

    def get_registration_code(self):
        return self._registration_code

    def set_registration_code(self, new_registration_code):
        self._set_registration_code(new_registration_code)

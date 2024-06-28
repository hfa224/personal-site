import csv

class Book:
  def __init__(self, title, author, picker, date, genre, cover_image_url, rating):
        self.title = title
        self.author = author
        self.picker = picker
        self.date = date
        self.genre = genre
        self.cover_image_url = cover_image_url
        self.rating = rating

  def make_from_row(row):

     rating = {
        "H": row[4],
        "M": row[5],
        "B": row[6]
     }

     cover_img = "https://covers.openlibrary.org/b/isbn/"+ row[9] + "-M.jpg"

     return Book(row[0], row[1], row[2], row[3], row[7], cover_img, rating)


def read_book_data() :
  with open('static/data/Berlin Beer & Book Club.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[2]} picked {row[0]} by {row[1]} in {row[3]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

def get_book_image_url(isbn):
  return "https://covers.openlibrary.org/b/isbn/" + isbn + "-M.jpg";

def read_book_isbns() :
  book_array = []
  with open('static/data/Berlin Beer & Book Club.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            book_array.append(Book.make_from_row(row))
  return book_array
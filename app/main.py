from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_inst = [Customer(customer["name"], customer["food"]) for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)
    for customer in customers_inst:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customers_inst, cinema_cleaner)

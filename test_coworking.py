
class CoworkingSpace:
    def __init__(self):
        self.desks = {"D1": "Available", "D2": "Available"}
        self.rooms = {"R1": "Available", "R2": "Available"}

    def book_desk(self, desk):
        if self.desks.get(desk) == "Available":
            self.desks[desk] = "Booked"
            return True
        return False

    def book_room(self, room):
        if self.rooms.get(room) == "Available":
            self.rooms[room] = "Booked"
            return True
        return False

    def cancel_desk(self, desk):
        if self.desks.get(desk) == "Booked":
            self.desks[desk] = "Available"
            return True
        return False

    def check_in(self, desk):
        if self.desks.get(desk) == "Booked":
            return "Checked in"
        return "Not booked"


def test_desk_booking():
    c = CoworkingSpace()
    assert c.book_desk("D1") is True


def test_duplicate_booking():
    c = CoworkingSpace()
    c.book_desk("D1")
    assert c.book_desk("D1") is False


def test_meeting_room_booking():
    c = CoworkingSpace()
    assert c.book_room("R1") is True


def test_desk_cancellation():
    c = CoworkingSpace()
    c.book_desk("D1")
    assert c.cancel_desk("D1") is True


def test_check_in():
    c = CoworkingSpace()
    c.book_desk("D1")
    assert c.check_in("D1") == "Checked in"

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance (name, str):
            raise Exception("The name is not of type string")
        if not len(name) > 0:
            raise Exception("The name does not have more than 0 characters")
        self._name = name

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        if hasattr(self, '_hometown'):
            raise AttributeError("Hometown is immutable")
        if not isinstance (hometown, str):
            raise Exception("The hometown is not of type string")
        if not len(hometown) > 0:
            raise Exception("The hometown does not have more than 0 characters")
        self._hometown = hometown

    def concerts(self):
        concerts_list = [concert for concert in Concert.all if concert.band == self]
        if len(concerts_list) < 0:
            return None
        else:
            return concerts_list

    def venues(self):
        venues_list = [concert.venue for concert in Concert.all if concert.band == self]
        if len(venues_list) < 0:
            return None
        else:
            return list(set(venues_list))

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        concerts_list = [concert for concert in Concert.all if concert.band == self]
        concert_introductions = [f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for concert in concerts_list]
        if len(concerts_list) < 0:
            return None
        else:
            return concert_introductions


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance (date, str):
            raise Exception("The date is not of type string")
        if not len(date) > 0:
            raise Exception("The date does not have more than 0 characters")
        self._date = date
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, band):
        if not isinstance (band, Band):
            raise Exception("The band is not of the class type Band")
        self._band = band
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, venue):
        if not isinstance (venue, Venue):
            raise Exception("The venue is not of the class type Venue")
        self._venue = venue

    def hometown_show(self):
        if self.band.hometown == self.venue.city:
            return True
        else:
            return False

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance (name, str):
            raise Exception("The name is not of type string")
        if not len(name) > 0:
            raise Exception("The name does not have more than 0 characters")
        self._name = name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not isinstance (city, str):
            raise Exception("The city is not of type string")
        if not len(city) > 0:
            raise Exception("The city does not have more than 0 characters")
        self._city = city

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        bands_list = [concert.band for concert in Concert.all if concert.venue == self]
        return list(set(bands_list))
